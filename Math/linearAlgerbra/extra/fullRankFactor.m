function [B,C] = fullRankFactor(A)

[m,n] = size(A);
[Ea c] = rref(A);
B = A(:,c);
C = B\A
