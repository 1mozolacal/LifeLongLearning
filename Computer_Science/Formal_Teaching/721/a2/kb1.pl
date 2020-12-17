minim([H|[]],Min):- Min=H.
minim([A,B|T],Min):- A < B , minim([A|T],Min). 
minim([A,B|T],Min):- not A < B , minim([B|T],Min).

polAdd([H1|[]],[H2|[]],Sum):- N is H1+H2, Sum=[N].
polAdd([H1|T1],[H2|T2],Sum):- N is H1+H2, polAdd(T1,T2,OtherSum), Sum=[N|OtherSum].

constMult([H|[]],C,Result):- N is H*C,Result=[N].
constMult([H|T],C,Result):- N is H*C,constMult(T,C,OtherResult),Result = [N|OtherResult].

normalize([],[],ResA,ResB):- ResA=[],ResB=[].
normalize([],[HB|TB],ResA,ResB):- normalize([],TB,RestOfA,RestOfB), ResA=[0|RestOfA],ResB=[HB|RestOfB].
normalize([HA|TA],[],ResA,ResB):- normalize(TA,[],RestOfA,RestOfB), ResA=[HA|RestOfA],ResB=[0|RestOfB].
normalize([HA|TA],[HB|TB],ResA,ResB):- normalize(TA,TB,RestOfA,RestOfB), ResA=[HA|RestOfA],ResB=[HB|RestOfB].

test(A,B,C):- B = C. 

polMult(A,B,Output):- mypolMult(A,B,[],[],Output).
mypolMult(A, [], S, X,Output):- Output = X.
mypolMult(A,[H|T],S,X,Output):- constMult(A,H,Scaled),
	append(S,Scaled,Product),
	normalize(Product,X,NorPro,NorX),
	polAdd(NorPro,NorX,NewX),
	append(S,[0],NewS),
	mypolMult(A,T,NewS,NewX,Output).


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


sameValue(Att,[H|[]],Val):- value(Att,H,Val).
sameValue(Att,[A,B|T],Val):- value(Att,A,V1),value(Att,B,V2),V1=V2,sameValue(Att,[B|T],Val).

divide([H|[]],Att,Boolean,Pos,Neg):-value(Att,H,X),X=Boolean,Pos=[H],Neg=[].
divide([H|[]],Att,Boolean,Pos,Neg):-value(Att,H,X),not X=Boolean,Pos=[],Neg=[H].
divide([H|[]],Att,Boolean,Pos,Neg):-not value(Att,H,X),Pos=[],Neg=[].
divide([H|T],Att,Boolean,Pos,Neg):- not value(Att,H,X),divide(T,Att,Boolean,P,N), Pos=P,Neg=N.
divide([H|T],Att,Boolean,Pos,Neg):- value(Att,H,X), X=Boolean,divide(T,Att,Boolean,P,N), Pos=[H|P],Neg=N.
divide([H|T],Att,Boolean,Pos,Neg):- value(Att,H,X), not X=Boolean,divide(T,Att,Boolean,P,N),Pos=P, Neg=[H|N].





