function B = nullSpace(A)
    [m n] = size(A);    
    [Ea c] = rref(A);
    Ea_and_P = rref([A eye(m)]);
    P = Ea_and_P(:,n+1:end);
    Eat = Ea';
    Eat_and_Qt = rref([Eat eye(n)]);
    Qt = Eat_and_Qt(:,m+1:end);
    Q = Qt';
    r = rank(A);
    last_col = Q(:,r+1:end);
    B = last_col;
end