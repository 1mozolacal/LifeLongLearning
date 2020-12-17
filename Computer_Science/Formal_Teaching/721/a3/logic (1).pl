floor(1). floor(2). floor(3). floor(4). floor(5). floor(6). floor(7). floor(8). floor(9). floor(10). 
floor(11). floor(12). floor(13). floor(14). floor(15). floor(16). floor(17). floor(18). floor(19). floor(20). 

print_solution([Peter, Romeo, Sam, Tom, Accountant, Businessman, ComputerS, Dentist]) :-
    solve1([Peter, Romeo, Sam, Tom, Accountant, Businessman, ComputerS, Dentist]),

    write("Peter lives on floor "), write(Peter),
    write("\nRomeo lives on floor "), write(Romeo),
    write("\nSam lives on floor "), write(Sam),
    write("\nTom lives on floor "), write(Tom),

    write("\nThe accountant lives on floor "), write(Accountant),
    write("\nThe businessman lives on floor "), write(Businessman),
    write("\nThe computer scientist lives on floor "), write(ComputerS),
    write("\nThe dentist lives on floor "), write(Dentist).

solve1([Peter, Romeo, Sam, Tom, Accountant, Businessman, ComputerS, Dentist]) :-
    floor(ComputerS), Tom is ComputerS*5, floor(Tom),

    ComputerS>3,

    floor(Sam), floor(Peter), Peter > Sam, Peter < Tom,

    floor(Romeo), floor(Dentist), Romeo < Dentist,

    N2 is Dentist-3, Peter=N2,

    floor(Accountant), Middle is (Accountant+Dentist)//2, floor(Businessman), N3 is Businessman-2, N3=Middle,

    Peter=Businessman,

    Dentist is Sam*2,

    Twice is Romeo*2, N5 is Accountant-2, Twice=N5,

    Dentist >= Tom.

solve2([Peter, Romeo, Sam, Tom, Accountant, Businessman, ComputerS, Dentist]) :-
    floor(Peter), floor(Romeo), floor(Sam), floor(Tom),
    floor(Accountant), floor(Businessman), floor(ComputerS), floor(Dentist),

    Tom=ComputerS*5,

    ComputerS>3,

    Peter > Sam, Peter < Tom,

    Romeo < Dentist,

    N2 is Dentist-3, Peter=N2,

    Middle is (Accountant+Dentist)//2, N3 is Businessman-2, N3=Middle,

    Peter=Businessman,

    Dentist is Sam*2,

    Twice is Romeo*2, N5 is Accountant-2, Twice=N5,

    Dentist >= Tom.