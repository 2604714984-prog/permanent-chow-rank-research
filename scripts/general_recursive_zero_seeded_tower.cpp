#include <algorithm>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>
using i64=std::int64_t;
void req(bool c,const std::string&m){if(!c)throw std::runtime_error(m);} 
i64 C(int n,int k){if(k<0||k>n)return 0;k=std::min(k,n-k);i64 r=1;for(int i=1;i<=k;++i)r=r*(n-k+i)/i;return r;}
i64 cr(int mask,int n,int d){i64 r=0;int idx=1;for(int v=0;v<n;++v)if(mask&(1<<v)){r+=C(v,idx);++idx;}req(idx==d+1,"colex");return r;}
struct Inv{int n,d,M,L,maxc;std::vector<int>p,w,gamma;Inv(int nn,int dd):n(nn),d(dd){std::vector<std::pair<i64,int>>layer;for(int mask=0;mask<(1<<n);++mask)if(__builtin_popcount((unsigned)mask)==d)layer.push_back({cr(mask,n,d),mask});std::sort(layer.begin(),layer.end());M=layer.size();L=C(n,d-1);maxc=L*L;req(M==C(n,d),"M");std::set<int>sh;p.push_back(0);for(auto it:layer){int mask=it.second;for(int v=0;v<n;++v)if(mask&(1<<v))sh.insert(mask^(1<<v));p.push_back(sh.size());int lm=0;while(mask&(1<<lm))++lm;w.push_back(lm);}req((int)sh.size()==L,"shadow");int ws=0;for(int x:w)ws+=x;req(ws==L,"weights");build();}
void build(){const int neg=-1000000000,W=M+1,costs=maxc+1;auto off=[&](int u,int c){return u*costs+c;};std::vector<int>dp(W*costs,neg),nx(W*costs,neg);dp[off(M,0)]=0;int reachable_max=0;for(int wt:w){if(wt==0){for(int u=0;u<=M;++u)for(int c=0;c<=reachable_max;++c){int&v=dp[off(u,c)];if(v>neg/2)v+=u;}continue;}std::fill(nx.begin(),nx.end(),neg);
#pragma omp parallel for schedule(static)
for(int c=0;c<=reachable_max;++c){int suf=neg;for(int x=M;x>=0;--x){suf=std::max(suf,dp[off(x,c)]);int nc=c+wt*p[x];if(suf>neg/2&&nc<=maxc)nx[off(x,nc)]=std::max(nx[off(x,nc)],suf+x);}}dp.swap(nx);reachable_max=std::min(maxc,reachable_max+wt*L);}gamma.assign(maxc+1,0);int pref=0;for(int c=0;c<=maxc;++c){int ex=0;for(int u=0;u<=M;++u)ex=std::max(ex,dp[off(u,c)]);pref=std::max(pref,ex);gamma[c]=pref;}req(gamma.back()==M*M,"full");}};
int inc(int n,int d){return (d*d-1)/n;}
int direct_seed(int n,int d){int z=inc(n,d);if(d>=3){int q=(d*d+1)/n;if(q>=2)z=std::max(z,q);}if(d==4){int q=(d*d+d+3)/n;if(q>=2)z=std::max(z,q);}if(d>=5){int q=(d*d+d+4)/n;if(q>=2)z=std::max(z,q);}return z;}
std::vector<int> closure(int n){std::vector<int>z(n+1,0);for(int d=2;d<=n;++d)z[d]=std::max(direct_seed(n,d),z[d-1]+inc(n,d));return z;}
std::vector<int> expected(int n){static const std::map<int,std::vector<int>>e={{3,{3,4}},{4,{4,7,8}},{5,{5,11,14,15}},{6,{6,16,24,26,27}},{7,{7,22,39,46,48,49}},{8,{8,29,59,80,87,89,90}},{9,{9,37,87,136,155,161,163,164}},{10,{10,46,123,219,280,299,305,307,307}}};return e.at(n);} 
std::string vec(const std::vector<int>&v,int start,int end){std::ostringstream o;o<<"[";for(int i=start;i<end;++i){if(i>start)o<<",";o<<v[i];}o<<"]";return o.str();}
int main(){try{std::cout<<"{\"rows\":{";bool fn=true;for(int n=3;n<=10;++n){int maxq=1<<(n-1);auto z=closure(n);std::vector<std::vector<int>>b(n),s(n);std::vector<int>tb(n,-1),ts(n,-1);b[1].resize(maxq+1);s[1].resize(maxq+1);for(int q=0;q<=maxq;++q)b[1][q]=s[1][q]=std::min(n*n,q*n);tb[1]=ts[1]=n;i64 changed=0,maxred=0;for(int d=2;d<=n-1;++d){Inv inv(n,d);int M=C(n,d),A=M*M;b[d].assign(maxq+1,0);s[d].assign(maxq+1,0);i64 pb=0,ps=0;for(int q=1;q<=maxq;++q){int db=std::min({A,q*M,inv.gamma[b[d-1][q]]});int ds=(q<=z[d])?0:std::min({A,q*M,inv.gamma[s[d-1][q]]});pb=std::min(pb,(i64)db-(i64)q*M);ps=std::min(ps,(i64)ds-(i64)q*M);b[d][q]=(int)((i64)q*M+pb);s[d][q]=(int)((i64)q*M+ps);req(s[d][q]<=b[d][q],"monotone");if(s[d][q]!=b[d][q]){++changed;maxred=std::max(maxred,(i64)b[d][q]-s[d][q]);}}for(int q=0;q<=maxq;++q){if(tb[d]<0&&b[d][q]==A)tb[d]=q;if(ts[d]<0&&s[d][q]==A)ts[d]=q;}req(tb[d]>=0&&ts[d]>=0,"sat");}
std::vector<int>ob(tb.begin()+1,tb.end()),os(ts.begin()+1,ts.end());req(ob==expected(n),"baseline");req(os==ob,"seeded changed threshold");if(!fn)std::cout<<",";fn=false;std::cout<<"\""<<n<<"\":{\"zero_counts\":"<<vec(z,1,n+1)<<",\"thresholds\":"<<vec(ts,1,n)<<",\"changed_capacity_cells\":"<<changed<<",\"maximum_capacity_reduction\":"<<maxred<<"}"<<std::flush;}std::cout<<"}}\nRECURSIVE_ZERO_SEEDED_TOWER_AUDIT_PASS\n";return 0;}catch(const std::exception&e){std::cerr<<"FAIL "<<e.what()<<"\n";return 1;}}
