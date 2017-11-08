from setuptools import setup, find_packages

setup(
    name='gitkeep',
    version='0.0.1',
    description='Add .gitkeep file to empty folders.',
    url='https://github.com/Frederick-S/gitkeep',
    packages=find_packages(exclude=['tests']),
    entry_points={
        'console_scripts': [
            'gitkeep = gitkeep.main:main'
        ]
    },
    include_package_data=True,
    test_suite="tests"
)
