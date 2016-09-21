How to accept Bitcoin on a website using Electrum
=================================================

This tutorial will show you how to accept Bitcoin on a website with
SSL signed payment requests. It is updated for Electrum 2.6.


Requirements
------------

- A webserver serving static HTML
- A SSL certificate (signed by a CA)
- Electrum version >= 2.6

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

By default, electrum will display local URLs, starting with 'file://'
In order to display public URLs, we need to set another configuration
variable, url_rewrite. For example:

.. code-block:: bash

   electrum setconfig url_rewrite "['file:///var/www/','https://electrum.org/']"

Create a signed payment request
-------------------------------

.. code-block:: bash

   electrum addrequest 3.14 -m "this is a test"
   {
      "URI": "bitcoin:1MP49h5fbfLXiFpomsXeqJHGHUfNf3mCo4?amount=3.14&r=https://electrum.org/r/7c2888541a", 
      "address": "1MP49h5fbfLXiFpomsXeqJHGHUfNf3mCo4", 
      "amount": 314000000, 
      "amount (BTC)": "3.14", 
      "exp": 3600, 
      "id": "7c2888541a", 
      "index_url": "https://electrum.org/r/index.html?id=7c2888541a", 
      "memo": "this is a test", 
      "request_url": "https://electrum.org/r/7c2888541a", 
      "status": "Pending", 
      "time": 1450175741
   }

This command returns a json object with two URLs:

 - request_url is the URL of the signed BIP70 request.
 - index_url is the URL of a webpage displaying the request.

Note that request_url and index_url use the domain name we defined in
url_rewrite.

You can view the current list of requests using the 'listrequests'
command.


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


Set ``websocket_server`` and ``websocket_port`` in your config:

.. code-block:: bash

    electrum setconfig websocket_server <FQDN of your server>

    electrum setconfig websocket_port 9999


And restart the daemon:

.. code-block:: bash

   electrum daemon stop

   electrum daemon start
   
Now, the page is fully interactive: it will update itself
when the payment is received. Please notice that higher ports might 
be blocked on some client's firewalls, so it is more safe for 
example to reverse proxy websockets transmission using standard 
``443`` port on an additional subdomain.

JSONRPC interface
-----------------

Commands to the Electrum daemon can be sent using JSONRPC. This is
useful if you want to use electrum in a PHP script.

Note that the daemon uses a random port number by default. In order to
use a stable port number, you need to set the 'rpcport' configuration
variable (and to restart the daemon):

.. code-block:: bash

   electrum setconfig rpcport 7777

With this setting, we can perform queries using curl or PHP. Example:

.. code-block:: bash

   curl --data-binary '{"id":"curltext","method":"getbalance","params":[]}' http://127.0.0.1:7777

Query with named parameters:

.. code-block:: bash

   curl --data-binary '{"id":"curltext","method":"listaddresses","params":{"funded":true}}' http://127.0.0.1:7777

Create a payment request:

.. code-block:: bash

   curl --data-binary '{"id":"curltext","method":"addrequest","params":{"amount":"3.14","memo":"test"}}' http://127.0.0.1:7777


