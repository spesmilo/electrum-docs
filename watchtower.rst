How to set up a watchtower
==========================

This tutorial shows how to configure an Electrum 4.8.4 daemon as a
watchtower for your Lightning wallet.

A watchtower is a separate Electrum process, typically running on another
computer. Configure the daemon, then enter its URL in your wallet preferences.



How to configure a watchtower
-----------------------------

You want to run your watchtower on a machine that is regularly
connected to the internet.

Install Electrum. With the daemon stopped, enable the watchtower plugin and
set its port and credentials:

.. code-block:: bash

    electrum -o setconfig plugins.watchtower.enabled true
    electrum -o setconfig plugins.watchtower.server_user myusername
    electrum -o setconfig plugins.watchtower.server_password mypassword
    electrum -o setconfig plugins.watchtower.server_port 12345

Then start the daemon:

.. code-block:: bash

    electrum daemon -d


The plugin listens on localhost only. To connect from a separate device, run an
HTTPS reverse proxy on the watchtower machine and forward requests to
``http://127.0.0.1:12345``, preserving the HTTP authorization header. Use the
proxy's public hostname and port in the wallet URL.

The watchtower database is named ``watchtower_db`` in the Electrum data
directory. It contains presigned transactions.


Note that the daemon does not need to contain a wallet, nor to have
Lightning enabled; the watchtower is only about watching onchain
addresses and broadcasting onchain transactions.


Configure the watchtower in your client
---------------------------------------

With the wallet's Electrum daemon stopped, set ``watchtower_url`` on the
client. For the HTTPS proxy in this example, use:

.. code-block:: bash

    electrum -o setconfig watchtower_url 'https://myusername:mypassword@example.com/'

Restart the client after setting the URL. To test a watchtower from a wallet
on the same machine, use ``http://myusername:mypassword@127.0.0.1:12345``.
