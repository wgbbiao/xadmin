#!/usr/bin/env python
from io import open
from setuptools import setup
# version_tuple = __import__('xadmin').VERSION
# version = ".".join([str(v) for v in version_tuple])

setup(
    name='xadmin2',
    version='2.0.4',
    description='Drop-in replacement of Django admin comes with lots of goodies, fully extensible with plugin support, pretty UI based on Twitter Bootstrap.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    author='wgbbiao',
    author_email='wgb237@163.com',
    license=open('LICENSE', encoding='utf-8').read(),
    url='http://www.xadmin.io',
    download_url='https://github.com/beeguess/xadmin/archive/master.zip',
    packages=[
        'xadmin', 'xadmin.migrations', 'xadmin.plugins', 'xadmin.templatetags',
        'xadmin.views'
    ],
    include_package_data=True,
    install_requires=[
        'setuptools', 'Django>=3', 'django-crispy-forms>=1.8.1',
        'django-reversion>=3.0.4', 'django-formtools>=2.1',
        'django-import-export>=1.2', 'httplib2==0.9.2', 'future'
    ],
    extras_require={
        'Excel': ['xlwt', 'xlsxwriter'],
        'Reversion': ['django-reversion>=3.0.4'],
    },
    zip_safe=False,
    keywords=['admin', 'django', 'xadmin', 'bootstrap'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        "Programming Language :: JavaScript",
        'Programming Language :: Python',
        "Programming Language :: Python :: 3.4",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ])
