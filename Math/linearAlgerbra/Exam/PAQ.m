function [P , Q ,EA,N] = PAQ(A)

[m,n] = size(A);
w1 = rref([A eye(m)]);
P = w1(:,n+1:m+n);

EA = w1(:,1:n);
w2 = rref([EA' eye(n)])
Q = w2(:,m+1:end)';   
N = w2(:,1:m)';
end

%Rules: Linear Independant when only has trivial solution Ax=0