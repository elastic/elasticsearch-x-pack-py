Elasticsearch X-Pack
=====================

This is an addon to the official elasticsearch python client that adds
functionality for the `X-Pack extensions <https://www.elastic.co/v5>`_

Installation
------------

You can install this addon using ``pip``::

    pip install elasticsearch-xpack

Usage
-----

You can use this client alone:

.. code:: python

    from elasticsearch import Elasticsearch
    from elasticsearch_xpack import XPackClient

    client = Elasticsearch()
    xpack = XPackClient(client)

    xpack.info()

Or you can add the ``xpack`` namespace to the official client to mimic the
behaviors of other namespaces:

.. code:: python

    XPackClient.infect_client(client)

    client.xpack.info()

License
-------

Copyright 2015 Elasticsearch

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

