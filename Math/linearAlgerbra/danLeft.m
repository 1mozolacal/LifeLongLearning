function lnull = leftNullSpace(A)
[m,n] = size(A);
r=rank(A);
w = rref([A eye(m)]); 
P = w(:,n+1:m+n);
lnull = P(r+1:m,:)';