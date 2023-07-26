load("MTH719FinalData.mat");
[V D] = eig(B)

bn1 = B - 2*eye(4)
nullSpace(bn1)