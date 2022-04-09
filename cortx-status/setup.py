#!/bin/env python3

import os
import glob
from setuptools import setup

def get_version() ->str:
    """ returns version string """
    return "2.0.0"

def get_install_requirements() -> list:
    """ Returns pre-requisite """

    with open('requirements.txt') as req:
        install_requires = [line.strip() for line in req]
    return install_requires

def get_db_files() -> list:
    """Returns db files."""
    return glob.glob('src/db/*.json')

setup(name='cortx-status',
    version=get_version(),
    package_dir={'cortx':'src'},
    packages=['cortx.status', 'cortx.db'],
    package_data={
        'cortx': ['py.typed']
    },
    entry_points={
        'console_scripts': ['cortx_status = cortx.status.cortx_status:main', 'upgrade_status = cortx.status.upgrade_status:main'
        ]
    },
    data_files=[
        ('/opt/seagate/cortx/status/db/', get_db_files()),
        ('/opt/seagate/cortx/status', ['requirements.txt'])
],
    zip_safe=False,
    python_requires='>=3.6',
    install_requires=get_install_requirements()
)
    
