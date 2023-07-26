load("MTH719FinalData.mat");
%{
mat = [3 -2 -2;
       2 -1 1
       ]
rref(mat)
%}

[P Q N E] = PAQ(W)
P_in = inv(P)
mat2 = [1 0 0 0 1 0;0 1 0 0 0 1; 0 0 1 0 1 2;0 0 0 1 4 7; 0 0 0 0 0 0]

Q2 = P_in * mat2