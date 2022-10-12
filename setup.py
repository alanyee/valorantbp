from setuptools import setup

# with open("README.md") as f:
#    readme = f.read()

setup(
    name="valorantbp",
    entry_points={
        "console_scripts": [
            "valorantbp = valorant.valorant:main",
        ],
    },
    version="0.0.1",
    description="Generate large textbook integer-type RSA schema",
    long_description="",
    author="Alan Yee",
    author_email="alanyee@users.noreply.github.com",
    url="https://github.com/alanyee/rsa-keygen",
    packages=["valorant"],
    include_package_data=True,
    python_requires=">=3.8",
    extras_require={"testing": ["pylint", "pytest", "mypy"]},
)
