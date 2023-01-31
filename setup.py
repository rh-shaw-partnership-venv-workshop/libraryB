from setuptools import setup

setup(
    name='libraryB',
    version='0.0.1',
    description='LibraryB has dependencies and setup.py',
    author='Elijah DeLee',
    author_email='kdelee@redhat.com',
    url='https://github.com/rh-shaw-partnership-venv-workshop/libraryB',
    install_requires=[
        'pytest==6.0.0',
        'requests',
    ],
    python_requires=">=3.0",
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
    ],
)
