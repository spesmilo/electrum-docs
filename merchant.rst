How to accept Bitcoin on a website using Electrum
=================================================

This tutorial will show you how to accept Bitcoin on a website with SSL signed
payment requests, according to BIP-70_. The docs are updated for Electrum 4.0.

.. _BIP-70:
    https://github.com/bitcoin/bips/blob/master/bip-0070.mediawiki

Requirements
------------

* Electrum version >= 4.0 (currently in development_)
* A valid SSL certificate (signed by a CA, for example free Letsencrypt_)

Please follow the instructions to install the development version.
Do not forget the submodule update command.

.. _development:
    https://github.com/spesmilo/electrum#development-version-git-clone

.. _Letsencrypt:
    https://letsencrypt.org/


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

   electrum -o setconfig ssl_keyfile /path/to/ssl/privkey.pem

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

   electrum -o setconfig ssl_certfile /path/to/ssl/fullchain.pem


Check that your SSL certificate correctly configured:

.. code-block:: bash

   electrum -o get_ssl_domain


Configure your full hostname and port:

.. code-block:: bash

   electrum -o setconfig payserver_address ecdsa.org:80


Start the Electrum daemon
-------------------------

Once your read-only wallet is (re-)created, start Electrum as a daemon:

.. code-block:: bash

   electrum daemon -d
   electrum daemon load_wallet


Note: to stop the daemon

.. code-block:: bash

   electrum stop


Create a signed payment request
-------------------------------

.. code-block:: bash

   electrum add_request 0.5 -m "test"
   {
    "URI": "bitcoin:bc1qyr5xx5jkue3k72sldm5xa0taqs3n2achupymz8?amount=0.5&message=test&time=1589115653&exp=3600",
    "address": "bc1qyr5xx5jkue3k72sldm5xa0taqs3n2achupymz8",
    "amount": 50000000,
    "amount_BTC": "0.5",
    "bip70_url": "https://ecdsa.org:80/bip70/bc1qyr5xx5jkue3k72sldm5xa0taqs3n2achupymz8.bip70",
    "exp": 3600,
    "id": "6988b80931",
    "memo": "test",
    "status": 0,
    "status_str": "Expires in about 1 hour",
    "time": 1589115653,
    "type": 0,
    "view_url": "https://ecdsa.org:80/r/pay?id=bc1qyr5xx5jkue3k72sldm5xa0taqs3n2achupymz8"
   }

This command returns a json object with two URLs:

 - bip70_url is the URL of the signed BIP70 request.
 - view_url is the URL of a webpage displaying the request.

You can view the current list of requests using the 'list_requests'
command. You can clear the list using 'clear_requests'.

Open the payment request page in your browser
---------------------------------------------

Let us open index_url in a web browser.

.. image:: png/payrequest.png

The page shows the payment request. You can open the
bitcoin: URI with a wallet, or scan the QR code. The bottom
line displays the time remaining until the request expires.

.. image:: png/payreq_window.png


The page will update itself when the payment is received, using websockets.


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

   curl --data-binary '{"jsonrpc":"2.0","id":"curltext","method":"getbalance","params":[]}' http://username:password@127.0.0.1:7777

Query with named parameters:

.. code-block:: bash

   curl --data-binary '{"jsonrpc":"2.0","id":"curltext","method":"listaddresses","params":{"funded":true}}' http://username:password@127.0.0.1:7777

Create a payment request:

.. code-block:: bash

   curl --data-binary '{"jsonrpc":"2.0","id":"curltext","method":"addrequest","params":{"amount":"3.14","memo":"test"}}' http://username:password@127.0.0.1:7777
