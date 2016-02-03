from setuptools import setup

with open('requirements.txt') as f:
    require = f.readlines()
install_requires = [r.strip() for r in require]

setup(
    name='petulant-bear',
    version='0.2.0',
    description='Presents etree interface to netcdf4-python objects using NCML data model',
    author='David Stuebe',
    author_email='DStuebe@ASAScience.com',
    url='https://github.com/ioos/petulant-bear',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
    ],
    license='GPLv3',
    keywords='netcdf lxml xml metadata ncml',
    packages=['petulantbear'],
    tests_require=['pytest'],
    install_requires=[
            'netCDF4>=1.0.0',
            'numpy>=1.7.0',
            'lxml>=3.2.1',
            ],
)
