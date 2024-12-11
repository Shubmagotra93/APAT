import os

import pytest
import json


@pytest.mark.usefixtures("setup")
class Base:
    pass

    @staticmethod
    def config_data():
        try:
            # file_path = os.path.join(os.getcwd(), "testdata.json")
            with open("/home/shubham/PycharmProjects/caseStudy/testdata.json", 'r') as file:
                return json.load(file)
        except FileNotFoundError as e:
            print(f"Configuration file not found: {e}")
            return {}





