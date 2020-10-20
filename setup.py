from setuptools import setup, find_packages

setuptools.setup(
        name="distant-rs",
        version="0.1",
        author="Adam Olech",
        author_email="aolech@antmicro.com",
        description="ResultStore client",
        packages=find_packages(),
        install_requires=[
            "protobuf", 
            "grpcio", 
            "google-auth",
            "google-cloud-storage",
            "requests"
            ],
        python_requires='>=3.6',
        )
