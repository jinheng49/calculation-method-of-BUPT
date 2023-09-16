function y = Factorial( n )
global y
y=zeros(n,1);

f(n);

end

function z = f( n )
global y
if(n==1)
    z=1;
else
    z=n*f(n-1);
end

y(n)=z;
    
end
