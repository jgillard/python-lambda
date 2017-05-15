#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pip

from setuptools import setup, find_packages

requirements = pip.req.parse_requirements(
    "requirements.txt", session=pip.download.PipSession()
)
pip_requirements = [str(r.req) for r in requirements]


setup(
    name='depop-python-lambda',
    version='0.1.0',
    packages=find_packages(),
    package_data={
        'aws_lambda': ['project_templates/*', 'project_templates/tests/*'],
        '': ['*.json'],
    },
    include_package_data=True,
    scripts=['scripts/lambda'],
    install_requires=pip_requirements,
)
