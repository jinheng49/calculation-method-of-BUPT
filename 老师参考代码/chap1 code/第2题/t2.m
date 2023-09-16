clear

T1=2e6;
T2=1e4;

time0=cputime;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
n1=1e10;
for j=1:T1
    e1=(1+1/n1)^n1;
end
time1=cputime;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
n2=9;


for j=1:T2
    ff=Factorial(n2);
    e2=1;
    for k=1:n2
       e2=e2+1/ff(k); 
    end
end
time2=cputime;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

cputime1=time1-time0
e1
error1=abs(exp(1)-e1)


cputime2=time2-time1
e2
error2=abs(exp(1)-e2)