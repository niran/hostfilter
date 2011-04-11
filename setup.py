from setuptools import setup

setup(
    name='hostfilter',
    version='0.1',
    description='A Django app with middleware that allows subdomains to have a limited view of a project.',
    author='Texas Tribune',
    author_email='tech@texastribune.org',
    url='http://github.com/niran/hostfilter',
    packages=['hostfilter'],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
