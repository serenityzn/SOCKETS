#!/usr/bin/env python
import yaml

def read_conf():
    with open('conf/srv.yaml', 'r') as f:
        doc = yaml.load(f)
    return doc
