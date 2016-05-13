#!/usr/bin/env python
from argparse import ArgumentParser

from .yaml_consulate import (
  load_yaml,
  consulize,
)

import json

def main():
    parser = ArgumentParser(
      'Accept a path to a YAML file and emit consulate JSON schema to STDOUT.')
    parser.add_argument('yaml_path', help='path to YAML file to convert.')
    parser.add_argument('root', help='the root key to branch varibles under.')
    args = parser.parse_args()

    data = { args.root : load_yaml(args.yaml_path) }

    json_data = json.dumps(consulize(data), indent=2)
    print(json_data)
