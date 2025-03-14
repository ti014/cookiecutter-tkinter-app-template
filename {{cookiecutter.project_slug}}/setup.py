from setuptools import setup, find_packages

setup(
    name="{{cookiecutter.project_slug}}",
    version="0.1.0",
    author="{{cookiecutter.author_name}}",
    author_email="{{cookiecutter.author_email}}",
    description="{{cookiecutter.description}}",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    entry_points={
        "console_scripts": [
            "{{cookiecutter.project_slug}} = main:main",
        ],
    },
    python_requires=">={{cookiecutter.python_version}}",
)