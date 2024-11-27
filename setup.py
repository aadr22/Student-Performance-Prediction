from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    This function reads the requirements file and returns a list of dependencies,
    excluding '-e .', which is handled by the setup script itself.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Clean up the requirements list
        requirements = [req.strip() for req in requirements if req.strip()]
        # Remove '-e .' as it is not a valid package specifier
        requirements = [req for req in requirements if req != "-e ."]

    return requirements

setup(
    name='mlproject',  # Name of your project
    version='0.0.1',  # Initial version
    author='Aadil',  # Your name
    author_email='aadil.rahman164@gmail.com',  # Your email
    packages=find_packages(),  # Automatically find all packages in the project
    install_requires=get_requirements('requirements.txt'),  # Dependencies
)
