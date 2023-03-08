function [P , Q ,EA,N] = pqal(A)

[m,n] = size(A); %A m x n
w1 = rref([A eye(m)]); % (EA | P) is m x (n+m)
P = w1(:,n+1:end);   
EA = w1(:,1:n); % EA is m x n -> EA^t is n x m

w2 = rref([EA' eye(n)]); % (N^t|Q^t) is n x (m+n)
Q = w2(:,m+1:end)';  % transpose of n x n, which is n x n
N = w2(:,1:m)'; % transpose of n x m , which is m x nEA
end


%Rules: Linear Independant when only has trivial solution Ax=0
% for A m x n
%rank(A) = rank(A|B)=n => unique solution
% rank(A) = rank(A|B)<n => infinitely many solutions
% rank(A) < rank(A|B) => inconsistent => no solutions

%AX=B has a solution for every B only if rank(A)=m
% A is invertible iff rank A=n iff AX=0 has only a trivial solution

%for powers, either do fliplr(vander([vector of initial numbers])) or
% explicitly do x=[column vector of initial numbers], x.^[vector of powers]
% fliplr(vander([0,1,2])) 
% 
% ans =
% 
%      1     0     0
%      1     1     1
%      1     2     4
% 
% x=[0 1 2]'
% 
% x =
% 
%      0
%      1
%      2
% 
% x.^[1 2 3]
% 
% ans =
% 
%      0     0     0
%      1     1     1
%      2     4     8
% 
% x.^[0 1 2]
% 
% ans =
% 
%      1     0     0
%      1     1     1
%      1     2     4