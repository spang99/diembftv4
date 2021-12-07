import itertools
import random

all_parts = set()
all_parts_list = []
honest_leaders = [] #= ['A', 'B', 'C', 'D']
twins = [] #= ['X']
all_leaders = [] #= ['A', 'B', 'C', 'D', 'X']

def set_to_list(partitions):
    ans = []
    for partition in partitions:
        temp = []
        for part in partition:
            temp.append(list(part))
        ans.append(temp)
    return ans

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

def createAllPartitions():
    global all_parts, all_leaders, all_parts_list
    permutations_object = itertools.permutations(all_leaders)
    permutations_list = list(permutations_object)
    for i,perm in enumerate(permutations_list):
        # print(f'Creating partitions for {perm}')
        createPartitions(perm, 0, 1, [], [])
    all_parts_list = set_to_list(all_parts)

    return

def initialize(honest_nodes, twin_nodes):
    global honest_leaders, twins, all_leaders
    honest_leaders = honest_nodes
    twins = twin_nodes
    all_leaders = honest_leaders + twins
    return

def get_twin(node):
    idx = all_leaders.index(node)
    if (idx >= len(twins)):
        return None
    return twins[idx]

# def deterministic_select(no_of_parts, honest_nodes, twin_nodes, rnds):
#     #select leader
#     tests = []
#     leaders = honest_nodes + twin_nodes
#     i = 0
#     for parts_set in all_parts:
#         if (len(parts_set) == no_of_parts) and (i < len(honest_nodes+twin_nodes)*rnds):
#             tests.append(list(parts_set)) #convert constituents to list too
#             leaders.append(leaders[i])
#             i = (i+1)%(len(leaders))
#     #prune()
#     return tests, leaders

# def randomized_select(no_of_tests):
#     leaders = []
#     tests = []
#     idx_set = set()
#     all_parts_list = list(all_parts)
#     seed(no_of_tests)
#     while len(idx_set) < no_of_tests:
#         idx = random()
#         if idx not in idx_set:
#             tests.append(all_parts_list[idx])
#             leaders.append(all_leaders[(int)(idx%len(all_leaders))])
#     return

def select_leaders(num_leaders_req, is_random):
    ret_leaders = [] #list of (list of) leaders
    if is_random is True:
        while len(ret_leaders) < num_leaders_req:
            temp = []
            idx = random.randint(0, len(all_leaders))
            temp.append(all_leaders[idx%len(all_leaders)])
            tw = get_twin(all_leaders[idx%len(all_leaders)])
            if tw is not None:
                temp.append(tw)
            if len(temp)>0:
                ret_leaders.append(temp)
    else:
        for i in range(0, num_leaders_req):
            temp = []
            #add leader and check for twin
            temp.append(honest_leaders[i%len(honest_leaders)])
            tw = get_twin(all_leaders[i%len(honest_leaders)])
            if tw is not None:
                temp.append(tw)
            if len(temp)>0:
                ret_leaders.append(temp)
    return ret_leaders

def select_partitions(no_of_parts, num_partitions, is_random):
    idx_set = set()
    tests = []
    if is_random is True:
        while (len(idx_set) < num_partitions):
            idx = random.randint(0, len(all_parts)-1)
            if idx not in idx_set:
                tests.append(all_parts_list[idx%len(all_parts_list)])
                idx_set.add(idx)
    else:
        for parts_set in all_parts:
            if len(parts_set) in no_of_parts:
                tests.append(list(parts_set))
    return tests

def select_test_configurations(no_of_parts, num_partitions, is_partition_random, num_leaders_req, is_leader_random, rounds):
    #select leader
    tests = [] #stores test configurations
    # nodes = all_leaders
    i = 0
    temp_tests = select_partitions(no_of_parts, num_partitions, is_partition_random)
    temp_leaders = select_leaders(num_leaders_req, is_leader_random)
    # print(temp_leaders)

    idx_set = set() # Keeps track of used numbers for rounds
    ret_leaders = [] # leader assignment for each round
    ret_tests = [] # test assignment for each round
    while len(ret_tests) < rounds-2:
        idx = random.randint(0, rounds)
        if idx not in idx_set:
            ret_tests.append(temp_tests[idx%len(temp_tests)])
            ret_leaders.append(temp_leaders[idx%len(temp_leaders)])
            idx_set.add(idx)

    # the last test cases should not result in timeouts
    half = int(len(honest_leaders)/2)

    ret_tests.append([honest_leaders[0:half], honest_leaders[half:]])
    ret_leaders.append([honest_leaders[len(twins)]])
    ret_tests.append([honest_leaders[0:half-1], honest_leaders[half-1:]])
    ret_leaders.append([honest_leaders[half+1]])

    f = open("test_cases.txt", 'w')
    f.write(str(ret_tests) + '\n' + str(ret_leaders))
    # f.write(str(ret_leaders) + '\n')
    f.close()
    return