Using Electrum from Python directly
===================================

Electrum itself is a wallet, mostly used from it's graphical interface.
But in some cases you don't want to install bitcoin node for your project,
or if you just like using electrum and want your project and
your wallet to always be consistent.

Electrum is written in python, and this section will show how to understand
electrum code and how to use it from python(not console in GUI,
but as a python module).

This is an advanced topic, continue only if you know what you're doing.

Electrum is written as a python package, so if you have installed
electrum with pip, like so:

.. code-block:: sh

    pip3 install Electrum-X.Y.Z.tar.gz

Then you can use it as a package.
To import electrum in python, just ``import electrum``!

Electrum commands structure
---------------------------

Have you ever tried electrum console commands?
They are run like ``electrum command_name``
For example, ``electrum help`` would list all available commands.

How are those commands generated? Where is this code?
Open electrum source code at `github <https://github.com/spesmilo/electrum>`_
and find ``electrum/commands.py`` `file <https://github.com/spesmilo/electrum/blob/master/electrum/commands.py>`_.

This is the source code for all CLI commands.

Commands class contains all commands, and each command is marked with
``@command('')`` decorator
The function name is used as CLI(and also JSON-RPC) method name.
The function arguments, if any, are converted to command line arguments.
The '' string passed to @command decorator is short description of the method.

- ``n`` means command requires network,

- ``w`` means command requires wallet, and

- ``p`` means command requires password

The python code inside those functions is executed upon
CLI or JSON-RPC method call.

The functions which have ``wallet_path`` argument recieve loaded wallet
path from daemon(``daemon.py``), or None when wallet is not used.

All those commands are methods of Commands class.
Commands class has all the objects needed to perform some actions.
Commands object accepts config(required), network and daemon.
Network object is from ``network.py``, daemon object is from ``daemon.py``
config object is from ``simple_config.py``.

So, to create Commands object, you would have to do something like that (differs from release to release):

.. code-block:: python

    from electrum.daemon import Daemon
    from electrum.simple_config import SimpleConfig
    from electrum.commands import Commands
    from electrum.util import create_and_start_event_loop
    loop, stop_loop, loop_thread = create_and_start_event_loop()
    config = SimpleConfig()
    daemon = Daemon(config, listen_jsonrpc=False)
    network = daemon.network
    commands = Commands(config=config, network=network, daemon=daemon)

    async def main():
        print(await commands.help())
    loop.create_task(main())

The result would be like so:

.. code-block:: python

    >>> loop.create_task(main())
    <Task pending coro=<main() running at <stdin>:1>>
    >>> ['add_lightning_request', 'add_peer', 'add_request', 'addtransaction', 'broadcast', 'clear_invoices', 'clear_ln_blacklist', 'clear_requests', 'close_channel', 'close_wallet', 'commands', 'convert_xkey', 'create', 'createmultisig', 'createnewaddress', 'decrypt', 'deserialize', 'dumpgraph', 'dumpprivkeys', 'encrypt', 'freeze', 'get', 'get_channel_ctx', 'get_tx_status', 'getaddressbalance', 'getaddresshistory', 'getaddressunspent', 'getalias', 'getbalance', 'getconfig', 'getfeerate', 'getinfo', 'getmasterprivate', 'getmerkle', 'getmpk', 'getprivatekeys', 'getpubkeys', 'getrequest', 'getseed', 'getservers', 'gettransaction', 'getunusedaddress', 'help', 'importprivkey', 'inject_fees', 'is_synchronized', 'ismine', 'lightning_history', 'list_channels', 'list_invoices', 'list_requests', 'list_wallets', 'listaddresses', 'listcontacts', 'listunspent', 'lnpay', 'load_wallet', 'make_seed', 'nodeid', 'notify', 'onchain_history', 'open_channel', 'password', 'payto', 'paytomany', 'removelocaltx', 'restore', 'rmrequest', 'searchcontacts', 'serialize', 'setconfig', 'setlabel', 'signmessage', 'signrequest', 'signtransaction', 'stop', 'sweep', 'unfreeze', 'validateaddress', 'verifymessage', 'version']

To view the most recent version of how to create Commands object, view `this file <https://github.com/spesmilo/electrum/blob/master/electrum/scripts/quick_start.py>`_


``loop, stop_loop, loop_thread = create_and_start_event_loop()`` line starts event loop to run electrum commands, they are asynchronous.

So, to run those commands you should run them from an async function.
They are defined with ``async def``.

We use ``loop.create_task(main())`` to start task in background.

Note that network and daemon creating is optional, then commands
would be run in offline mode.

So, to run a command, just call
``await commands.command_name()`` function, for example

.. code-block:: python

    print(await commands.help())

Wallet object
-------------

But how to use a wallet with those functions?
Well, just create a Wallet object.
Actually to run a command you don't need Wallet object, but it
contains other methods you might use.

.. code-block:: python

    from electrum.wallet import Wallet
    from electrum.storage import storage

    storage = Storage("wallet path here")
    wallet = Wallet(storage, config=config)
    wallet.start_network(network) # if you need network

But to use the wallet in commands you just need wallet path.
Wallet path is got as ``wallet.storage.path`` if you created wallet object or as ``config.get_wallet_path()``.

.. code-block:: python

    wallet_path = config.get_wallet_path()

Before running commands with new wallet,
if you have passed daemon to Commands class,
then you should also add wallet to the daemon.
Daemon is like a manager of your wallets.
So, run:

.. code-block:: python

    daemon.add_wallet(wallet)

To add it.

So, to run a command that requires wallet just pass ``wallet_path``
to that command, for example:

.. code-block:: python

    await commands.getbalance(wallet_path=wallet_path)

Where are the default servers read from?
----------------------------------------

For mainnet, it reads ``electrum/servers.json`` file, for testnet
``electrum/servers_testnet.json``.
For regtest it uses local electrumx install.
