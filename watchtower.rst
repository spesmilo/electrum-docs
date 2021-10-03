How to setup a watchtower
=========================

This tutorial will show you how to configure your Electrum daemon as a
watchtower for your lightning wallet.  It is written for Electrum 4.0.

A watchtower is a separate Electrum process, that runs on
another computer. To setup a watchtower, you need to configure
an Electrum daemon, and enter its URL in your preferences.



How to configure a watchtower
-----------------------------

You want to run your watchtower on a machine that is regularly
connected to the internet.

First install Electrum, and add a SSL certificate to your Electrum
configuration:

.. code-block:: bash

   electrum -o setconfig ssl_keyfile /path/to/ssl/privkey.pem
   electrum -o setconfig ssl_certfile /path/to/ssl/fullchain.pem

For details see `How to add SSL <ssl.html>`_


Second, configure your watchtower with an address, username and password:

.. code-block:: bash

    electrum setconfig -o run_watchtower true
    electrum setconfig -o watchtower_user myusername
    electrum setconfig -o watchtower_password mypassword
    electrum setconfig -o watchtower_address example.com:12345

Then start the daemon:

.. code-block:: bash

    electrum daemon -d


The watchtower database contains presigned transactions, and is in
~/.electrum/watchtower_db


Note that the daemon does not need to contain a wallet, nor to have
Lightning enabled; the watchtower is only about watching onchain
addresses and broadcasting onchain transactions.


If you run Electrum's Qt GUI on the machine that is configured as a
watchtower, you can view the database size and number of transactions
per channel if you open the watchtower window:

.. image:: png/watchtower_window.png


Configure the watchtower in your client
---------------------------------------

In your client preferences, tick 'use a remote watchtower' and enter the url:

.. code-block:: bash

    https://myusername:mypassword@example.com:12345
