function A = moorePenrose(a)
[B C] = fullRankFactor(a);
A = C'*inv(B'*a*C')*B'