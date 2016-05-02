#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name = 'readgroup_json_db',
      author = 'Jeremiah H. Savage',
      author_email = 'jeremiahsavage@gmail.com',
      version = 0.7,
      description = 'read readgroup data as json and store in sqlitedb',
      url = 'https://github.com/jeremiahsavage/readgroup_json_db',
      license = 'Apache 2.0',
      packages = find_packages(),
      install_requires = [
          'pandas',
          'sqlalchemy',
          'cdis_pipe_utils'
      ],
      classifiers = [
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
      ],
)
