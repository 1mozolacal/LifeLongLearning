
taken([mon,12,r1]). taken([mon,1,r1]). taken([mon,1,r4]). taken([mon,2,r4]). 
taken([tues,9,r2]). taken([tues,10,r2]). taken([tues,3,r1]). taken([tues,4,r1]).
taken([wed,10,r3]). taken([wed,11,r3]). taken([wed,12,r3]). taken([wed,1,r3]).
taken([thurs,12,r4]). taken([thurs,1,r4]). taken([fri,3,r1]). taken([fri,4,r1]).

two_consecutive_hours( [D,T1,R], [D,T2,R] ):- T2 is T1 + 1.
dame_day([ [D,T1,R1], [D,T2,R2] ]).

day_time_member( [D,T,R1], [ [D,T,R2] | T]).
day_time_member( Class , [H | T] ):- day_time_member( Class, T).

prof_conflict([H | T],List):- day_time_member(H,List).
prof_conflict([H | T],List):- prof_conflict(T,List).

/*
available(List):- not taken[], checkNewClass(List).
*/

/* note we need to make out own member */
class_time( [Day,Hour,Room] ):-
	member(Day, [mon,tue,wed,thu,fri] ),
	member(Hour, [9,10,11,12,1,2,3,4] ),
	member(Room, [r1,r2,r3,r4] ).

print_solution( [AI1,AI2,AI3,AI4,OS1,OS2,OS3,WD1,WD2,WD3,DS1,DS2,DS3,AL1,AL2,AL3,NE1,NE2] ):-
	class_time(AI1),class_time(AI2),
	two_consecutive_hours(AI1,AI2),
	class_time(AI3),class_time(AI4),
	two_consecutive_hours(AI3,AI4),
	not same_day(AI1,AI3),
	available([AI1,AI2,AI3,AI4]),

	class_time(OS1),class_time(OS2),
	two_consecutive_hours(OS1,OS2),
	class_time(OS3),
	not same_day(OS1,OS3),
	available([OS1,OS2,OS3]),

	not conflict([AI1,AI2,AI3,AI4],[OS1,OS2,OS3]),

	class_time(NE1),
	class_time(NE2),
	not same_day(NE1,NE2),
	available([NE1,NE2,NE3]),
	
	not conflict([AI1,AI2,AI3,AI4,OS1,OS2,OS3],[NE1,NE2,NE3]),
	not prof_conflict( [OS1,OS2,OS3], [NE1,NE2,NE3] ),
	
	class_time(WD1),class_time(WD2),
	two_consecutive_hours(WD1,WD2),
	class_time(WD3),
	two_consecutive_hours(WD2,WD3),
	available(WD1,WD2,WD3),

	not conflict([AI1,AI2,AI3,AI4,OS1,OS2,OS3,NE1,NE2,NE3],[WD1,WD2,WD3]),

	class_time(DS1),class_time(DS2),
	two_consecutive_hours(DS1,DS2),
	class_time(DS3),
	not same_day(DS1,DS3),
	available(DS1,DS2,DS3),

	not conflict([AI1,AI2,AI3,AI4,OS1,OS2,OS3,NE1,NE2,NE3,WD1,WD2,WD3],[DS1,DS2,DS3]),

	class_time(AL1),class_time(AL2),
	two_consecutive_hours(AL1,AL2),
	class_time(AL3),
	not same_day(AL1,AL3),
	available(AL1,AL2,AL3),

	not conflict([AI1,AI2,AI3,AI4,OS1,OS2,OS3,NE1,NE2,NE3,WD1,WD2,WD3,DS1,DS2,DS3],[AL1,AL2,AL3]),
	not prof_conflict( [DS1,DS2,DS3], [AL1,AL2,AL3] ).

	
	
	