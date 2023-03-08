function [P] = reduce(A)
    A_size = size(A);
    AI = eye(A_size(1));
    both = [A AI];
    r_both = rref(both);
    P = r_both(:,A_size(2)+1:end);
end
%{
Same thing as findP
%}