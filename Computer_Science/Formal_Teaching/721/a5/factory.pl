/*
Submission by:
Daniel Mezhibovski   500899282   Section 4
Calvin Mozola        500909122   Section 5
Cesar Argota         500882780   Section 6
*/

/* Factory domain */

/* Universal situations and fluents based planner  */
:- dynamic free/2.
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

/* This rule is for the initial parts of the factory domain.
   Use it when you debug your precondition and other rules and
   when you test whether your program can solve easy planning problems. 
   Comment it out, when answering the last question about heuristics
   in the factory domain. Instead, use the other rule provided below.
*/
%reachable(S2, [M|List]) :- reachable(S1,List), legal_move(S2,M,S1).
 
/*The following rule uses declarative heuristics to cut search: remove comments
   and write your rules to implement the predicate useless(M,List) (see below).
   You use this only when answering the last question in the factory domain,
   for solving a planning problem that requires 7 steps.
*/
reachable(S2, [M | ListOfPastActions]) :- reachable(S1,ListOfPastActions),
                    legal_move(S2,M,S1),
                    not useless(M,ListOfPastActions).

legal_move([A|S], A, S) :- poss(A,S).
initial_state([]).


        	/* Precondition axioms */
% write your precondition rules here: you have to provide brief comments %
poss(drill(X),S):- free(X,[]),free(X,S).% the "free(X,[])" is used to ground the variable
%poss(shape(X),S).
poss(shape(X),S):- free(X,[]). % the "free(X,[])" is used to ground the variable
poss(bolt(X,Y),S):- drilled(X,S), drilled(Y,S), free(X,S), free(Y,S), not X = Y.
poss(paint(X,Col),S):- free(X,[]),free(X,S), available(Col). % the "free(X,[])" is used to ground the variables

        	/* Successor state axioms */
% write your successor state rules here: you have to include brief comments %
connected(X,Y,[bolt(X,Y)|S]).% base case
connected(X,Y,[bolt(Y,X)|S]).% base case
connected(X,Y,[A|S]):- not A = shape(X), not A = shape(Y),connected(X,Y,S).% recursive step

painted(X,C,[paint(X,C)|S]).% base case
painted(X,C,[A|S]):- not A = drill(X), not A = shape(X), not (A = paint(X,C2),not  C = C2) , painted(X,C,S).% recursive step

shaped(X,[shape(X)|S]).% base case
shaped(X,[A|S]):- shaped(X,S).% recursive step

free(X,[shape(X)|S]). % base case
free(X,[A|S]):- connected(X,Y,[S]), A=shape(Y).% base case when other part it is connected to is being shaped
free(X,[A|S]):- not A = shape(X), not A = bolt(X,Y), not A = bolt(Y,X), free(X,S). % recursive step
% The "not A = shape(X)" is here because objects start free in the initial
% state. This will stop recursion when a shaped is reached so if something is
% freed by shape then it will not continue and reach the inital case(this woudl 
% result in duplicates). In short "not A = shape(X)" this there to remove duplicates.

drilled(X,[drill(X)|S]).% base case
drilled(X,[A|S]):- not A = shape(X),drilled(X,S).% recursive step



		/* ---------- Heuristics To Cut Search ------------- */
% write your rules implementing the predicate  useless(Action,History) here. %

useless(paint(X,Col),S):- painted(X,Col,S).
useless(shape(X),S):-shaped(X,S).
useless(drill(X),S):- drilled(X,S).
useless(drill(X),S):- painted(X,C,S).
useless(shape(X),S):- painted(X,C,S).
useless(shape(X),S):- connected(X,Y,S).

:- [initFactory].
/* This last line compiles also the file initFactory.pl  that should be in same
   directory as this file. Do NOT insert this file here because your program 
   will be tested by a TA using different initial and goal states.      */