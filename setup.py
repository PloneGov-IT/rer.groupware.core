from setuptools import setup, find_packages
import os

version = '2.0.0.dev0'

setup(name='rer.groupware.core',
      version=version,
      description="rer.groupware.core",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Plone",
        "Framework :: Plone :: 4.2",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='RedTurtle Technology',
      author_email='sviluppoplone@redturtle.it',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['rer', 'rer.groupware'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.discussion',
          'Products.Ploneboard',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
