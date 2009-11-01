from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='OpenCorePaste',
      version=version,
      description="pastescript template for opencore plugin authors",
      long_description="`paster create -t opencore_plugin`",
      classifiers=[], 
      keywords='',
      author='Ethan Jucovy',
      author_email='opencore-dev@lists.coactivate.org',
      url='',
      license='GPLv3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'PasteScript',
      ],
      entry_points="""
      [paste.paster_create_template]
      opencore_plugin = opencorepaste:OpenCorePlugin
      """,
      )
