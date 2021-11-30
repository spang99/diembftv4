

import TestGenerator
import TestExecutor

def main():
    TestGenerator.initialize(['A', 'B', 'C', 'D'], ['X'])
    TestGenerator.createAllPartitions()
    TestGenerator.select_test_configurations([2, 3], 10, True, 10, True, 7)
    return