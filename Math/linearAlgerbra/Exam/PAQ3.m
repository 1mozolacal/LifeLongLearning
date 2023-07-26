function [P , Q ,EA,N] = PAQ3(A)

[m,n] = size(A);
w1 = rref([A eye(m)]);
P = w1(:,n+1:m+n);

EA = w1(:,1:n);
w2 = rref([EA' eye(n)])
Q = w2(:,n:m+n)';   
N = w2(:,1:n-1)';
end

%Rules: Linear Independant when only has trivial solution Ax=0