How to setup a watchtower
=========================

This tutorial will show you how to configure your Electrum daemon as a
watchtower for your lightning wallet.  It is written for Electrum 4.0.


Local and remote watchtower
---------------------------

There are two ways a watchtower can be configured in Electrum: Local
or Remote.

A local watchtower runs in the same process as your Electrum client,
and can be activated in the preferences dialog of the Qt GUI. A local
watchtower creates a database of pre-signed breach remedy
transactions, and it watches the funding addresses of your
channels. When your lightning wallet is open, breach remedy
transactions will be signed and added to the watchtower database.
Once you your wallet is closed, assuming Electrum is still running,
the local watchtower will watch your channels, and it will broadcast
pre-signed breach remedy transactions if needed.

A remote watchtower is a separate Electrum process, that runs on
another computer. To setup a remote watchtower, you need to configure
an Electrum daemon, and to enter its URL in your preferences.


How to configure a local watchtower
------------------------------------

In your preferences, check 'Run a local watchtower'

.. image:: png/watchtower_settings.png


The second option ensures that Electrum keeps running on your computer
after you have closed your wallet file. If you click it, the Electrum
icon should persist in your taskbar after you have closed all your
Electrum windows.


If you have open channels and a local watchtower, Electrum will
populate the watchtower database.  You can view the database size and
number of transactions per channel if you open the watchtower window:

.. image:: png/watchtower_window.png


How to configure a remote watchtower
------------------------------------

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

    electrum setconfig -o run_local_watchtower true
    electrum setconfig -o watchtower_user myusername
    electrum setconfig -o watchtower_password mypassword
    electrum setconfig -o watchtower_address example.com:12345

Then start the daemon:

.. code-block:: bash

    electrum daemon -d


The watchtower database contains presigned transactions, and is in
~/.electrum/watchtower_db If you open the GUI you can see hown many
channels and transactions are in the database.

Note that the daemon does not need to contain a wallet, nor to have
Lightning enabled; the watchtower is only about watching onchain
addresses and broadcasting onchain transactions.

Configure the watchtower in your client
---------------------------------------

In your client preferences, tick 'use a remote watchtower' and enter the url:

.. code-block:: bash

    https://myusername:mypassword@example.com:12345
