isaLink(mammal,animal).
isaLink(reptile,animal).
isaLink(bird,animal).
isaLink(fish,animal).
isaLink(whale,mammal).
isaLink(dog,mammal).
isaLink(cat,mammal).
isaLink(retriever,dog).
isaLink(golden_retriever,retriever).
isaLink(poodle,dog).
isaLink(tabby,cat).
isaLink(canary,bird).
isaLink(penguin,bird).
isaLink(chicken,bird).
isaLink(robin,canary).
isaLink(emperor_penguin,penguin).
isaLink(shark,fish).

leaf(Child):- isaLink(Child,Parent), not isaLink(X,Child).
sibling(X,Y) :- isaLink(X,A), isaLink(Y,A),not X=Y.
grandParent(X,Y) :- isaLink(X,A), isaLink(A,Y).
isa(X,Y):- X=Y.
isa(X,Y):- isaLink(X,P),isa(P,Y).
mostSpecifiedSubsumer(X,Y,Z) :- isa(X,Z), isa(Y,Z).
