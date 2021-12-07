#! /usr/bin/python

from pathlib import Path
# import TestGenerator
# import TestExecutor


if __name__ == '__main__':
    config_folder = Path("./config")
    fname = 'twinsConfig.csv'
    path = config_folder / fname
    with open(path, 'r') as file:
        generator_config = {}
        for line in file:
            arguments = line.split('=')
            # print(arguments)
            key = arguments[0].strip()

            if key == 'nodes':
                nodes = arguments[1].split(',')
                nodes = [node.strip() for node in nodes]
                generator_config['nodes'] = nodes
            elif key == 'target_nodes':
                target_nodes = arguments[1].split(',')
                target_nodes = [node.strip() for node in target_nodes]
                generator_config['target_nodes'] = target_nodes
            elif key == 'no_of_parts':
                no_of_parts = arguments[1].split(',')
                no_of_parts = [int(part.strip()) for part in no_of_parts]
                generator_config['no_of_parts'] = no_of_parts
            elif key == 'num_partitions':
                num_partitions = int(arguments[1].strip())
                generator_config['num_partitions'] = num_partitions
            elif key == 'is_partition_random':
                is_partition_random = arguments[1].strip() == 'True'
                generator_config['is_partition_random'] = is_partition_random
            elif key == 'num_leaders_req':
                num_leaders_req = int(arguments[1].strip())
                generator_config['num_leaders_req'] = num_leaders_req
            elif key == 'is_leader_random':
                is_leader_random = arguments[1].strip() == 'True'
                generator_config['is_leader_random'] = is_leader_random
            elif key == 'rounds':
                rounds = int(arguments[1].strip())
                generator_config['rounds'] = rounds

    #
    # TestGenerator.initialize(['A', 'B', 'C', 'D'], ['X'])
    # TestGenerator.createAllPartitions()
    # TestGenerator.select_test_configurations([2, 3], 10, True, 10, True, 7)
    #
    # te = new(TestExecutor.TestExecutor, num=1)
    # setup(te, nodes, target_nodes)
    # start(te)
    # return