import TestGenerator
import TestExecutor

def main():
    nodes = ['A', 'B', 'C', 'D']
    target_nodes = ['X']

    TestGenerator.initialize(['A', 'B', 'C', 'D'], ['X'])
    TestGenerator.createAllPartitions()
    TestGenerator.select_test_configurations([2, 3], 10, True, 10, True, 7)

    te = new(TestExecutor.TestExecutor, num=1)
    setup(te, nodes, target_nodes)
    start(te)
    return