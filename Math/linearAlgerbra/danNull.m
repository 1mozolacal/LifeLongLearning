
function null = danNull(A)
[m,n] = size(A);
EA = rref(A);
w = rref([EA' eye(n)]);
Q = w(:,m+1:m+n)';
r=rank(A);
null = Q(:,r+1:n);