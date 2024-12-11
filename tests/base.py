import os

import pytest
import json


@pytest.mark.usefixtures("setup")
class Base:
    pass

    @staticmethod
    def config_data():
        try:
            # Dynamically construct the file path
            file_path = os.path.join(os.getcwd(), "testdata.json")
            print("current directory",os.getcwd())
            print(file_path)
            with open(file_path, 'r') as file:
                    return json.load(file)
        except FileNotFoundError as e:
            print(f"Configuration file not found: \n{e}")
            return {}


# /home/shubham/Shubham_QA/Projects/caseStudy/testdata.json