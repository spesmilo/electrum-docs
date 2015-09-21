How to accept Bitcoin on a website using Electrum
=================================================

This tutorial will show you how to accept Bitcoin on a
website with SSL signed payment requests.


Requirements
------------

- A webserver serving static HTML
- A SSL certificate (signed by a CA)
- Electrum 2.4

Create a wallet
---------------

Create a wallet on your web server:

.. code-block:: bash

   electrum create

You can also use a watching only wallet (restored from xpub), if you
want to keep private keys off the server.

Once your wallet is created, start Electrum as a daemon:

.. code-block:: bash

   electrum daemon start

Add your SSL certificate to your configuration
----------------------------------------------

You should have a private key and a public certificate for
your domain.

Create a file that contains only the private key:

.. code-block:: none

   -----BEGIN PRIVATE KEY-----
   your private key
   -----BEGIN END KEY-----


Set the path to your the private key file with setconfig:

.. code-block:: bash

   electrum setconfig ssl_privkey /path/to/ssl.key

Create another file, file that contains your certificate,
and the list of certificates it depends on, up to the root
CA. Your certificate must be at the top of the list, and
the root CA at the end.

.. code-block:: none

   -----BEGIN CERTIFICATE-----
   your cert
   -----END CERTIFICATE-----
   -----BEGIN CERTIFICATE-----
   intermediate cert
   -----END CERTIFICATE-----
   -----BEGIN CERTIFICATE-----
   root cert
   -----END CERTIFICATE-----


Set the ssl_chain path with setconfig:

.. code-block:: bash

   electrum setconfig ssl_chain /path/to/ssl.chain


Configure a requests directory
------------------------------

This directory must be served by your webserver (eg Apache)

.. code-block:: bash

   electrum setconfig requests_dir /var/www/r/


Create a signed payment request
-------------------------------

.. code-block:: bash

   electrum addrequest 3.14 -m "this is a test"

   {
   "address": "15KX6Fty5zQNKfNHvcg6kmpX5Kpfdm5yCD", 
   "amount": "3.14 BTC", 
   "exp": 3600, 
   "id": "8c85589985", 
   "memo": "this is a test", 
   "status": "Unknown", 
   "time": 1437765812
   }

With the listrequests command, we can see our list of requests:

.. code-block:: bash

   electrum listrequests

   [
    {
        "URI": "bitcoin:15KX6Fty5zQNKfNHvcg6kmpX5Kpfdm5yCD?amount=1.&amp;r=file:///var/www/r/d898360e19", 
        "address": "15KX6Fty5zQNKfNHvcg6kmpX5Kpfdm5yCD", 
        "amount": "3.14 BTC", 
        "exp": 3600, 
        "id": "d898360e19", 
        "index_url": "file:///var/www/r/index.html?id=d898360e19", 
        "memo": "this is a test", 
        "request_url": "file:///var/www/r/d898360e19", 
        "status": "Pending", 
        "time": 1437765725
    }
   ]


Note that listrequests shows the status of the request (pending). It
also displays request_url: this is the path to a signed BIP70 request.

For the moment request_url is a local URL. We need to instruct
electrum to create a public url. This is achieved by setting another
configuration variable, url_rewrite:

.. code-block:: bash

   electrum setconfig url_rewrite "['file:///var/www/','https://electrum.org/']"


With this setting, we can list requests again

.. code-block:: bash

   electrum listrequests

   [
    {
        "URI": "bitcoin:15KX6Fty5zQNKfNHvcg6kmpX5Kpfdm5yCD?amount=1.&amp;r=https://electrum.org/r/8c85589985", 
        "address": "15KX6Fty5zQNKfNHvcg6kmpX5Kpfdm5yCD", 
        "amount": "3.14 BTC", 
        "exp": 3600, 
        "id": "8c85589985", 
        "index_url": "https://electrum.org/r/index.html?id=8c85589985", 
        "memo": "this is a test", 
        "request_url": "https://electrum.org/r/8c85589985", 
        "status": "Pending", 
        "time": 1437765812
    }
   ]

Now request_url and index_url are a public URLs.

Open the payment request page in your browser
---------------------------------------------

Let us open index_url in a web browser.

.. image:: png/payrequest.png


The page shows the payment request. You can open the
bitcoin: URI with a wallet, or scan the QR code. The bottom
line displays the time remaining until the request expires.

.. image:: png/payreq_window.png
          

This page can already used to receive payments. However,
it will not detect that a request has been paid; for that
we need to configure websockets

Add web sockets support
-----------------------

Get SimpleWebSocketServer from here:

.. code-block:: bash

   git clone https://github.com/ecdsa/simple-websocket-server.git


Set websocket_server in your config:

.. code-block:: bash

   electrum setconfig websocket_server <FQDN of your server>


And restart the daemon:

.. code-block:: bash

   electrum daemon stop

   electrum daemon start
   
Now, the page is fully interactive: it will update itself
when the payment is received.

Customize
---------

If you decide to modify index.html, please note that it
will be overwritten everytime you restart the electrum
daemon; you need to modify the source file.

If you want to access electrum commands by PHP, instead of
the command line, you may want to use the jsonrpc interface
to Electrum.

JSONRPC interface
-----------------

Start the jsonrpc interface:

.. code-block:: bash

   electrum -g jsonrpc

Example query:

.. code-block:: bash

   curl --data-binary '{"id":"curltext","method":"getbalance","params":[]}' http://127.0.0.1:7777

Query with named parameters:

.. code-block:: bash

   curl --data-binary '{"id":"curltext","method":"listaddresses","params":{"funded":true}}' http://127.0.0.1:7777
