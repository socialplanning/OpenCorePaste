from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='OpenCorePaste',
      version=version,
      description="",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Ethan Jucovy',
      author_email='opencore-dev@lists.coactivate.org',
      url='',
      license='GPLv3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      [paste.paster_create_template]
      opencore_plugin = opencorepaste:OpenCorePlugin
      """,
      )
