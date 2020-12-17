
risk(donald, high).
history(donald, good).
debt(donald, low).
collateral(donald, none).
income(donald, 15_to_35).

risk(may, high).
history(may,bad).
debt(may, high).
collateral(may, none).
income(may, 0_to_15).

risk(michael, moderate).
history(michael,unknown).
debt(michael, low).
collateral(michael, none).
income(michael, 15_to_35).

risk(logan, high).
history(logan,unknown).
debt(logan, high).
collateral(May, none).
income(May, 15_to_35).

risk(jess, low).
history(jess,good).
debt(jess,low).
collateral(jess, none).
income(jess, over35).

risk(john, low).
history(john,unknown).
debt(john, low).
collateral(john, none).
income(john, over35).

risk(will,moderate).
history(will,good).
debt(will,high).
collateral(will,none).
income(will, 15_to_35).




calcRisk(person):- stuff.

calcCreditHistory(Person, Output):- history(Person, Credit), (Credit = unknown -> calcBadDebt(Person,Output); (Credit = bad -> calcCollateralBad(Person, Ouput); calcGoodDebt(Person, Output) ).
calcBadDebt(Person, Output):- debt(Person, Debt), (Debt = high -> Ouptut is high; calcRiskCollateral(Person,Ouput) ).
calcGoodDebt(Person, Output):- debt(Person, Debt), (Debt = low -> Output is low; calcRiskCollateral(Person,Output) ).
calcCollateralBad(Person, Output):- collateral(Person,Coll), (Coll = none -> Output is high; calcRiskCollaterl(Person,Output) ).
calcRiskCollateral(Person, Output):- collateral(Person,Coll), (Coll = adequate -> Ouput is low; calcIncome(Person,Output) ).
calcIncome(Person,Output):- income(Person,Inc), (Inc = 0_to_15 -> Ouput is high; (Inc = 15_to_35 -> Output is moderate; Output is low) ).
