function B = columnSpace(A)
    [Ea c] = rref(A);
    B = A(:,c);
end