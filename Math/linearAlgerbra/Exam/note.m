%{
m = rows
n= columns

B = A'
B = ctranspose(A)


[Q,R] = qr(A) performs a QR decomposition on m-by-n matrix A such that A = Q*R. The factor R is an m-by-n upper-triangular matrix, and the factor Q is an m-by-m orthogonal matrix.

[V,D] = eig(A) returns diagonal matrix D of eigenvalues and matrix V whose columns are the corresponding right eigenvectors, so that A*V = V*D.

%}