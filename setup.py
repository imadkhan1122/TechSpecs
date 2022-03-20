from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()
    
setup_args = dict(
    name='techSpecs',
    version='0.0.1',
    description='Useful tools to get data from TechSPecs API',
    long_description_content_type="https://techspecs.readme.io/reference/apple-machine-id-search",
    long_description=README,
    license='MIT',
    packages=find_packages(),
    author='Imad Ud Din',
    author_email='imadyousafzai0@gmail.com',
    keywords=['TechSpecAPI'],
    url='https://github.com/imadkhan1122/TechSpecs',
    download_url='https://pypi.org/project/TechSpecs/'
)

install_requires = [
    'requests==2.26.0'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
