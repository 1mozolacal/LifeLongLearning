% find line of best fit
x = (10:10:80)';
y = [25 70 380 550 610 1220 830 1450]';
v = vander(x);
V =v(:,6:8);
n = [1 0];
other_V = x.^n;%same as vander
v_trans_v = V'*V;
v_trans_y = V'*y;
a=v_trans_v\v_trans_y;
%V\y; matalb short cut
%find error
err = sqrt((y-V*a)'*(y-V*a));
% err = norm(y-V*a)
%x_line = 10:0.01:80;
%y_line = a(1)*x_line + a(2);
%plot(x,y,'o',x_line,y_line,'-')