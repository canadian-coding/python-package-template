
# Development/Contribution guide

*If you have any useful information that may be pertinent to people beginning to help develop the project put it here*


## TODO

- [ ] Find and replace all instances of ```package_name``` with whatever the name of your package is


## Table of Contents
- [Development/Contribution guide](#developmentcontribution-guide)
  - [TODO](#todo)
  - [Table of Contents](#table-of-contents)
  - [Development guide](#development-guide)
    - [Getting dev dependencies](#getting-dev-dependencies)
    - [Building "API" docs](#building-api-docs)
    - [Nox integration](#nox-integration)
      - [Running tests](#running-tests)
      - [Building the package](#building-the-package)
  - [Contribution guide](#contribution-guide)
    - [TLDR](#tldr)
    - [Bug Reports & Feature Requests](#bug-reports--feature-requests)
    - [Pull requests](#pull-requests)
  - [Folder Structure](#folder-structure)
    - [/package_name](#package_name)
    - [/docs](#docs)
    - [/tests](#tests)
    - [Root Directory](#root-directory)
  - [Additional Information](#additional-information)

## Development guide



### Getting dev dependencies

To grab the specified development dependencies simply run ```pip install adh[dev]```, this will grab everything you need.



If for some reason this does not work, here are a list of development dependencies:

```
nox    # Used to run automated processes
pytest # Used to run the test code in the tests directory
mkdocs # Used to create HTML versions of the markdown docs in the docs directory
```



### Building "API" docs

API docs are useful if you want an easily navigatable version of the in-line documentation. The best way to do this currently is to download [pdoc3](https://pdoc3.github.io/pdoc/doc/pdoc/); ```pip install pdoc3``` then (assuming ahd is installed) run ````pdoc ahd --http localhost:8080`. Go to a browser and type in [http://localhost:8080/ahd](http://localhost:8080/ahd).



### Nox integration

If you have never used [nox](https://nox.readthedocs.io/) before it is a great system for automating tedius tasks (builds, distributions, testing etc). This project uses nox for a number of things and in the following sections I will explain each. 



#### Running tests

Testing is implemented using [pytest](https://docs.pytest.org/en/latest/), and can be run 1 of 2 ways:

1. Run the tests through nox using ```nox -s tests```, this will automatically run the tests against python 3.5-3.8 (assuming they are installed on system).
2. Go to the root directory and run ```pytest```, this should automatically detect the /tests folder and run all tests.



#### Building the package

This is not necessary for pull requests, or even development but if you want to validate that it doesn't break buildability here is how to do it. You can use ```nox -s build```, this will create a source distribution for you using pythons [setuptools module](https://setuptools.readthedocs.io/en/latest/).



## Contribution guide

### TLDR

1. Commenting/documentaion is **not** optional
2. Breaking platform compatability is **not** acceptable
3. Do **everything** through [github](https://github.com/Descent098/ahd) (don't email me), and (mostly) everything has been setup for you.



### Bug Reports & Feature Requests

Submit all bug reports and feature requests on [github](https://github.com/Descent098/ahd/issues/new/choose), the format for each is pre-defined so just follow the outlined format



### Pull requests

Pull requests should be submitted through github and follow the default pull request template specified. If you want the rundown of what needs to be present:

1. Provide a clear explination of what you are doing/fixing
2. Feature is tested on Windows & *nix (unless explicitly incompatable)
3. All Classes, modules, and functions must have docstrings that follow the [numpy-style guide](https://numpydoc.readthedocs.io/en/latest/format.html).
4. Unless feature is essential it cannot break backwards compatability



## Folder Structure

*A Brief explanation of how the project is set up for people trying to get into developing for it*



### /package_name

*Contains all the first party modules used in package_name*



### /docs

*Contains markdown source files to be used with [mkdocs](https://www.mkdocs.org/) to create html/pdf documentation.* 

**Before you can use this you will need to setup the mkdocs.yml file **



### /tests

*Contains tests to be run before release* 

**Before you can use this you will need to create tests, for more details take a look at [pytest](https://docs.pytest.org/en/latest/) **



### Root Directory

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

