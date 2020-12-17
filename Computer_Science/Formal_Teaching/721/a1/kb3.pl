income(will, 15).
income(john, 35).
income(jess, 35).
income(michael, 15).
income(may, 0).
income(donald, 15).

collateral(will,none).
collateral(john, none).
collateral(jess, none).
collateral(michael, none).
collateral(may, none).
collateral(donald, none).

debt(will,high).
debt(john, low).
debt(jess,low).
debt(logan, high).
debt(michael, low).
debt(may, high).
debt(donald, low).

history(will,good).
history(john,unknown).
history(jess,good).
history(logan,unknown).
history(michael,unknown).
history(may,bad).
history(donald, good).

risk(donald, high).
risk(may, high).
risk(michael, moderate).
risk(logan, high).
risk(jess, low).
risk(john, low).
risk(will,moderate).


calcCreditHistory(Person,Out) :- history(Person, Type), Type = bad,  calcBadCollateral(Person,Out).
calcCreditHistory(Person,Out) :- history(Person, Type), Type = unknown,   calcDebtUnknown(Person,Out).
caclCreditHistory(Person,Out) :- history(Person, Type), Type = good,   calcDebtGood(Person,Out). 

calcBadCollateral(Person, Out) :- collateral(Person, Coll), Coll = none, Out = high.
calcBadCollateral(Person, Out) :- collateral(Person, Coll), Coll = adequate, Out = moderate.

calcDebtUnknown(Person, Out):- debt(Person, Debt), Debt = high, Out = high.
calcDebtUnknown(Person, Out):- debt(Person, Debt), Debt = low, calcCollateral(Person,Out).

calcDebtGood(Person,Out) :- debt(Person,Level), Level = high, calcCollateral(Person,Out).
calcDebtGood(Person,Out) :- debt(Person,Level), Level = low, Out = low.

calcCollateral(Person,Out):- collateral(Person,Coll), Coll = None, calcIncome(Person, Out).
calcCollateral(Person,Out):- collateral(Person,Coll), Coll = adequate, Out = low.

calcIncome(Person,Out):- income(Person, Inc), Inc = 0, Out = high.
calcIncome(Person,Out):- income(Person, Inc), Inc = 15, Out = moderate.
calcIncome(Person,Out):- income(Person, Inc), Inc = 35, Out = low. 

calcIncomeTwo(Person,Out,Inc):- income(Person, Inc), Inc = 0, Out = high.
calcIncomeTwo(Person,Out,Inc):- income(Person, Inc), Inc = 15, Out = moderate.
calcIncomeTwo(Person,Out,Inc):- income(Person, Inc), Inc = 35, Out = low. 
