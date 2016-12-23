# ----------------------------------------------------------------------------
# Copyright (c) 2016-2017, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from setuptools import setup, find_packages

setup(
    name="q2templates",
    version='2017.2.0.dev0',
    license='BSD-3-Clause',
    url='https://qiime2.org',
    packages=find_packages(exclude=['tests']),
    package_data={
        'q2templates': [
            'templates/*.html',
            'templates/assets/css/*.css',
            'templates/assets/img/*.png',
            'templates/assets/fonts/glyphicons-*'
        ]
    },
    install_requires=['jinja2']
)
