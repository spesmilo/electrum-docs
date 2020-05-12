How to setup a watchtower
=========================

This tutorial will show you how to configure your Electrum daemon as a
watchtower for your lightning wallet.  It is written for Electrum 4.0
(currently in development_)

.. _development:
    https://github.com/spesmilo/electrum#development-version-git-clone

Add your SSL certificate to Electrum
------------------------------------

To protect against MITM attacks, add a SSL certificate:

.. code-block:: bash

   electrum -o setconfig ssl_keyfile /path/to/ssl/privkey.pem
   electrum -o setconfig ssl_certfile /path/to/ssl/fullchain.pem

For details see `How to add SSL <ssl.html>`_


Configure your Watchtower
-------------------------

Configure your watchtower address and password:

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


Configure the watchtower in your client
---------------------------------------

In your client preferences, tick 'use a remote watchtower' and enter the url:

.. code-block:: bash

    https://myusername:mypassword@example.com:12345
