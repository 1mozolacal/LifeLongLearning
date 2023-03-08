function [Q] = findA(A)
    [m,n] = size(A);
    P = findP(A);
    EA = P*A;
    EA_trans = EA';
    both = [EA_trans eye(n)]
    A_size = size(A)
    [Both_,AI_,P] = lineSol(A,eye(A_size(1)))
end