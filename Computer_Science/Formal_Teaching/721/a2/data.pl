/*
Submission by:
Calvin Mozola           500909122       Section 5
Cesar Perez             500882780       Section 6
Daniel Mezhibovski      500899282       Section 4
*/

/* ATOMIC SENTENCES */
value(historyK,p1,bad). value(debt,p1,high). value(collateral,p1,none).
value(hist,p2,unknown). value(debt,p2,high). value(collateral,p2,none).
value(hist,p3,unknown). value(debt,p3,low). value(collateral,p3,none).
value(hist,p4,unknown). value(debt,p4,low). value(collateral,p4,none).
value(hist,p5,unknown). value(debt,p5,low). value(collateral,p5,none).
value(hist,p6,unknown). value(debt,p6,low). value(collateral,p6,adequate).
value(historyK,p7,bad). value(debt,p7,low). value(collateral,p7,none).
value(historyK,p8,bad). value(debt,p8,low). value(collateral,p8,adequate).
value(historyK,p9,good). value(debt,p9,low). value(collateral,p9,none).
value(historyK,p10,good). value(debt,p10,high). value(collateral,p10,adequate).
value(historyK,p11,good). value(debt,p11,high). value(collateral,p11,none).
value(historyK,p12,good). value(debt,p12,high). value(collateral,p12,none).
value(historyK,p13,good). value(debt,p13,high). value(collateral,p13,none).
value(historyK,p14,bad). value(debt,p14,high). value(collateral,p14,none).

/* SAME VALUE */
sameValue(Att,[H|[]],Val):- value(Att,H,Val).
sameValue(Att,[A,B|T],Val):- value(Att,A,V1),value(Att,B,V2),V1=V2,sameValue(Att,[B|T],Val).

/* DIVIDE */
divide([H|[]],Att,Boolean,Pos,Neg):-value(Att,H,X),X=Boolean,Pos=[H],Neg=[].
divide([H|[]],Att,Boolean,Pos,Neg):-value(Att,H,X),not X=Boolean,Pos=[],Neg=[H].
divide([H|[]],Att,Boolean,Pos,Neg):-not value(Att,H,X),Pos=[],Neg=[].
divide([H|T],Att,Boolean,Pos,Neg):- not value(Att,H,X),divide(T,Att,Boolean,P,N), Pos=P,Neg=N.
divide([H|T],Att,Boolean,Pos,Neg):- value(Att,H,X), X=Boolean,divide(T,Att,Boolean,P,N), Pos=[H|P],Neg=N.
divide([H|T],Att,Boolean,Pos,Neg):- value(Att,H,X), not X=Boolean,divide(T,Att,Boolean,P,N),Pos=P, Neg=[H|N].

/* COUNT */
count([], Att, Bool, 0, 0).
count([H|Tail], Att, Bool, T, F) :- value(Att, H, X), X=Bool, count(Tail, Att, Bool, N, N2), T is N+1, F is N2.
count([H|Tail], Att, Bool, T, F) :- value(Att, H, X), not X=Bool, count(Tail, Att, Bool, N, N2), T is N, F is N2+1.
count([H|Tail], Att, Bool, T, F) :- count(Tail, Att, Bool, N, N2), T is N, F is N2.