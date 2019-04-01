How to accept Bitcoin on a website using Electrum
=================================================

This tutorial will show you how to accept Bitcoin on a website with SSL signed
payment requests, according to BIP-70_. The docs are updated for Electrum 3.1.2.

.. _BIP-70:
    https://github.com/bitcoin/bips/blob/master/bip-0070.mediawiki

Requirements
------------

* A webserver serving static HTML
* A valid SSL certificate (signed by a CA, for example free Letsencrypt_)
* Electrum version >= 3.1
* Electrum-Merchant_

.. _Letsencrypt:
    https://letsencrypt.org/
.. _Electrum-Merchant:
    https://pypi.org/project/electrum-merchant/

Create and use your merchant wallet
-----------------------------------

Create a wallet on your protected machine, as you want to keep your
cryptocurrency safe. If anybody compromise your merchant server, s/he will be able
to access read-only version of your wallet only and won't be able to spent currency.

Please notice that the potential intruder still will be able to see your
addresses, transactions and balance, though. It's also recommended to use a
separate wallet for your merchant purposes (and not your main wallet).

.. code-block:: bash

   electrum create

Still being on a protected machine, export your Master Public Key (xpub):

.. code-block:: bash

   electrum getmpk -w .electrum/wallets/your-wallet

Now you are able to set up your electrum merchant daemon.

On the server machine restore your wallet from previously exported Master
Public Key (xpub):

.. code-block:: bash

   electrum restore xpub...............................................

Once your read-only wallet is (re-)created, start Electrum as a daemon:

.. code-block:: bash

   electrum daemon start
   electrum daemon load_wallet

Add your SSL certificate to your configuration
----------------------------------------------

You should have a TLS/SSL private key and a public certificate for
your domain set up already. Please note that this is not your wallet
key but a private key for the matching TLS/SSL certificate.

Create a file that contains only the private key:

.. code-block:: openssl

   -----BEGIN PRIVATE KEY-----
   your private key
   -----END PRIVATE KEY-----

Set the path to your the SSL private key file with setconfig:

.. code-block:: bash

   electrum setconfig ssl_privkey /path/to/ssl.key

Create another file, file that contains your certificate,
and the list of certificates it depends on, up to the root
CA. Your certificate must be at the top of the list, and
the root CA at the end.

.. code-block:: openssl

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

This directory must be served by your webserver (eg Apache or Nginx)

.. code-block:: bash

   electrum setconfig requests_dir /srv/www/payment/

By default, electrum will display local URLs, starting with 'file://'
In order to display public URLs, we need to set another configuration
variable, url_rewrite. For example:

.. code-block:: bash

   electrum setconfig url_rewrite "[ 'file:///srv/www/', 'https://example.com/' ]"

Web server must be prepared for serving payment requests, a relevant
configuration for Nginx:

.. code-block:: nginx

    location /payment/ {
        default_type "application/bitcoin-paymentrequest";
        alias /srv/www/payment/;
    }
    
Or for Apache 2:

.. code-block:: apache

    <Directory /srv/www/payment/requests/>
        ForceType application/bitcoin-paymentrequest
    </Directory>

For other web servers, please check the manual on how to change the default MIME-type based on directory.

Install Electrum-Merchant
-------------------------

Install and run Electrum-Merchant_ configuration program. By default it
installs a simple interface, other interfaces are in preparation and will be
available in future.

.. code-block:: bash

    pip3 install electrum-merchant
    python3 -m electrum-merchant

Please note that it is required to follow steps in previous paragraph before you
will be able to successfuly run Electrum-Merchant_.

Create a signed payment request
-------------------------------

.. code-block:: bash

   electrum addrequest 3.14 -m "this is a test"
   {
      "URI": "bitcoin:1MP49h5fbfLXiFpomsXeqJHGHUfNf3mCo4?amount=3.14&r=https://example.com/payment/7c2888541a",
      "address": "1MP49h5fbfLXiFpomsXeqJHGHUfNf3mCo4",
      "amount": 314000000,
      "amount (BTC)": "3.14",
      "exp": 3600,
      "id": "7c2888541a",
      "index_url": "https://example.com/payment/index.html?id=7c2888541a",
      "memo": "this is a test",
      "request_url": "https://example.com/payment/7c2888541a",
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
we need to configure websockets.

Add web sockets support
-----------------------

Get SimpleWebSocketServer from here:

.. code-block:: bash

    git clone https://github.com/dpallot/simple-websocket-server

Set ``websocket_server`` and ``websocket_port`` in your config:

.. code-block:: bash

    electrum setconfig websocket_server example.com

    electrum setconfig websocket_port 9999

And restart the daemon:

.. code-block:: bash

    electrum daemon stop

    electrum daemon start

Now, the page is fully interactive: it will update itself
when the payment is received. 

Please notice that higher ports might be blocked on some client's
firewalls, so it is safer for example to reverse proxy websockets
transmission using standard ``443`` port on an additional external
IP address. If your local installation websocket server or server's
port Electrum serves varies from the port you want to announce to
your customers, you are able to set two additional config parameters:

* websocket_server_announce
* websocket_port_announce

JSONRPC interface
-----------------

Commands to the Electrum daemon can be sent using JSONRPC. This is
useful if you want to use electrum in a PHP script.

Note that the daemon uses a random port number by default. In order to
use a stable port number, you need to set the 'rpcport' configuration
variable (and to restart the daemon):

.. code-block:: bash

   electrum setconfig rpcport 7777

Further, starting with Electrum 3.0.5, the JSON-RPC interface is
authenticated using `HTTP basic auth`_.

.. _`HTTP basic auth`: https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication#Basic_authentication_scheme

The username and the password are config variables.
When first started, Electrum will initialise both;
the password will be set to a random string. You can of course
change them afterwards (the same way as the port, and then restart
the daemon). To simply look up their value:

.. code-block:: bash

   electrum getconfig rpcuser
   electrum getconfig rpcpassword

Note that HTTP basic auth sends the username and the password unencrypted as
part of the request. While using it on localhost is fine in our opinion,
using it across an untrusted LAN or the Internet is not secure.
Hence, you should take further measures in such cases, such as wrapping the
connection in a secure tunnel. For further details, `read this`_.

.. _`read this`: https://bitcoin.org/en/release/v0.12.0#rpc-ssl-support-dropped

After setting a static port, and configuring authentication,
we can perform queries using curl or PHP. Example:

.. code-block:: bash

   curl --data-binary '{"id":"curltext","method":"getbalance","params":[]}' http://username:password@127.0.0.1:7777

Query with named parameters:

.. code-block:: bash

   curl --data-binary '{"id":"curltext","method":"listaddresses","params":{"funded":true}}' http://username:password@127.0.0.1:7777

Create a payment request:

.. code-block:: bash

   curl --data-binary '{"id":"curltext","method":"addrequest","params":{"amount":"3.14","memo":"test"}}' http://username:password@127.0.0.1:7777
