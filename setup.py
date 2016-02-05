import os

from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-ibantools',
    version='0.2',
    packages=['bank'],
    include_package_data=True,
    license='BSD License',
    description='A simple IBAN/Bic Datamanager app',
    long_description=README,
    url='https://github.com/nadobit/django-ibantools',
    author='Bastian Probian',
    author_email='contmp@me.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
