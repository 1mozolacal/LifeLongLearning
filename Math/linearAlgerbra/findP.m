function [P] = findP(A)
    A_size = size(A)
    [Both_,AI_,P] = lineSol(A,eye(A_size(1)))
end