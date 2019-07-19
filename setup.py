
from distutils.core import setup

setup(name='networkmonitor',
    version='0.0.1',
    description='Console application to let you monitor the status of devices.', 
    author='James Tombleson',
    url='http://github.com/luther38/networkmonitor',   
    packages=[
        'requests',
        'click'
    ],
    entry_points='''
        [console_scripts]
        networkmonitor=networkmonitor:init
    '''
)