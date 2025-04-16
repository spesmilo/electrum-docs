How to offer Submarine Swaps
============================

Electrum allows users to move bitcoin between their Lightning and on-chain balance in a trustless way,
this is called Submarine Swaps. It allows the user, for example, to add incoming liquidity to
their lightning channel or to add funds to their lightning balance without having to open additional channels.

In order for the client to execute a swap, it needs a counterparty to execute the swap with.
This counterparty, hereafter referred to as the swap server, can be operated by anyone
in order to earn fees for the liquidity it provides to its customers.

Swap server setup
-----------------
A swap server is supposed to be operated as a continuously running daemon, so the first step is to
acquire some linux server that can be online for prolonged time. This can be a simple VPS, a Raspberry Pi
or an old notebook. The swap server requires **no** port forwarding, so it can be run easily behind a firewall or
consumer internet connection without open ports.

Once you have access to the host shell the swap server can be setup using the following steps:

1. **Download Electrum:**

The swap server is part of the regular Electrum application, you can either
`run from source <https://github.com/spesmilo/electrum#development-version-git-clone>`_
or get the binary:

.. code-block:: bash

    wget https://download.electrum.org/CURRENT_VERSION/electrum-CURRENT_VERSION-x86_64.AppImage

Then make the binary executable with:

.. code-block:: bash

    chmod +x electrum-CURRENT_VERSION-x86_64.AppImage

.. note::
    Replace *CURRENT_VERSION* with the latest version number, e.g. 4.6.0, which you can find on
    `electrum.org <https://electrum.org/#download>`_.

    | If you use the **AppImage**:
    | Replace ``./run_electrum`` with ``./electrum-CURRENT_VERSION-x86_64.AppImage``
    | in all following commands.

.. caution::

    | You may want to verify the authenticity of the downloaded binary.
    | To do so refer, to the following guide:
    | `Verifying GPG signature of Electrum using Linux command line <gpg-check.html>`_

2. **Start Electrum as daemon:**

Now start an instance of Electrum as daemon.
The option ``-d`` will start it in detached mode (in the background):

.. code-block:: bash

    ./run_electrum daemon -d
    ---> starting daemon (PID 42836)

This will create a directory called ``~/.electrum`` in your home directory,
which contains the configuration and wallet files.

3. **Create a wallet:**

Now we need to create a new wallet that will be used for the swap server.
Optionally you could also import an existing Electrum seed.

.. code-block:: bash

    ./run_electrum create
    --->
        {
            "msg": "Please keep your seed in a safe place; if you lose it, you will not be able to restore your wallet.",
            "path": "/home/user/.electrum/wallets/default_wallet",
            "seed": "obey wash exit have spice fitness dumb debate shrimp risk grief coral"
        }

As always, write down your `seed` in a safe place and do not share it with anyone.

4. (OPTIONAL) **Encrypt wallet keystore:**

It is possible to encrypt the wallet keystore, this is the part in the database that contains the private keys.
It is a good measure to increase the security of your swap server private keys.

.. code-block:: bash

    # always set --encrypt_file False
    # otherwise DB performance may be too low for swap server operation
    ./run_electrum password --new_password <new_password> --encrypt_file False

.. caution::

    If you set a keystore password you have to unlock it every time you load the wallet, otherwise
    the swap server will not be able to sign transactions. See the unlock command in the following step.

5. **Load the wallet:**

To activate the newly created wallet, it has to be loaded:

.. code-block:: bash

    ./run_electrum load_wallet

    # if you set a password for the keystore, unlock it
    ./run_electrum unlock --password <your password>

6. **Enable logging into files:**

Logging can be useful to monitor your swap server and debug potential issues.
Enable logging into files using the following command:

.. code-block:: bash

    ./run_electrum setconfig log_to_file True
    ./run_electrum setconfig logs_num_files_keep 100

By default the log files will be stored in ``~/.electrum/logs/electrum_log_*.log``

7. (OPTIONAL) **Enable gossip:**

By default Electrum uses Trampoline routing to find a path for lightning payments as
this provides better user experience. However, as the swap server is a long running daemon, we can
enable gossip to fetch the lightning network gossip and find paths locally:

.. code-block:: bash

    ./run_electrum setconfig use_gossip True

    # now restart electrum to apply the changes
    ./run_electrum stop
    ./run_electrum daemon -d
    ---> starting daemon (PID 42836)
    ./run_electrum load_wallet

    # with keystore encryption:
    ./run_electrum unlock --password <your password>

This will allow you to open lightning channels to any other node instead of just the following hardcoded
`trampoline nodes <https://github.com/spesmilo/electrum/blob/c0ddce458602b4ebccbbb7fe06c73c5d7841c98e/electrum/trampoline.py#L22>`_.

8. **Funding the swap server:**

To become a useful swaps provider you need to have on-chain funds as well as balanced lightning
channels on your electrum node. This process varies depending on your available funds and strategy.

The following commands are useful in the process of funding the swap server:

.. code-block:: bash

    # check the balance of the swap server
    ./run_electrum getbalance

    # get new onchain address
    ./run_electrum getunusedaddress

    # open a lightning channel
    ./run_electrum open_channel <connection string> <amount>

    # list lightning channels
    ./run_electrum list_channels

At this point it may be useful to have a look at all available commands:

.. code-block:: bash

    # to show all available commands
    ./run_electrum help

    # to show help for a specific command
    ./run_electrum open_channel -h

Refer to the `Command Line documentation <cmdline.html>`_ for a more detailed overview of the
command line functionality of the Electrum daemon.

.. note::
    Lightning channels in Electrum can be force closed just with your seed backup, so you don't have
    to worry about any other backup than the seed words.

9. **Enabling the swap server:**

Now that you have a funded and well balanced Electrum lightning node we can enable the swap server plugin:

.. code-block:: bash

    # this will enable the swap server plugin, it will automatically start when the daemon is started
    ./run_electrum setconfig plugins.swapserver.enabled True

    # now restart the daemon again to apply the changes
    ./run_electrum stop
    ./run_electrum daemon -d
    ---> starting daemon (PID 42836)
    ./run_electrum load_wallet

    # with keystore encryption:
    ./run_electrum unlock --password <your password>

On the first restart you may notice some CPU load as the swap server will calculate some Proof of Work
for spam protection. This is a one time process and will not be repeated on subsequent restarts unless you change
it's target configuration. This can take a couple of minutes depending on the hardware, please be patient.

.. note::
    Now if you run a regular Electrum Wallet and open the Submarine Swap dialog you should be able to see your
    new swap server in the list of available swap servers.
    Now all users of Electrum can use your swap server to do submarine swaps.

    .. image:: png/swap_providers.png

10. **Configure the swap server:**

The following configuration options are available for the swap server:

.. code-block:: bash

    # fee_millionths: fee charged for swaps, default is 5000
    ./run_electrum setconfig plugins.swapserver.fee_millionths <value>

    # swapserver_pow_target: announcement proof of work target, default is 30
    # a higher value ranks you higher in the clients GUI, 35 already can take hours to find,
    # depending on the hardware
    ./run_electrum setconfig swapserver_pow_target <value>

    # nostr_relays: comma separated nostr relay urls your swap server uses for communication
    # and self-announcement. Default: see file electrum/simple_config.py
    ./run_electrum setconfig nostr_relays <csv string>

.. note::
    The configuration variables can also be set manually using a text editor instead of the above CLI commands.
    By default the configuration file located at ``~/.electrum/config``.

    To see all available configuration options you can have a look at the ``electrum/simple_config.py``
    file in the Electrum source code repository.

Operation
----------

To stay competitive in the market of swap providers you should keep an eye on your lightning channels
liquidity and on-chain balance to ensure you can provide swaps in both directions to your users.
Also make sure you always run the latest release of Electrum to benefit from the
latest features and bug fixes.

Shutting down
-------------
To shut down the swap server you can gracefully stop the daemon using:

.. code-block:: bash

    ./run_electrum stop