function [Q] = findQ(A)
    [m,n] = size(A);
    P = findP(A);
    EA = P*A;
    EA_trans = EA';
    both = [EA_trans eye(n)];
    both_rref = rref(both);
    Nr_trans = both_rref(:,1:m);
    Q_trans = both_rref(:,m+1:end);
    Q = Q_trans';
end