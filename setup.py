import setuptools
from os.path import dirname, join


def readme() -> str:
    """Read the README file."""
    return open(join(dirname(__file__), "readme.md")).read()


setuptools.setup(
    name="streamlit-antd-components",
    version="0.3.3",
    author="Ji Hao Ran",
    author_email="",
    maintainer="Panagiotis Erodotou",
    maintainer_email="",
    description="A Streamlit custom component to implement Antd-Design and Mantine widgets",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/nicedouble/StreamlitAntdComponents",
    packages=setuptools.find_packages(),
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=[
        "streamlit >= 1.12.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Streamlit",
    ],
    keywords="streamlit, antd, mantine, components, widgets, ui",
)
