"""Small, dependency-free worker selection for bounded exact replays.

The returned worker count is a CLI scheduling choice only.  Callers must not
put it in a mathematical payload or frozen certificate.
"""

from __future__ import annotations

import ctypes
import os


GIB = 2**30
AUTO_MEMORY_BUDGET_BYTES = 8 * GIB
AUTO_RESERVED_BYTES = 2 * GIB
CPU_RESERVE = 4


def parse_worker_argument(value: str) -> int:
    """Return 0 for ``auto`` or a validated explicit worker count."""

    normalized = value.strip().lower()
    if normalized == "auto":
        return 0
    count = int(normalized)
    if count < 1 or count > 64:
        raise ValueError("workers must be auto or an integer in [1, 64]")
    return count


def available_memory_bytes() -> int | None:
    """Return currently available physical memory without extra dependencies."""

    if os.name == "nt":
        class _MemoryStatusEx(ctypes.Structure):
            _fields_ = [
                ("length", ctypes.c_ulong),
                ("memory_load", ctypes.c_ulong),
                ("total_phys", ctypes.c_ulonglong),
                ("avail_phys", ctypes.c_ulonglong),
                ("total_page", ctypes.c_ulonglong),
                ("avail_page", ctypes.c_ulonglong),
                ("total_virtual", ctypes.c_ulonglong),
                ("avail_virtual", ctypes.c_ulonglong),
                ("avail_extended", ctypes.c_ulonglong),
            ]

        status = _MemoryStatusEx()
        status.length = ctypes.sizeof(status)
        try:
            if ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(status)):
                return int(status.avail_phys)
        except (AttributeError, OSError):
            pass
        return None

    try:
        with open("/proc/meminfo", encoding="ascii") as handle:
            for line in handle:
                if line.startswith("MemAvailable:"):
                    return int(line.split()[1]) * 1024
    except (FileNotFoundError, OSError, ValueError):
        return None
    return None


def resolve_worker_count(
    requested: int,
    *,
    max_workers: int,
    estimated_bytes_per_worker: int,
    gpu: bool = False,
) -> int:
    """Resolve explicit or adaptive workers while keeping memory bounded."""

    if not 1 <= max_workers <= 64:
        raise ValueError(max_workers)
    if estimated_bytes_per_worker <= 0:
        raise ValueError(estimated_bytes_per_worker)
    if gpu:
        if requested not in (0, 1):
            raise ValueError("GPU replay requires --workers 1 or --workers auto")
        return 1
    available = available_memory_bytes()
    if available is None:
        memory_budget = AUTO_MEMORY_BUDGET_BYTES
    else:
        memory_budget = min(
            AUTO_MEMORY_BUDGET_BYTES,
            max(estimated_bytes_per_worker, available - AUTO_RESERVED_BYTES),
        )
    if requested:
        if requested > max_workers:
            raise ValueError(f"workers must be <= {max_workers}")
        if requested > max(1, (os.cpu_count() or 1) - CPU_RESERVE):
            raise ValueError(
                f"workers must leave {CPU_RESERVE} logical CPUs free"
            )
        if requested * estimated_bytes_per_worker > memory_budget:
            raise ValueError(
                "requested workers exceed the bounded memory budget; "
                "use --workers auto or a smaller explicit value"
            )
        return requested

    cpu_count = max(1, (os.cpu_count() or 1) - CPU_RESERVE)
    memory_workers = max(1, memory_budget // estimated_bytes_per_worker)
    return min(max_workers, cpu_count, int(memory_workers))
