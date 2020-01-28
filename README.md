<iframe width="560" height="315" src="https://www.youtube.com/embed/6j1I3mC0BR0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

# Python Package Template

*A generic python project template. Replace this line with a project description*



## TODO

- [ ] Replace all instances of package_name in this file
- [ ] Fill out all the sections in this file with your own information
- [ ] The [development guide](#development-contribution-guide) below will help you use the advanced features of this template
    - [ ] Finish creating setup.py
    - [ ] Update mkdocs.yml
- [ ] Create the actual package code
- [ ] Create tests



## Quick-start

*Include how people can get started using your project in the shortest time possible*



### Installation

#### From source

1. Clone this repo: (put github/source code link here)
2. Run ```pip install .``` or ```sudo pip3 install .```in the root directory



#### Usage

*Include how to use your package as an API (if that's what you're going for)*



#### Arguments

*If you are writing a script, include some helpful/often used arguments here. If you decide to use [docopt](http://docopt.org/) the usage string should do.* 



## Additional Documentation

*If you have any supplementary documentation elsewhere (i.e. https://readthedocs.org/) include references to it here.*



## Development-Contribution guide

*If you have any useful information that may be pertinent to people beginning to help develop the project put it here*



### Installing development dependencies

There are a few dependencies you will need to use this package fully, they are specified in the extras require parameter in setup.py but you can install them manually:

```
nox   	# Used to run automated processes
pytest 	# Used to run the test code in the tests directory
mkdocs	# Used to create HTML versions of the markdown docs in the docs directory
```

Just go through and run ```pip install <name>``` or ```sudo pip3 install <name>```. These dependencies will help you to automate documentation creation, testing, and build + distribution (through PyPi) automation.



### Folder Structure

*A Brief explanation of how the project is set up for people trying to get into developing for it*



#### /package_name

*Contains all the first party modules used in package_name*



#### /docs

*Contains markdown source files to be used with [mkdocs](https://www.mkdocs.org/) to create html/pdf documentation.* 

**Before you can use this you will need to setup the mkdocs.yml file **



#### /tests

*Contains tests to be run before release* 

**Before you can use this you will need to create tests, for more details take a look at [pytest](https://docs.pytest.org/en/latest/) **



#### Root Directory

**setup.py**: Contains all the configuration for installing the package via pip.



**LICENSE**: This file contains the licensing information about the project.



**CHANGELOG.md**: Used to create a changelog of features you add, bugs you fix etc. as you release.



**mkdocs.yml**: Used to specify how to build documentation from the source markdown files.



**noxfile.py**: Used to configure various automated processes using [nox](https://nox.readthedocs.io/en/stable/), these include;

- Building release distributions
- Releasing distributions on PyPi
- Running test suite agains a number of python versions (3.5-current)

If anything to do with deployment or releases is failing, this is likely the suspect.



There are 4 main sessions built into the noxfile and they can be run using ```nox -s <session name>``` i.e. ```nox -s test```:

- build: Creates a source distribution, builds the markdown docs to html, and creates a universal wheel distribution for PyPi.
- release: First runs the build session, then asks you to confirm all the pre-release steps have been completed, then runs *twine* to upload to PyPi
- test: Runs the tests specified in /tests using pytest, and runs it on python versions 3.5-3.8 (assuming they are installed)
- docs: Serves the docs on a local http server so you can validate they have the content you want without having to fully build them.



**.gitignore**: A preconfigured gitignore file (info on .gitignore files can be found here: https://www.atlassian.com/git/tutorials/saving-changes/gitignore)



## Additional Information

*If your module is complex enough, sometimes additional resources (papers, etc.) are useful to include here.*







