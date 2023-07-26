function B = rowSpace(A)
    At = A';
    [Ea c] = rref(At);
    B = At(:,c);
end