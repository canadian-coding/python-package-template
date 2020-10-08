# package_name

*A generic python PyPi project template. Replace this line with a project description*

---

**This file is meant to be a template but my recommendation is to fork it and make it your own for what suits your projects. After completing the TODO section take a look at the end of the file for final touches.

Video guide for usage of the package template can be found [here](https://www.youtube.com/watch?v=6j1I3mC0BR0).**

## TODO

- [ ] Setup a [github project board](https://docs.github.com/en/free-pro-team@latest/github/managing-your-work-on-github/about-project-boards). Here are a few examples of some boards; [sdu](https://github.com/Descent098/sdu/projects), [pystall](https://github.com/Descent098/pystall), [ahd](https://github.com/Descent098/ahd)
- [ ] Replace all instances of package_name in this file
- [ ] Finish creating setup.py
- [ ] Update mkdocs.yml or remove it if you don't intend to have user docs. Take a look at [ahd](https://ahd.readthedocs.io/en/latest/) for a great example of setting up the [docs folder](https://github.com/Descent098/ahd/tree/master/docs) and configuring [mkdocs.yml](https://github.com/Descent098/ahd/blob/master/mkdocs.yml)
- [ ] Fill out [features & Roadmap section](#features--roadmap)
- [ ] Fill out [quick start](#quick-start)
- [ ] Create the actual package code
- [ ] Fill out or remove the following sections
  - [ ] [What does package_name do?](#what-does-package_name-do)
  - [ ] [Examples](#examples)
  - [ ] [Why should I use package_name?](#why-should-i-use-package_name)
  - [ ] [Who is package_name for?](#who-is-package_name-for)
  - [ ] [Arguments](#arguments)
  - [ ] [Additional documentation](#additional-documentation)
- [ ] Remove [From PyPi](#from-pypi) section if you don't intend to publish it to PyPi
- [ ] Remove any outstanding sections from [Table of Contents](#table-of-contents)
- [ ] Fill out CONTRIBUTING.md
- [ ] Fill out CHANGELOG.md
- [ ] Create tests, see [creating tests](#creating-tests) if you have never made tests before
- [ ] Do (or don't) final touches, then remove this whole section from your readme

## Final Touches

These are all optional extras you can do to make your project better, you can either do them or just delete this whole section.

### Uploading to PyPi

Now that you have finished the todo section (and assuming you want people to be able to pip install without downloading the source) it can be published on [PyPi](https://pypi.org/) by first signing up for an account, then running ```nox -s release```. The release session will build a distribution, prompt you to make sure you have filled out all the information necessary and then start the upload to PyPi (you will then have to login to PyPi through the command line).

### ReadTheDocs

There are some optional extras, for example if you signup for a [readthedocs](https://readthedocs.org/) account you can host your documentation with a single click. Alternatively if you want to use a custom theme for your documentation you can use github pages and run ```mkdocs gh-deploy``` which will do the documentation building for you. From there you can follow [this guide](https://help.github.com/en/github/working-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) to setup your github pages for your project, by default running ```mkdocs gh-deploy``` will create a gh-pages branch for you so you can just hit that checkbox in the repositories settings to get setup.

### Auto generated API docs

If you have written an API and want to use API documentation that autobuilds based on docstrings [like sdu](https://kieranwood.ca/sdu/), I would highly recommend [pdoc3](https://pypi.org/project/pdoc3/). This package will allow you to build the docs very easily, check out [their documentation](https://pdoc3.github.io/pdoc/) for details.

### Creating tests

If you have never created tests before, take a look at the [pytest docs](https://docs.pytest.org/en/stable/) and [this video](https://www.youtube.com/watch?v=bbp_849-RZ4) or [this video](https://www.youtube.com/watch?v=byaxg00Gf9I).

### Setting up deepsource.io

[Deepsource.io](https://deepsource.io) is an incrediby useful tool I have found that will scan your github repo and warn you about potential security issues, anti-patterns, and style guide infractions you've made. It is completely free for pulic repo's and has saved me a few times from some prety big mistakes.

---

## Table of Contents
- [What does package_name do?](#what-does-package_name-do)
- [Features & Roadmap](#features--roadmap)
- [Why should I use package_name?](#why-should-i-use-package_name)
- [Who is package_name for?](#who-is-package_name-for)
- [Quick-start](#quick-start)
    - [Installation](#installation)
      - [From source](#from-source)
      - [From PyPi](#from-pypi)
      - [Examples](#examples)
- [Usage](#usage)
    - [Arguments](#arguments)
- [Additional Documentation](#additional-documentation)

## What does package_name do?

*Provide a brief exposition on what the purpose of your package is, or change this heading to goals (like [sdu](https://github.com/Descent098/sdu#goals))*

## Features & Roadmap

*Include a bullet point list of implemented features, and either a link to the github planning board or list of coming-soon features*

## Why should I use package_name?

*If there are well-known alternatives provide details about why people should use your package instead*

## Who is package_name for?

*If your package has multiple uses in seperate domains it may be worth explaning use cases in different domains; see [ahd](https://github.com/Descent098/ahd#who-is-ahd-for) for example*

## Quick-start

*Include how people can get started using your project in the shortest time possible*

### Installation

#### From source

1. Clone this repo: (put github/source code link here)
2. Run ```pip install .``` or ```sudo pip3 install .```in the root directory

#### From PyPi

1. Run ```pip install package_name```

#### Examples

*Include an example or two of usage, or common use cases*

## Usage

*Include how to use your package as an API (if that's what you're going for)*

### Arguments

*If you are writing a script, include some helpful/often used arguments here. If you decide to use [docopt](http://docopt.org/) the usage string should do.* 

## Additional Documentation

*If you have any supplementary documentation elsewhere (i.e. https://readthedocs.org/) include references to it here.*
