"""Contains all the configuration for the package on pip"""
import setuptools

def get_content(*filename:str) -> str:
    """ Gets the content of a file or files and returns
    it/them as a string
    Parameters
    ----------
    filename : (str)
        Name of file or set of files to pull content from 
        (comma delimited)
    
    Returns
    -------
    str:
        Content from the file or files
    """
    content = ""
    for file in filename:
        with open(file, "r") as full_description:
            content += full_description.read()
    return content

setuptools.setup(
    name = "", # TODO: Give the package a name
    version = "0.0.1", # I recommend every 2nd decimal release (i.e. 0.x.0) for big releases and 3rd (i.e. 0.0.x) for bug fixes.
    author = "", # TODO: Add your name
    author_email = "", # TODO: Add your email
    description = "", # TODO: Give the package a description
    long_description = get_content("README.md", "CHANGELOG.md"),
    long_description_content_type = "text/markdown",
    # Replace https://github.com/canadian-coding/python-package-template with your repo github URL 
    project_urls = {
        "User Docs" :      "", # TODO: Fill out or remove
        "API Docs"  :      "", # TODO: Fill out or remove
        "Source" :         "https://github.com/canadian-coding/python-package-template",
        "Bug Report":      "https://github.com/canadian-coding/python-package-template/issues/new?assignees=Descent098&labels=bug&template=bug_report.md&title=%5BBUG%5D",
        "Feature Request": "https://github.com/canadian-coding/python-package-template/issues/new?labels=enhancement&template=feature_request.md&title=%5BFeature%5D",
        "Roadmap":         "https://github.com/canadian-coding/python-package-template/projects"
    },
    include_package_data = True,
    packages = setuptools.find_packages(),

    # The code below is used to define entrypoints, if you don't know what this is then:
    # SEE: https://canadiancoding.ca/posts/post/python/script-entrypoints/

    
    # entry_points = { 
    #        'console_scripts': ['... = ...']
    #    },
    

    install_requires = [
    "docopt", # Used for argument parsing if you are writing a CLI
        ],
    extras_require = {
        "dev" : ["nox",    # Used to run automated processes
                "pytest",  # Used to run the test code in the tests directory
                "mkdocs"], # Used to create HTML versions of the markdown docs in the docs directory

    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning" # TODO: Change this when you have created package, SEE: https://pypi.org/classifiers/
    ],
)