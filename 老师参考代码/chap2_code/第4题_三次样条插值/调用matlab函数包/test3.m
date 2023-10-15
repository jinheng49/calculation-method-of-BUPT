clear
time0=cputime;

N=100;

x0=-1:2/N:1;              %�ȷֵ�
% j=1:N-1;
% x0=[1,cos(pi*j/N),-1];

y0=1./(1+25*x0.^2);

x=-1:2/N/10:1;

% pp=interp1(x0,y0,'spline','pp');              %����������ֵ
% pp=csape(x0,y0,'periodic');              %����������ֵ
% pp=csape(x0,y0,'second');              %����������ֵ
pp=csape(x0,y0,'complete');              %����������ֵ
y=ppval(pp,x);


time=cputime-time0

plot(x,y)

yexact=1./(1+25*x.^2);
error=norm(y-yexact)

