from typing import List
from setuptools import setup,find_packages
from typing import List

#declaring variables for setup functions
PROJECT_NAME="Housing-Predictor"
VERSION="0.0.1"
AUTHOR="Reshali"
DESCRIPTION="This is the first FSDS nov batch machine learning project"
'''PACKAGES=["housing"]'''
REQUIREMENTS_FILE_NAME="requirements.txt"


def get_requirements_list()->List[str]:
    '''
    Description:This function is going to return list of requiremt mention
    in the requirements.txt file

    return:This function is going to return a list 
    which contains name of libraries mentioned in requirements.txt file
    '''
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")



setup(name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(),#["housing"]
install_requires=get_requirements_list())

if __name__=="__main__":
    print(get_requirements_list())