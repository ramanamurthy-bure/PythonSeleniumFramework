import json
import os


def getglobaldata(data_name):
    # To get the test data file path
    str_testdata_dir = os.pardir + "\\testdata\\global_config.json"
    # Opening Json file
    # str_file = open(str_testdata_dir)
    with open(str_testdata_dir) as str_file:
        global_data = json.load(str_file)
        str_file.close()
    return global_data[data_name]
