dig(0). dig(1). dig(2). dig(3). dig(4). dig(5). dig(6). dig(7). dig(8). dig(9).



solve([S,A,N,T,C,L,U,X,M]):-
dig(A),dig(S), S>0,
S is (A - S) mod 10,
Carry1 is (S-A+9) //10,
dig(T),dig(U),
A is (T - U - Carry1) mod 10,
Carry2 is ( (U - T - Carry1) + 9) //10,
dig(N),dig(A),
M is (N - A - Carry2) mod 10,  
Carry3 is ( (A - N - Carry2) + 9) //10,
dig(A),dig(L),

X is (A - L - Carry3) mod 10, X>0,
Carry4 is ( (L - A - Carry3) + 9 ) // 10,
dig(S),dig(C),C>0,

0 is S - C + Carry4,
write(S),write(A),write(N),write(T),write(A),write("\n"),
write(C),write(L),write(A),write(U),write(S),write("\n "),
write(X),write(M),write(A),write(S).


solve([S,A,N,T,C,L,U,X,M]):-
dig(A),dig(S), 
dig(T),dig(U),
dig(N),dig(A),
dig(A),dig(L),
dig(S),dig(C),
dig(X),dig(M),
dig(Carry1),dig(Carry2),dig(Carry3),dig(Carry4),

S>0,
S is (A - S) mod 10,
Carry1 is (S-A+9) //10,
A is (T - U - Carry1) mod 10,
Carry2 is ( (U - T - Carry1) + 9) //10,
M is (N - A - Carry2) mod 10,  
Carry3 is ( (A - N - Carry2) + 9) //10,
X is (A - L - Carry3) mod 10, X>0,
Carry4 is ( (L - A - Carry3) + 9 ) // 10,
C>0,
0 is S - C + Carry4,

write(S),write(A),write(N),write(T),write(A),write("\n"),
write(C),write(L),write(A),write(U),write(S),write("\n "),
write(X),write(M),write(A),write(S).