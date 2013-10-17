from setuptools import setup

name = 'lumberjack'
version = "0.1-dev"

setup(name=name,
    version=version,
    license='BSD',
    packages=[name],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'docopt >= 0.6.1',
        'PyYAML',
        'Jinja2 >= 2.7',
    ],
    extras_require={
        'development': [
            'flake8',
            'py >= 1.4.17',
            'pytest >= 2.4.2',
            'pytest-flakes',
            'pytest-pep8',
            'pytest-cov',
            'tox',
            'setuptools-git',

        ],
    },
    entry_points={
        'console_scripts': 'lumberjack = lumberjack.commandline:main'
    },
)
