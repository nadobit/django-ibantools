import os

from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-ibantools',
    version='0.4.3',
    packages=['ibantools'],
    include_package_data=True,
    license='BSD License',
    description='A simple IBAN/Bic Helper app',
    long_description=README,
    url='https://github.com/nadobit/django-ibantools',
    author='Bastian Probian',
    author_email='contmp@me.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.0',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
