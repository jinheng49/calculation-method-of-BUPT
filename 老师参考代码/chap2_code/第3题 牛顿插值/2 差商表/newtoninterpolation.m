function y = newtoninterpolation(x0,y0,x )

n=length(x0);
m=length(x);
A=zeros(n);    %定义差商表
A(:,1)=y0;      %差商表第一列为y0
for j=2:n               %j为列标
    for i=1:(n-j+1)     %i为行标
        A(i,j)=(A(i,j-1)-A(i+1,j-1))/(x0(i)-x0(i+j-1));   %计算差商表
    end
end
%根据差商表,求对应的牛顿插值多项式在x0=x(l)处的值y(l)

a=A(1,:)';

for l=1:m
    z=x(l);
    M=zeros(1,n);
    
    M(1)=1;
    for j=2:n
        M(j)=M(j-1)*(z-x0(j-1));
    end
    y(l)=sum(M'.*a);
%     y(l)=M*a;
end

end


