function [P , Q ,EA,N] = PAQ2(A)

[m,n] = size(A); %A m x n
w1 = rref([A eye(m)]); % (EA | P) is m x (n+m)
P = w1(:,n+1:end);   
EA = w1(:,1:n); % EA is m x n -> EA^t is n x m

w2 = rref([EA' eye(n)]); % (N^t|Q^t) is n x (m+n)
Q = w2(:,m+1:end)';  % transpose of n x n, which is n x n
N = w2(:,1:m)'; % transpose of n x m , which is m x nEA
end
