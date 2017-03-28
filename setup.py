#
# Copyright 2016 DGraph Labs, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.version_info >= (2, 7, 9):
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context

from pydgraph.utils.meta import VERSION

setup(name="pydgraph",
      version=VERSION,
      description="Dgraph driver for Python",
      license="Apache License, Version 2.0",
      author="Mohit Ranka",
      author_email="mohitranka@gmail.com",
      url="https://github.com/dgraph-io/pydgraph",
      classifiers=[
          "Intended Audience :: Developers",
          "License :: OSI Approved :: Apache Software License",
          "Operating System :: OS Independent",
          "Topic :: Database",
          "Topic :: Software Development",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3.3",
          "Programming Language :: Python :: 3.4",
      ],
      packages=["pydgraph", "pydgraph.utils"],
      install_requires=open('requirements.txt').readlines(),
      test_suite='tests',
      )
