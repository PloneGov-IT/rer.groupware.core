from setuptools import setup, find_packages
import os

version = '1.0.2'

setup(name='rer.groupware.core',
      version=version,
      description="rer.groupware.core",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='RedTurtle Technology',
      author_email='sviluppoplone@redturtle.net',
      url='',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['rer', 'rer.groupware'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Products.eXtremeManagement'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
