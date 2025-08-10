from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT='-e .'

# since ip is in the form of path it is str and since it returns the list we have imported the list
def get_requirements(file_path:str)->list[str]:
    '''

    this function will return the list of requirements

    '''

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        # since readline adds the nextline char at end of each line so hence we replace func
        requirements=[req.replace("\n","")for req in requirements]
        # to prevent the reading of -e.
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        return requirements

setup(
    name="mlproject",
    version='0.0.1',
    author='vaishali',
    author_email='vaishalimamidi10@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)