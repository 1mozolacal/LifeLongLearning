class Machine:
    def __init__(self,val,child):
        self.fun = val
        self.used = False
        self.child = child if child != -1 else None
        self.parents = []
        
    def add_as_parent(self,machine_dict):
        if self.child is None:
            return
        machine_dict[self.child].add_parent(self)
    
    def add_parent(self,parent):
        self.parents.append(parent)
        
    def get_cur_val(self):
        if self.used:
            return 0
        return self.fun

    def get_low_max(self):
        if len(self.parents) == 0:
            if self.used:
                return None
            return self.fun
        par_max = [x.get_low_max() for x in self.parents if not x.get_low_max() is None]
        if len(par_max) == 0:
            return None
        p_max = max(par_max)
        return max(p_max,self.get_cur_val())

def best_route(void):

    for v in void:
        # print('void')
        ret = recur_best(v,0)
        # print(f'got {ret} {not ret is None}')
        if not ret is None:
            return ret
    return None
    
def recur_best(current,base):
    # print(f"{current.fun} - {base}")
    
    if len(current.parents) == 0:
        if current.used:
            return None
        m=  max(current.get_cur_val(), base)
        current.used = True
        return m
    
    if len(current.parents) == 1:
        m = max(base,current.get_cur_val())
        current.used = True
        return recur_best(current.parents[0],m)
    
    next_dirction = None
    lowest_max = None
    for par in current.parents:
        par_max = par.get_low_max()
        if par_max is None:
            continue
        if lowest_max is None or par_max < lowest_max:
            next_dirction = par
            lowest_max = par_max
    
    if next_dirction is None:
        return None
    m =max(base,current.get_cur_val())
    current.used = True
    return recur_best(next_dirction, m)

    
    # ava_par = [x for x in machines[current].parents if not x.used]
    # if len(ava_par) == 0:
    #     return None
    # elif len(ava_par) < 2:
    #     new_base = max(base, machines[current].get_cur_val())
    #     recur_best(current,machines,new_base)
    
    #check lowest
    
    

for test in range(int(input())):
    amount = int(input())
    fun_vals = [int(x) for x in input().split(' ')]
    connection_vals = [int(x)-1 for x in input().split(' ')]
    
    void_pointers = []
    
    machines = {}
    for mach_index in range(amount):
        new_mach = Machine(fun_vals[mach_index],connection_vals[mach_index])
        machines[mach_index] = new_mach
        if connection_vals[mach_index] == -1:
            void_pointers.append(new_mach)
        
    for _i,mach in machines.items():
        mach.add_as_parent(machines)
        
    score = 0
    while True:
        curr_route = best_route(void_pointers)
        if curr_route is None:
            break
        score += curr_route
    print(f'Case #{test+1}: {score}')
    