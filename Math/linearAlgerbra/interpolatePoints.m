function [X] = interpolatePoints(points)
  A = interpolateMatrix(points)
  rref(A)
  B = points(:,2);
  X = A\B;

end

function [A] = interpolateMatrix(points)
   n= length(points);
   A = zeros(n);
   for i = 1:n
        xVal = points(i,1);
       for j = 0:n-1
           A(i,n-j) = xVal^j;
       end
   end

end

%{
Example:
points = [-1 6;0 -1;1 -2;2 -3;3 14]

interpolatePoints(points)

ans =

     1    -1     1    -1     1
     0     0     0     0     1
     1     1     1     1     1
    16     8     4     2     1
    81    27     9     3     1
%}