A =[ 27 10 -6 3;10 4 -2 1; -7 -2 2 -1; -8 -3 2 -1; -33 -12 8 -4]';
columnSpace(A);
nullSpace(A);
rref(A);
B = [ 27 10 -6 3;10 4 -2 1; -8 -3 2 -1]';
[P Q E N] = PAQ(B)
BB = [ 27 10 -6 3;10 4 -2 1; -8 -3 2 -1;0 0 1 0]';