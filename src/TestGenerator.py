import itertools
all_parts = set()
honest_leaders = ['A', 'B', 'C', 'D']
twins = ['X']
all_leaders = ['A', 'B', 'C', 'D', 'X']
def createPartitions(processes, pos, k, parts, st):
    global all_parts
    # print(k)

    if (pos == len(processes)-1):
        # if (k<=0):
        st.append(processes[pos])
        # print(f'Inserting {st}')
        parts.append(frozenset(st))
        # print(f'Parts is now {parts}')
        all_parts.add(frozenset(parts))
        # print(f'Global Set is now {all_parts}')
        parts.remove(frozenset(st))
        st.remove(processes[pos])
        return
    # if (k>0) and (pos == (len(processes)-1)):
        # return
    # if (k<0) or (pos > len(processes)-1):
        # return
    st.append(processes[pos])
    createPartitions(processes, pos+1, k, parts, st)
    parts.append(frozenset(st))
    createPartitions(processes, pos+1, k-1, parts, [])
    parts.remove(frozenset(st))
    st.remove(processes[pos])

def initializeNodes(honest_nodes, twin_nodes):
    global honest_leaders, twins, all_leaders
    honest_leaders = honest_nodes
    twins = twin_nodes
    all_leaders = honest_leaders + twins
    return

def createAllPartitions(honest_nodes, faulty_nodes):
    global all_parts, all_leaders
    permutations_object = itertools.permutations(all_leaders)
    permutations_list = list(permutations_object)
    for i,perm in enumerate(permutations_list):
        print(f'Creating partitions for {perm}')
        createPartitions(perm, 0, 1, [], [])
    return

def deterministic_select(no_of_parts, honest_nodes, twin_nodes, rnds):
    #select leader
    tests = []
    leaders = honest_nodes + twin_nodes
    i = 0
    for parts_set in all_parts:
        if (len(parts_set) == no_of_parts) and (i < len(honest_nodes+twin_nodes)*rnds):
            tests.append(list(parts_set)) #convert constituents to list too
            leaders.append(leaders[i])
            i = (i+1)%(len(leaders))
    #prune()
    return tests, leaders

def randomized_select(no_of_tests):
    leaders = []
    tests = []
    idx_set = set()
    all_parts_list = list(all_parts)
    seed(no_of_tests)
    while len(idx_set) < no_of_tests:
        idx = random()
        if idx not in idx_set:
            tests.append(all_parts_list[idx])
            leaders.append(all_leaders[(int)(idx%len(all_leaders))])
    return

def prune():
    pass

createAllPartitions(['A', 'B', 'C', 'D'], ['X'])
print(len(all_parts))