"""
Description:
    Contains all the configuration for the package on pip
"""
import setuptools

def get_content(*filename):
    """ Gets the content of a file and returns it as a string
    Args:
        filename(str): Name of file to pull content from
    Returns:
        str: Content from file
    """
    content = ""
    for file in filename:
        with open(file, "r") as full_description:
            content += full_description.read()
    return content

setuptools.setup(
    name = "", # TODO: Give the package a name
    version = "0.0.1", # I recommend every 2nd decimal release for big releases and 3rd for bug fixes.
    author = "", # TODO: Add your name
    author_email = "", # TODO: Add your email
    description = "", # TODO: Give the package a description
    long_description = get_content("README.md", "CHANGELOG.md"),
    long_description_content_type = "text/markdown",
    url = "", # TODO: Put github link if applicable
    include_package_data = True,
    packages = setuptools.find_packages(),

    # The code below is used to define entrypoints, if you don't know what this is then:
    # SEE: https://canadiancoding.ca/posts/post/python/script-entrypoints/

    
    # entry_points = { 
    #        'console_scripts': ['... = ...']
    #    },
    

    install_requires = [
    "docopt", # Used for argument parsing
      ],
    extras_require = {
        "dev" : ["nox",    # Used to run automated processes
                 "pytest", # Used to run the test code in the tests directory
                 "mkdocs"],# Used to create HTML versions of the markdown docs in the docs directory

    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)