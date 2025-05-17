from setuptools import setup, find_packages

setup(
    name="dash-gauge-component",
    version="0.1.0",
    author="Dash Gauge Component Team",
    author_email="example@example.com",
    description="A responsive gauge component for Dash applications",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/dash-gauge-component",
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