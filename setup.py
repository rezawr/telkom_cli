from setuptools import setup, find_packages

with open('README.md', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name='telkom_cli',
    version='1.0.0',
    description='Command line user export utility',
    long_description=readme,
    author='Reza Wahyu Ramadhan',
    author_email='reza@admin.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': 'telkom_cli=telkom_cli.cli:main'
    },
    install_requires=[]
)