/*
Submission by:
Calvin Mozola           500909122       Section 5
Cesar Perez             500882780       Section 6
Daniel Mezhibovski      500899282       Section 4
*/

/* MINIM */
minim([H|T],Min):- T=[], Min=H.
minim([A,B|T],Min):- A < B , minim([A|T],Min). 
minim([A,B|T],Min):- not A < B , minim([B|T],Min).

/* POL ADD */
polAdd([H1|[]],[H2|[]],Sum):- N is H1+H2, Sum=[N].
polAdd([H1|T1],[H2|T2],Sum):- N is H1+H2, polAdd(T1,T2,OtherSum), Sum=[N|OtherSum].

/* CONST MULT */
constMult([H|[]],C,Result):- N is H*C,Result=[N].
constMult([H|T],C,Result):- N is H*C,constMult(T,C,OtherResult),Result = [N|OtherResult].

/* POL MULT */
polMult(A,B,Output):- mypolMult(A,B,[],[],Output).
mypolMult(A, [], S, X,Output):- Output = X.
mypolMult(A,[H|T],S,X,Output):- constMult(A,H,Scaled),
	append(S,Scaled,Product),
	normalize(Product,X,NorPro,NorX),
	polAdd(NorPro,NorX,NewX),
	append(S,[0],NewS),
	mypolMult(A,T,NewS,NewX,Output).