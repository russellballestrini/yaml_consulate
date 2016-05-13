yaml_consulate
##############

This program basically does an ETL (export, transform, load) from YAML to JSON in a format that consulate can load.

Consulate is a tool for managing consul.

For example::
 
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
