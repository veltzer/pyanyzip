import setuptools

setuptools.setup(
    name='pyanyzip',
    version='0.0.7',
    description='pyanyzip is a module to help with dealing with compressed files transparently',
    long_description='pyanyzip is a module to help with dealing with compressed files transparently',
    url='https://veltzer.github.io/pyanyzip',
    author='Mark Veltzer',
    author_email='mark.veltzer@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
    ],
    keywords='python zip bz2 gzip',
    package_dir={'': 'src'},
    py_modules=['pyanyzip'],
    install_requires=[
        'pypipegzip',  # for opening zipped files
        'pylzma',  # for working with .xz files
        'typing',  # for types
    ],
)
