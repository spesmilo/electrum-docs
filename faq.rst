Frequently Asked Questions
==========================


How does Electrum work?
-----------------------

Electrum's focus is speed, with low resource usage and
simplifying Bitcoin. Startup times are instant because it
operates in conjunction with high-performance servers that
handle the most complicated parts of the Bitcoin system.

Does Electrum trust servers?
----------------------------

In short, not really. The Electrum client never sends private keys
to the servers. In addition, it verifies the information
reported by servers, using a technique called :ref:`Simple Payment Verification <spv>`

By default, Electrum tries to maintain connections to ~10 servers.
The client subscribes to block header notifications to all of these,
and also periodically polls each for dynamic fee estimates.
For all connected servers except one, that is all they are used for.
Getting block headers from multiple sources is useful to detect lagging
servers, chain splits, and forks.

One of the servers, arbitrarily, is selected as the "main" server.

- The client subscribes to its own addresses (nit: sha256 hashes
  of scriptPubKeys) so that it would be notified of new transactions touching them.
  It also synchronizes the existing history of its addresses.
  This means the client sacrifices some privacy to the server, as the server
  can now reasonably guess that all these addresses belong to the same entity.

- As above, confirmed transactions are verified via SPV.

- The server is trusted about unconfirmed transactions.

- The server can lie by omission. That is, it can "forget" to mention
  (both confirmed and unconfirmed) transactions that are relevant to the client.

- All connected servers are polled for fee estimates, but whether those values
  are used depends on the "auto-connect" setting of the client.
  With "auto-connect" disabled, only the fee estimates sent by the main server are used.
  With "auto-connect" enabled, the client uses the median of all received fee estimates.
  In either case, low-high sanity limits are applied in the client.

- The main server is also used to broadcast the transactions the client makes.

- A list of server peers is also requested by the client, to learn about
  other servers it can use. (There is a list of hardcoded servers in the
  client to bootstrap)

Further, all of the connected servers will see the client's IP address
(which might be that of a proxy/VPN/Tor, if used).

The fast startup times and low resource usage is achieved at the cost of
the above detailed privacy loss. The protocol and the client is designed
in a way that minimises trust in the server.

Anyone can run a server. If you feel strongly about privacy,
or if SPV-security guarantees are not enough for you, you should
consider running your own Electrum server.


What is the seed?
-----------------

The seed is a random phrase that is used to generate your private
keys.

Example:

.. code-block:: none

   slim sugar lizard predict state cute awkward asset inform blood civil sugar

Your wallet can be entirely recovered from its seed. For this, select
the "I already have a seed" option in the wizard.

How secure is the seed?
-----------------------

The seed phrase created by Electrum has 132 bits of entropy. This
means that it provides the same level of security as a Bitcoin private
key (of length 256 bits). Indeed, an elliptic curve key of length n
provides n/2 bits of security.


I have forgotten my password. What can I do?
--------------------------------------------

It is not possible to recover your password. However, you can restore
your wallet from its seed phrase and choose a new password.
If you lose both your password and your seed, there is no way
to recover your money. This is why we ask you to save your seed
phrase on paper.

To restore your wallet from its seed phrase, create a new wallet, select
the type, choose "I already have a seed" and proceed to input your seed
phrase.


How does Electrum get the Bitcoin price it uses?
------------------------------------------------
Electrum gets the Bitcoin price from a third party, but provides
various options.  Please see menubar > `Tools` > `Preferences` > `Fiat`
to view the current setting or choose a new one.


My transaction has been unconfirmed for a long time. What can I do?
-------------------------------------------------------------------

Bitcoin transactions become "confirmed" when miners accept to write
them in the Bitcoin blockchain. In general, the speed of confirmation
depends on the fee you attach to your transaction; miners prioritize
transactions that pay the highest fees.

Recent versions of Electrum use "dynamic fees" in order to make sure
that the fee you pay with your transaction is adequate. This feature
is enabled by default in recent versions of Electrum.

If you have made a transaction that is unconfirmed, you can:

 - Wait for a long time. Eventually, your transaction will either be
   confirmed or cancelled. This might take several days.

 - Increase the transaction fee. This is only possible for
   "replaceable" transactions. To create this type of transaction, 
   you must have checked "Replaceable" on the send tab before sending
   the transaction. If you're not seeing the "Replaceable" option on 
   the send tab go to Tools menu > Preferences > Fees tab and set 
   "Propose Replace-By-Fee" to "Always". Transactions that are
   replaceable have the word "Replaceable" in the date column on the
   history tab. To increase the fee of a replaceable transaction right 
   click on its entry on the history tab and choose "Increase Fee". 
   Set an appropriate fee and click on "OK". A window will popup with 
   the unsigned transaction. Click on "Sign" and then "Broadcast".


 - Create a "Child Pays for Parent" transaction. A CPFP is a new
   transaction that pays a high fee in order to compensate for the
   small fee of its parent transaction. It can be done by the
   recipient of the funds, or by the sender, if the transaction has a
   change output. To create a CPFP transaction right click on the 
   unconfirmed transaction on the history tab and choose 
   "Child pays for parent". Set an appropriate fee and click on "OK". 
   A window will popup with the unsigned transaction. Click on "Sign"
   and then "Broadcast".


What does it mean to "freeze" an address in Electrum?
-----------------------------------------------------

When you freeze an address, the funds in that address will not be used
for sending bitcoins. You cannot send bitcoins if you don't have
enough funds in the non-frozen addresses.


How is the wallet encrypted?
----------------------------

Electrum uses two separate levels of encryption:

 - Your seed and private keys are encrypted using AES-256-CBC. The
   private keys are decrypted only briefly, when you need to sign a
   transaction; for this you need to enter your password. This is done
   in order to minimize the amount of time during which sensitive
   information is unencrypted in your computer's memory.

 - In addition, your wallet file may be encrypted on disk. Note that
   the wallet information will remain unencrypted in the memory of
   your computer for the duration of your session. If a wallet is
   encrypted, then its password will be required in order to open
   it. Note that the password will not be kept in memory; Electrum
   does not need it in order to save the wallet on disk, because it
   uses asymmetric encryption (ECIES).

Wallet file encryption is activated by default since version 2.8. It
is intended to protect your privacy, but also to prevent you from
requesting bitcoins on a wallet that you do not control.


Does Electrum support cold wallets?
-----------------------------------

Yes, see :ref:`Cold Storage <coldstorage>`.


Can I import private keys from other Bitcoin clients?
-----------------------------------------------------

In Electrum 2.0, you cannot import private keys in a wallet that has a
seed. You should sweep them instead.

If you want to import private keys and not sweep them, you need to
create a special wallet that does not have a seed.  For this, create a
new wallet, select "restore", and instead of typing your seed, type a
list of private keys, or a list of addresses if you want to create a
watching-only wallet.


.. image:: png/import_addresses.png


You will need to back up this wallet, because it cannot be
recovered from a seed.

Can I sweep private keys from other Bitcoin clients?
----------------------------------------------------


Sweeping private keys means to send all the bitcoins they control to
an existing address in your wallet. The private keys you sweep do not
become a part of your wallet.  Instead, all the bitcoins they control
are sent to an address that has been deterministically generated from
your wallet seed.

To sweep private keys, go to the Wallet menu -> Private Keys ->
Sweep. Enter the private keys in the appropriate field. Leave the
"Address" field unchanged. That is the destination address, and it will
be from your existing electrum wallet. Click on "Sweep". It'll now take 
you to the send tab where you can set an appropriate fee and then click
on "Send" to send the coins to your wallet.


.. _datadir:

Where is the Electrum datadir located?
--------------------------------------

The data directory of Electrum is where wallet files, config settings,
logs, blockchain headers, etc are stored.

On Windows:

- Show hidden files
- Go to \\Users\\YourUserName\\AppData\\Roaming\\Electrum (or %APPDATA%\\Electrum)

On Mac:

- Open Finder
- Go to folder (shift+cmd+G) and type ~/.electrum

On Linux:

- Home Folder
- Go -> Location and type ~/.electrum


Where is my wallet file located?
--------------------------------

The default wallet file is called default_wallet, which is created when
you first run the application and is located in the /wallets folder,
inside the :ref:`datadir <datadir>`.


How to enable debug logging?
----------------------------

1. Logging to file

   On Linux/Windows/macOS, you can enable logging to disk.
   Using the (Qt) GUI, go to menubar>Tools>Preferences>Misc,
   and tick "Write logs to file". After restarting Electrum,
   debug logs will be written to the :code:`logs/` folder inside the
   :ref:`datadir <datadir>`.

   If you encounter an error while opening a wallet and hence cannot
   get to "Preferences" to enable logging, as a workaround you can
   create a temporary throwaway wallet and access the settings there.

   Using CLI/RPC, you can enable file logging via e.g.:

   .. code-block:: none

       $ electrum setconfig log_to_file true

2. Logging to terminal (standard error)

   On Linux/macOS, if you start Electrum from terminal, you can specify
   the :code:`-v` flag, to enable debug logs in the terminal (to stderr).
   This option does not work on Windows (when using the binaries).

   On macOS, when using the official binary, try e.g.:

   .. code-block:: none

       $ /Applications/Electrum.app/Contents/MacOS/run_electrum -v


Can I do bulk payments with Electrum? (batching)
------------------------------------------------

You can create a transaction with several outputs. In the GUI, type
each address and amount on a line, separated by a comma.

.. image:: png/paytomany.png

Amounts are in the current unit set in the client. The
total is shown in the GUI.

You can also import a CSV file in the "Pay to" field, by clicking on
the folder icon.


Can Electrum create and sign raw transactions?
----------------------------------------------

Electrum lets you create and sign raw transactions right from the user
interface using a form.

Electrum freezes when I try to send bitcoins.
--------------------------------------------

This might happen if you are trying to spend a large number of
transaction outputs (for example, if you have collected hundreds of
donations from a Bitcoin faucet). When you send Bitcoins, Electrum
looks for unspent coins that are in your wallet in order to create a
new transaction. Unspent coins can have different values, much like
physical coins and bills.

If this happens, you should consolidate your transaction inputs by
sending smaller amounts of bitcoins to one of your wallet addresses;
this would be the equivalent of exchanging a stack of nickels for a
dollar bill.

.. _gap limit:

What is the gap limit?
----------------------

The gap limit is the maximum number of consecutive unused addresses in
your deterministic sequence of addresses. Electrum uses it in order
to stop looking for addresses. In Electrum 2.0, it is set to 20 by
default, so the client will get all addresses until 20 unused
addresses are found.


How can I pre-generate new addresses?
-------------------------------------

Electrum will generate new addresses as you use them,
until it hits the `gap limit`_.

If you need to pre-generate more addresses, you can do so by typing
wallet.create_new_address(False) in the console. This command will generate
one new address. Note that the address will be shown with a red
background in the address tab to indicate that it is beyond the gap
limit. The red color will remain until the gap is filled.

WARNING: Addresses beyond the gap limit will not automatically be
recovered from the seed. To recover them will require either increasing
the client's gap limit or generating new addresses until the used
addresses are found.


If you wish to generate more than one address, you can use a "for"
loop. For example, if you wanted to generate 50 addresses, you could
do this:

.. code-block:: python

   [wallet.create_new_address(False) for i in range(50)]


How do I upgrade Electrum?
--------------------------

Warning: always save your wallet seed on paper before
doing an upgrade.

To upgrade Electrum, just install the most recent version.
The way to do this will depend on your OS.

Note that your wallet files are stored separately from the
software, so you can safely remove the old version of the
software if your OS does not do it for you.

Some Electrum upgrades will modify the format of your
wallet files.

For this reason, it is not recommended to downgrade
Electrum to an older version once you have opened your
wallet file with the new version. The older version will
not always be able to read the new wallet file.


The following issues should be considered when upgrading
Electrum 1.x wallets to Electrum 2.x:

- Electrum 2.x will need to regenerate all of your
  addresses during the upgrade process. Please allow it
  time to complete, and expect it to take a little longer
  than usual for Electrum to be ready.

- The contents of your wallet file will be replaced with
  an Electrum 2 wallet. This means Electrum 1.x will no
  longer be able to use your wallet once the upgrade is
  complete.

- The "Addresses" tab will not show any addresses the
  first time you launch Electrum 2. This is expected
  behavior. Restart Electrum 2 after the upgrade is
  complete and your addresses will be available.

- Offline copies of Electrum will not show the
  addresses at all because it cannot synchronize with
  the network. You can force an offline generation of a
  few addresses by typing the following into the
  Console: wallet.synchronize(). When it's complete,
  restart Electrum and your addresses will once again
  be available.


.. _antivirus:

My anti-virus has flagged Electrum as malware! What now?
--------------------------------------------------------

Electrum binaries are often flagged by various anti-virus software.
There is nothing we can do about it, so please stop reporting that to us.
Anti-virus software uses heuristics in order to determine if a program
is malware, and that often results in false positives.

If you trust the developers of the project, you can verify
the GPG signature of Electrum binaries, and safely ignore any anti-virus
warnings.

If you do not trust the developers of the project, you should build the
binaries yourself, or run the software from source.

Finally, if you are really concerned about malware, you should not use an
operating system that relies on anti-virus software.


Electrum requires recent Python. My Linux distribution does not yet have it. What now?
--------------------------------------------------------------------------------------

There are several ways to resolve this.

1. Use the AppImage distributed by us. This is a single self-contained
   binary that includes all the dependencies.
   Currently, we only distribute this binary for x86_64 (amd64) architecture.
   Just download it, (verify GPG sig), make it executable, and run it. E.g.:

   .. code-block:: none

      $ wget https://download.electrum.org/3.3.4/electrum-3.3.4-x86_64.AppImage
      $ chmod +x electrum-3.3.4-x86_64.AppImage
      $ ./electrum-3.3.4-x86_64.AppImage


2. Use backports (e.g. in case of Debian, check the packages in stable-backports)

3. Upgrade your distribution (e.g. use Debian testing instead of stable)

4. Compile Python yourself, and then install pyqt5 using pip (as the package
   manager for the distribution will only have PyQt5 for the version of
   Python that is packaged by them).

   .. code-block:: none

      $ python3 -m pip install --user pyqt5

   (Unfortunately, it seems pyqt5 via pip is only available for x86/x86_64.
   On other archs, you might have to build Qt/PyQt yourself.)

5. Use a virtual machine where you run another Linux distribution that has
   more recent packages.


I might run my own server. Are client-server connections authenticated?
-----------------------------------------------------------------------

Electrum uses a client-server architecture, where the endpoints speak the
Electrum protocol. The Electrum protocol is JSON-RPC based.
The two main stacks the client supports are

1. JSON-RPC over SSL/TLS over TCP

2. JSON-RPC over TCP

Note that neither option uses HTTP.

The client only connects to servers over SSL (so plaintext TCP is not used).
Prior to Electrum 3.1, there used to be a checkbox in the GUI to toggle this
but it was removed.

As for authentication, the client accepts both CA-signed certificates and self-signed
SSL certificates. When it first connects to a server, it pins the fact whether that
server is using a CA-signed or a self-signed cert.

- If it is self-signed, it will only accept that cert until it expires for that server (TOFU).

- If it is CA signed, it will forever only accept CA-signed certs for that server.

For your own server, both CA-signed and self-signed certs have their advantages.

- With self-signed certs, as the client uses TOFU, there is a possibility of
  man-in-the-middle during the first connection.

- With CA-signed certs, you need to trust the Certificate Authorities.


Does Electrum support altcoins ("cryptocurrencies")?
----------------------------------------------------

No. Electrum only supports Bitcoin.

The project has never supported any altcoins, only Bitcoin. However Electrum
is free (as in freedom) software with a permissive license, and there are many
forks of the software that support specific altcoins. These are separate projects,
with their own maintainers, independent of Electrum. We do not review their code
or endorse them in any way. If you are a user of these, please direct any and all
support requests to their maintainers, instead of us.
