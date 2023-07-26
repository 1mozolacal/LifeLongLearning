load("MTH719FinalData.mat");

[P Q E N]= PAQ(A);
rank(A);
Q8 = P(1:3,:)