# setup.py
import re
from sys import argv
from setuptools import setup, find_packages

# Import your compilers if necessary
from compiler.api import compiler as api_compiler
from compiler.errors import compiler as errors_compiler

# Read the requirements from requirements.txt
with open("requirements.txt", encoding="utf-8") as r:
    requires = [i.strip() for i in r]

# Extract the version number from the package __init__.py file
with open("MYPyrogram/__init__.py", encoding="utf-8") as f:
    version = re.findall(r'__version__ = "(.+)"', f.read())[0]

# Read the long description from README.md
with open("README.md", encoding="utf-8") as f:
    readme = f.read()

# Compile if specific commands are passed
if len(argv) > 1 and argv[1] in ["bdist_wheel", "install", "develop"]:
    api_compiler.start()
    errors_compiler.start()

# Setup configuration
setup(
    name="MYPyrogram",  # Updated package name
    version=version,
    description="Elegant, modern and asynchronous Telegram MTProto API framework in Python for users and bots",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/MYPyrogram",  # Update to your repo URL
    download_url="https://github.com/yourusername/MYPyrogram/releases/latest",  # Update to your repo URL
    author="Your Name",  # Update with your name
    author_email="your.email@example.com",  # Update with your email
    license="LGPLv3",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet",
        "Topic :: Communications",
        "Topic :: Communications :: Chat",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries :: Application Frameworks"
    ],
    keywords="telegram chat messenger mtproto api client library python",
    project_urls={
        "Tracker": "https://github.com/yourusername/MYPyrogram/issues",  # Update to your repo URL
        "Community": "https://t.me/MYPyrogram",  # Update to your community link
        "Source": "https://github.com/yourusername/MYPyrogram",  # Update to your repo URL
        "Documentation": "https://docs.MYPyrogram.org",  # Update to your documentation URL
    },
    python_requires="~=3.7",
    package_data={
        "MYPyrogram": ["py.typed"],  # Update to the new package name
    },
    packages=find_packages(exclude=["compiler*", "tests*"]),
    zip_safe=False,
    install_requires=requires
)
