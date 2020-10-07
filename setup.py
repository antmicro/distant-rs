from setuptools import setup, find_packages

setuptools.setup(
        name="distant-rs",
        version="0.1",
        author="Adam Olech",
        author_email="aolech@antmicro.com",
        description="ResultStore client",
        packages=find_packages(),
        install_requires=["protobuf", "grpcio", "termcolor", "requests"],
        python_requires='>=3.6',
        )

