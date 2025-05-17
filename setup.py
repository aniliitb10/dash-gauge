from setuptools import setup, find_packages

setup(
    name="dash-gauge",
    version="0.1.0",
    author="Anil Kumar",
    author_email="aniliitb10@gamil.com",
    description="A responsive gauge component (with needle) for Dash applications",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/aniliitb10/dash-gauge",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "dash>=2.0.0",
        "plotly>=5.0.0",
        "numpy>=1.19.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)