% find line of best fit
x = [-1 0 1 2]';
y = [4 1 0 -5]';
v = vander(x);
V =v(:,1:4)
solution = V\y