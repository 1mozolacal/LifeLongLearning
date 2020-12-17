removeEle([H|T],X,Left,Out):- H=X, append(Left,T,Out).
removeEle([H|T],X,Left,Out):- append(Left,[H],NewLeft),removeEle(T,X,NewLeft,Out).

permutation([],[]).
permutation(Bank,[H|T]):- removeEle(Bank,H,[],NewBank), isPerm(NewBank,T).

myIntersection(A,B,Out):- myInterHelper(A,B,[],Out).
myInterHelper([],X,Acc,Out):- isPerm(Acc,Out).
myInterHelper([H|T],B,Acc,Out):- member(H,B), not member(H,Acc), myInterHelper(T,B,[H|Acc],Out).
myInterHelper([H|T],B,Acc,Out):- not member(H,B), myInterHelper(T,B,Acc,Out).

myUnion(L1,L2,L3):- myUnionHelp(L1,L2,[],Out),isPerm(Out,L3).
myUnionHelp([],[],R,Out):- Out=R.
myUnionHelp([],[H|T],R,Out):- not member(H,R), myUnionHelp([],T,[H|R],Out).
myUnionHelp([],[H|T],R,Out):- member(H,R), myUnionHelp([],T,R,Out).
myUnionHelp([H|T],L,R,Out):- member(H,L),myUnionHelp(T,L,R,Out).
myUnionHelp([H|T],L,R,Out):- member(H,R),myUnionHelp(T,L,R,Out).
myUnionHelp([H|T],L,R,Out):- not member(H,L),not member(H,R),myUnionHelp(T,L,[H|R],Out).

