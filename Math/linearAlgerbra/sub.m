%clear()
load('MTH719MidtermData.mat')



ant_m = [0.4 0 0 0.2;0 0.4 0.3 0.2;0 0.3 0.4 0.2;0.6 0.3 0.3 0.4]
after = [24 50 52 74]'
before = lineSol(ant_m,after)

ant2 =[-0.6 0 0 0.2;0 -0.6 0.3 0.2;0 0.3 -0.6 0.2;0.6 0.3 0.3 -0.6]