# installation: pip install rdig
from setuptools import (
  setup,
  find_packages,
)

# get list of requirement strings from requirements.txt
remove_whitespace = lambda x : ''.join(x.split())
sanitize = lambda x : not x.startswith('#') and x != ''
with open('requirements.txt', 'r') as f:
    requires = filter(sanitize, map(remove_whitespace, f.readlines() ))

setup( 
    name = 'yaml_consulate',
    version = '1.0.0',
    description = 'Accept a path to a YAML file and emit consulate JSON schema to STDOUT.',
    long_description = open('README.rst').read(),
    author = 'Russell Ballestrini',
    url = 'https://github.mandiant.com/rballestrini/yaml_consulate',
    packages = find_packages(),
    include_package_data = True,
    install_requires = requires,
    entry_points = {
      'console_scripts': [
        'yaml_consulate = yaml_consulate.__main__:main',
      ],
    }
)
