from setuptools import setup, find_packages

setup(
  name = "zhihubackup",
  packages=find_packages(),
  version = '0.0.2',
  install_requires = ['requests', 'tqdm']
)
