Q = [1 0 0 0;-1 1 0 0;1 -2 1/2 0;-1 3 -3/2 1/6]'
Q_in = inv(Q)
V = Q_in * [6 1 -7/2 1/2]'
Q*V
Q*[3 -4 2 3]'
