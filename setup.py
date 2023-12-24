try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

import ramen

def get_requirements(requirements_path='requirements.txt'):
    with open(requirements_path) as fp:
        return [x.strip() for x in fp.read().split('\n') if not x.startswith('#')]

get_requirements()

setup(
    name='ramen',
    version=ramen.__version__,
    description='Term2 library',
    author='Mikel',
    packages=find_packages(where='', exclude=['tests']),
    install_requires=get_requirements(),
    setup_requires=['pytest-runner', 'wheel'],
    url='https://github.com/mgallon235/term2.git',
    classifiers=[
        'Programming Language :: Python >= 3.7.16'
    ]
)
