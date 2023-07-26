function B = leftNullSpace(A)
    At = A';
    [m n] = size(At);    
    [Ea c] = rref(At);
    Ea_and_P = rref([At eye(m)]);
    P = Ea_and_P(:,n+1:end);
    Eat = Ea';
    Eat_and_Qt = rref([Eat eye(n)]);
    Qt = Eat_and_Qt(:,m+1:end);
    Q = Qt';
    r = rank(At);
    last_col = Q(:,r+1:end);
    B = last_col;
end