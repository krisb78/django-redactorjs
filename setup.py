from setuptools import (
    setup,
    find_packages
)

from redactorjs import __version__ as version

setup(
    name = 'django-redactorjs',
    version = version,
    description = 'A simple redactor.js widget for Django',
    author = 'Krzysztof Bandurski',
    author_email = 'krzysztof.bandurski@gmail.com',
    url = 'https://github.com/krisb78/django-redactorjs',
    packages = find_packages(
        exclude=[
            'testproject',
            'testproject.app',
        ]
    ),
    zip_safe=False,
    include_package_data = True,
    install_requires=[
        'Django>=1.2',
    ],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Database",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ]
)
