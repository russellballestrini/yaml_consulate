yaml_consulate
##############

Pass a YAML file and key root and we will emit JSON in a schema that consulate may digest.

This is an example of the YAML to Consulate JSON schema conversion::
 
 yaml_consulate example.yaml my_website

You can pipe this into consulate kv restore like this::

 yaml_consulate example.yaml my_website | ssh $VPC_NAME-consul01 "consulate kv restore"

install
========

::
 python develop setup.py

