%clear()
load('MTH719MidtermData.mat')

points=[1 1;2 10;3 35;4 84];
interpolatePoints(points);


P=[1 0 0 -1 -1 -1;0 1 0 -2 1 1;0 0 1 -2 -2 -2;0 0 0 0 0 0]

save("Midterm.mat","P","A")