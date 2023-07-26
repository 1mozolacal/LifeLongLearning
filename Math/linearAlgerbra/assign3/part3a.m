A= [2 -2 -1;-2 2 1;-1 1 5]';
B =[10 -26 -2];
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