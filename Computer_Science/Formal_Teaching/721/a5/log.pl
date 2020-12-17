/*
Submission by:
Daniel Mezhibovski   500899282   Section 4
Calvin Mozola        500909122   Section 5
Cesar Argota         500882780   Section 6
*/

		%% LOGISTICS DOMAIN %%
/* Universal situations and fluents based planner  */
:- dynamic at/3.
/* This is necessary if rules with the same predicate in the head are not
   consecutive in your program.
*/ 

% We are looking for a list of actions represented by a variable Plan
% such that executing actions in Plan leads from the initial state 
% to a reachable state where a goal condition is true.

solve_problem(Bound,Plan)  :-  C0 is cputime,     % C0 is time when program starts %
          max_length(Plan,Bound),          % Bound is the maximal length of Plan   %
          reachable(S,Plan), 
	       goal_state(S),           % A situation S must be a solution of the problem %
          Cf is cputime, D is Cf - C0, nl,     % Cf is time when program finishes  %
          write('Elapsed time (sec): '), write(D), nl.

max_length([],N) :- N >= 0.
max_length([First | L],N1) :- N1 > 0, N is N1 - 1, max_length(L,N).

reachable(S,[]) :- initial_state(S).
/* This rule is for the regular part of the assignment */
reachable(S2, [M|List]) :- reachable(S1,List), legal_move(S2,M,S1).   

/* The following rule is for the bonus question only: remove comments
   and write your own rules to implement the predicate useless(M,List). 

reachable(S2, [M | ListOfActions]) :- reachable(S1,ListOfActions),
                    legal_move(S2,M,S1),
                    not useless(M,ListOfActions).
*/

legal_move([A|S], A, S) :- poss(A,S).
initial_state([]).

/*------------ Precondition Axioms------------------- */
	% write here your rules expressing when actions are possible

poss(load(B,V,L),S):- vehicle(V), at(B,_,[]), not vehicle(B), at(B,L,S), at(V,L,S), not loaded(B,S).
poss(unload(B,V,L),S):- vehicle(V), at(B,_,[]), not vehicle(B), in(B,V,S), at(V,L,S).
poss(drive(V,F,T,C),S):- truck(V), at(V,F,S), inCity(F,C), inCity(T, C), not F=T.
poss(fly(V,F,T),S):- airplane(V), airport(F), airport(T), at(V,F,S), inCity(F,C), inCity(T,C2), not C = C2.

/*----------- Successor State Axioms-------------- */
	% write here your rules expressing effects of actions 
in(B,V,[load(B,V,L)|S]).
in(B,V,[A|S]):- not A = unload(B,V,L), in(B,V,S).

loaded(B,[load(B,V,L)|S]).
loaded(B,[A|S]):- not A = unload(B,V,L), loaded(B,S).

at(X,Loc,[drive(X,L,Loc,C)|S]). 
at(X,Loc,[fly(X,L,Loc)|S]).
at(X,Loc,[unload(X,V,Loc)|S]).
at(X,Loc,[load(X,V,Loc)|S]).
at(X,Loc,S):- in(X,V,S), at(V,Loc,S).
at(X,Loc,[A|S]):-   not A = drive(X,L,Loc2,C),
                    not A = fly(X,L,Loc3),
                    not A = unload(X,V,Loc4), 
                    not A = load(X,V,Loc5),
                    not in(X,V,[A|S]), 
                    at(X,Loc,S).

 

:- [initLogistics].

/* This command loads the file  initLogistics.pl  with the initial and goal states.
  Keep it in the same folder as this file. Do not copy content here, because TA
  will test your program using another setting (with different trucks, airplanes)
*/


/* ----------------- Heuristics To Cut Search ------------------ */
	% BONUS: write here your rules implementing the predicate "useless" %

