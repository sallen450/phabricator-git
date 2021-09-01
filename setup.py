from setuptools import setup, find_packages

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name='pha-g',
    version="0.0.1",
    author='anonymous',
    author_email='anonymous@example.com',
    description='sync ',
    packages=find_packages(),
    py_modules=['phabricator_git', 'app'],
    install_requires=[requirements],
    python_requires='>=3.7',
    entry_points='''
        [console_scripts]
        pha-g=phabricator_git:main
    '''
)
