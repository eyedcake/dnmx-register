from setuptools import setup

setup (
    version = '0.0.1',
    name = 'dnmx-register',
    install_requires = ["requests>=2.25.1"],
    scripts = [
        'dnmx-register'
    ]
)
