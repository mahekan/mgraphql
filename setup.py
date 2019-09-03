from setuptools import setup, find_packages
 
with open("README.md", "r") as readme_file:
    readme = readme_file.read()
 
requirements = ["requests>=2"]
 
setup(
    name="mgraphql",
    version="0.0.4",
    author="ayaz abdi",
    author_email="mayazabdi@gmail.com",
    description="Python library link with graphql",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/mahekan/mgraphql",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
