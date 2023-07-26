
%A= [1 1 2; 1 4 3; 2 3 5]';
A= [1 1 2; 1 1 3; 2 3 1]';
B =[0 0 0];
j=0;

[P D] = eig(A);
B_prime = B*P;
x_prime =D(1,1);
y_prime =D(2,2);
z_prime =D(3,3);
primes = [x_prime y_prime z_prime]
comp = B_prime./primes./2
prep_square = comp.*comp.*primes;
summs = j- sum( prep_square)


%{
A= [1 0.1; 0.1 1]';
B =[0];
j=-1;

[P D] = eig(A);
B_prime = B*P;
x_prime =D(1,1);
y_prime =D(2,2);
primes = [x_prime y_prime]
comp = B_prime./primes./2
prep_square = comp.*comp.*primes;
summs = j- sum( prep_square)
%}
