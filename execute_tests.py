import json
import os
import sys


result_dir = "test_results/"

json_file = open("data/input.json",mode='r')

data = json.load(json_file)

data[0]['cmd'] = data[0]['cmd'].replace('{input}', data[0]["inputs"][0])

print(data[0]['cmd'])



if __name__ == '__main__':

    json_filename = sys.argv[1]
    print("Processing test set: {}".format(json_filename))
    json_file = open(json_filename, 'r')

    test_set = json.load(json_file)

    for test in test_set:
        test_name = test['name']
        test_cmd = "test_scripts/" + test['cmd']
        test_inputs = test['inputs']
        test_output_dir = test['output_dir']
        test_result_dir = os.path.join(result_dir, test_name)

        # Create directory to store the results of the test
        if os.path.exists(test_output_dir):
            os.rmdir(test_output_dir)
        os.mkdir(test_output_dir)

        # Create the temporal output directory of the test
        if os.path.exists(test_output_dir):
            os.rmdir(test_output_dir)
        os.mkdir(test_output_dir)

        # Process the inputs
        for input in test_inputs:
            cmd = test_cmd.replace('{input}', input)
            os.system(cmd)

        # Move the results to the result directory and remove the temporal directory
        os.system("mv {output_dir}/* {test_output_dir}".format(output_dir=test_output_dir, test_result_dir=test_result_dir ))
        os.rmdir(test_output_dir)
