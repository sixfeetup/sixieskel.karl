from setuptools import setup, find_packages

version = '1.0.3'

long_description = (
    open('README.txt').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(
    name='sixieskel.karl',
    version=version,
    description="Collection of templates for KARL development",
    long_description=long_description,
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Programming Language :: Python",
    ],
    keywords='karl python templer template',
    author='Six Feet Up, Inc.',
    author_email='info@sixfeetup.com',
    url='http://github.com/sixfeetup/sixieskel.karl',
    license='gpl',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['sixieskel'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'sixieskel.buildout',
    ],
    entry_points="""
    [paste.paster_create_template]
    sfu_karl_buildout = sixieskel.karl.template:KarlBuildout
    karl_custom_pkg = sixieskel.karl.template:KarlCustomizationPackage
    """,
    )
