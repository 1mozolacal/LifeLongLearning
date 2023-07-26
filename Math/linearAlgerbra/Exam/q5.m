basis = [1 0 0; 0 1 0;0 0 1;1 1 1];
[Q R] = qr(basis);
Q5 = Q(:,1:3)