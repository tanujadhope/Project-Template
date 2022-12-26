from setuptools import setup
with open("README.md",'r',encoding="utf-8") as f:
    long_description = f.read()

SOURCE_REPO="Mlproject"
AUTHOR_USER_NAME=  "tanujadhope"  
REPO_NAME="Project-Template"
LIST_OF_REQUIREMENTS =[]

setup(name = SOURCE_REPO,
version = "0.0.1",
author = AUTHOR_USER_NAME,
descrpition ="This is the release of first Version",
long_description = long_description,
url =f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
author_mailid=tanuja_dhope@yahoo.com,
packages=[SOURCE_REPO],
python_requires=">3.6",
install_requires=LIST_OF_REQUIREMENTS
)

