from distutils.core import setup
from setuptools import find_packages

# 这是一个和根目录相关的安装文件的列表，列表中setup.py更具体)

files = ["things/*"]

setup(name="nnl",
      version="0.1",
      description="hello",
      author="oybb",
      author_email="emailboxbeta@gmail.com",
      #url="whatever",
      # Name the folder where your packages live:
      # (If you have other packages (dirs) or modules (py files) then
      # put them into the package directory - they will be found recursively.)
      packages=find_packages("src"),
      package_dir={"": "src"},
      # 'package' package must contain files (see list above)
      # I called the package 'package' thus cleverly confusing the whole issue...
      # This dict maps the package name =to=> directories
      # It says, package *needs* these files.
#
# This next part it for the Cheese Shop, look a little down the page.
# classifiers = []

      )