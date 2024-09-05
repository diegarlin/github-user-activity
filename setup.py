import setuptools
from distutils.core import setup

setup(
    name='github-activity',
    version='0.1',
    description='A simple github activity program',
    author='diegarlin',
    author_emails='garcialinaresdiego@gmail.com',
    packages=['github_activity'],
    entry_points={
        'console_scripts': ['github-activity=github_activity.entry:cli_entry_point'],    
    },
    install_requires=[
        'requests',
    ],
)