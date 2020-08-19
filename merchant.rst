How to accept Bitcoin on a website using Electrum
=================================================

This tutorial will show you how to accept Bitcoin on a website with
SSL signed payment requests, according to BIP-70_. The docs are
updated for Electrum 4.0 (currently in development_).

.. _BIP-70:
    https://github.com/bitcoin/bips/blob/master/bip-0070.mediawiki

You will need a valid SSL certificate (signed by a CA, for example
free Letsencrypt_).  Please follow the instructions to install the
development version.  Do not forget the submodule update command.


.. _development:
    https://github.com/spesmilo/electrum#development-version-git-clone

.. _Letsencrypt:
    https://letsencrypt.org/


Add your SSL certificate to Electrum
------------------------------------

.. code-block:: bash

   electrum -o setconfig ssl_keyfile /path/to/ssl/privkey.pem
   electrum -o setconfig ssl_certfile /path/to/ssl/fullchain.pem

For details see `How to add SSL <ssl.html>`_


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


Lightning payments
------------------

To use lightning, you need to initialize lightning keys in your wallet.
You will need to restart the daemon after that, or to stop it before:

.. code-block:: bash

   electrum stop
   electrum -o init_lightning
   electrum daemon -d

Note that it is possible to add lightning keys to a watching-only
wallet.  That wallet will not be able to spend coins onchain, but it
will be able to perform lightning transactions.

The next thing you will need to do is open a channel:

.. code-block:: bash

   electrum open_channel <node_id> <amount>

Wait until it is ready to be used:

.. code-block:: bash

   electrum list_channels

You will not immediately be able to receive with that channel, because
it does not have inbound capacity. If you need to be able to receive
immediately, you may do a submarine swap of your channel funds.

To create a lightning payment request:

.. code-block:: bash

   electrum add_lightning_request 0.0001 -m "test"
