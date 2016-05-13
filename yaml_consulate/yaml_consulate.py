#!/usr/bin/env python
from six import iteritems

import collections

import yaml

import json

def load_yaml(path):
    """load YAML config file and return Python Dict."""
    with open(path) as f:
        return yaml.load(f)

def flatten(d, parent_key='', sep='/'):
    """http://stackoverflow.com/a/6027615"""
    items = []
    for k, v in iteritems(d):
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(iteritems(flatten(v, new_key, sep=sep)))
        else:
            items.append((new_key, v))
    return dict(items)

def consulize(d):
    """take a python dict and format it how consul likes it."""
    list_o_lists = []
    for key, value in iteritems(flatten(d)):
        list_o_lists.append([key.replace('_', '-'), 0, value])
    return list_o_lists
