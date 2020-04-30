from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="get-git-repository",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'get-git-repository = get_git_repository.__main__:main'
        ]
    },

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=["requests"],
    python_requires='>=3.7',

    # metadata to display on PyPI
    author="okojomoeko",
    author_email="",
    description="You can get all repository",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/okojomoeko/get-git-repository",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
