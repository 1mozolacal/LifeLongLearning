% find line of best fit
x = [-1 0 1 2]';
y = [4 1 0 -5]';
v = vander(x);
V =v(:,2:4)
v_trans_v = V'*V;
v_trans_y = V'*y;
a=v_trans_v\v_trans_y
%V\y; matalb short cut
%find error
err = sqrt((y-V*a)'*(y-V*a));
% err = norm(y-V*a)
%x_line = -2:0.01:3;
%y_line = a(1)*x_line + a(2);
%plot(x,y,'o',x_line,y_line,'-')