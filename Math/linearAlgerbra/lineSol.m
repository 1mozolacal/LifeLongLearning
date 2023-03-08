function [Both,AI,R] = lineSol(A,B)
    A_size = size(A);
    both = [A B];
    Both = rref(both);
    AI = Both(:,1:A_size(2));
    R = Both(:,A_size(2)+1:end);
end