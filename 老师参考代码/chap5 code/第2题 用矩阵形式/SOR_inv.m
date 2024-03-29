function x = SOR_inv( A,b,omega )
%SOR_INV 此处显示有关此函数的摘要


N=size(A,1);


D=diag(diag(A,0));    %求矩阵A的第1条对角线的元素。
L=-tril(A,-1);    %求矩阵A的第-1条对角线以下的元素。
U=-triu(A,1);    %求矩阵A的第1条对角线以上的元素。

invDL=(D-omega*L)\eye(N);
B=invDL*((1-omega)*D+omega*U);
g=invDL*omega*b;

x0=g;
x=B*x0+g;

while(norm(x-x0)>1e-14)
    x0=x;
    x=B*x0+g;
end





end

