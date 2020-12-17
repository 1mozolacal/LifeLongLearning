dig(0). dig(1). dig(2). dig(3). dig(4). dig(5). dig(6). dig(7). dig(8). dig(9).

solve([S,A,N,T,C,L,U,X,M]):-
dig(A),dig(S), S>0,
S is (A - S) mod 10,
Carry1 is ( (A - S) - 9) // 10,
dig(T),dig(U),
A is (T - U + Carry1) mod 10,
Carry2 is ( (T - U + Carry1) - 9) //10,
dig(N),dig(A),
M is (N - A + Carry2) mod 10,  
Carry3 is ( (N - A + Carry2) - 9) //10,
dig(A),dig(L),

X is (A - L + Carry3) mod 10, X>0,

Carry4 is ( (A - L + Carry3) - 9 ) // 10,
write("make the X\n"),
dig(S),dig(C),C>0,

0 is S - C + Carry4,
write(S),write(A),write(N),write(T),write(A),write("\n"),
write(C),write(L),write(A),write(U),write(S),write("\n "),
write(X),write(M),write(A),write(S).
