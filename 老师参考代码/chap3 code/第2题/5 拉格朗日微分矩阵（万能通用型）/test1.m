clear 
format long

time0=cputime;

N=32;

j=[0:1:N]; 
x=[cos(pi*j/N)];          %切比雪夫-高斯-罗巴托点，也可以换成其他点

F0=zeros(N+1,1);
F2=zeros(N+1,1);

for k=0:N
   F0(1+k)=sin(x(1+k))+x(1+k)^3;          %函数0阶导
   F2(1+k)=-sin(x(1+k))+6*x(1+k);          %函数2阶导
end


D2=DM(2,N,x);          %拉格朗日二阶微分矩阵

F_2=D2*F0;          %函数2阶导数值解

error=norm(F_2-F2)          %函数2阶导数值解和精确解差的范数，误差
CPUTIME=cputime-time0



% l=4;k*sin(k*acos(x(l)))/sqrt(1-x(l)^2)
% ee=0.000000001;
% (cos(k*acos(x(l)+ee))-cos(k*acos(x(l))))/ee

