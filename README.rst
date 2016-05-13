yaml_consulate
##############

Pass a YAML file and key root and we will emit JSON in a schema that consulate may digest.

This is an example of the YAML to Consulate JSON schema conversion::
 
 yaml_consulate example.yaml my_website

You can pipe this into consulate kv restore like this::

 yaml_consulate example.yaml my_website | ssh $VPC_NAME-consul01 "consulate kv restore"

install
========

download repo and run::

 python develop setup.py

verify install by running::

 yaml_consulate --help

quick guide
===========

**example.yaml**::

 domain: russell.ballestrini.net
 port: 80
 
 books:
   - don't make me think
   - the goal
 
 this:
   is:
     deeply:
       nested: amirite?


And the conversion::

 yaml_consulate example.yaml my_website

Results in this json which consulate may ingest::
 
 [
   [
     "my-website/port",
     0,
     80
   ],
   [
     "my-website/this/is/deeply/nested",
     0,
     "amirite?"
   ],
   [
     "my-website/domain",
     0,
     "russell.ballestrini.net"
   ],
   [
     "my-website/books",
     0,
     [
       "don't make me think",
       "the goal"
     ]
   ]
 ]
