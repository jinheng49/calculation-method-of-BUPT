clear
time0=cputime;

N=100;

x0=-1:2/N:1;              %等分点
% j=1:N-1;
% x0=[1,cos(pi*j/N),-1];

y0=1./(1+25*x0.^2);

x=-1:2/N/10:1;

% pp=interp1(x0,y0,'spline','pp');              %三次样条插值
% pp=csape(x0,y0,'periodic');              %三次样条插值
% pp=csape(x0,y0,'second');              %三次样条插值
pp=csape(x0,y0,'complete');              %三次样条插值
y=ppval(pp,x);


time=cputime-time0

plot(x,y)

yexact=1./(1+25*x.^2);
error=norm(y-yexact)

