Act = [unload(bigBox1, gmc, stJohnAirport), load(bigBox1, gmc, memorialUnivNewfoundland), drive(gmc, stJohnAirport, memorialUnivNewfoundland, stJohn)]


at(gmc, X , [load(bigBox1, gmc, memorialUnivNewfoundland), drive(gmc, stJohnAirport, memorialUnivNewfoundland, stJohn)] ).


[drive(gmc, memorialUnivNewfoundland, stJohnAirport, stJohn), drive(gmc, memorialUnivNewfoundland, memorialUnivNewfoundland, stJohn), drive(gmc, stJohnAirport, memorialUnivNewfoundland, stJohn)]

poss(X,[drive(gmc, stJohnAirport, memorialUnivNewfoundland, stJohn)]).
poss(load(bigBox1,gmc,memorialUnivNewfoundland),[drive(gmc, stJohnAirport, memorialUnivNewfoundland, stJohn)]).



 at(B, L, [drive(gmc, stJohnAirport, memorialUnivNewfoundland, stJohn)]), not vehicle(B).
 at(bigBox1, L, [drive(gmc, stJohnAirport, memorialUnivNewfoundland, stJohn)]).


at(X,Loc,[drive(X,_,Loc,_)|S]).
at(X,Loc,[fly(X,_,Loc)|S]).
at(X,Loc,S):- in(X,V,S), vehicle(V), at(V,L,S).
at(X,Loc,[unload(X,_,Loc)|S]).
at(X,Loc,[A|S]):- not A = drive(X,Loc,_,_), not ( in(X,V,S), A = drive(V,Loc,_,_) ), at(X,Loc,S).


