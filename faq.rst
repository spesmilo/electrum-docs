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

Not really; the Electrum client never sends private keys
to the servers. In addition, it verifies the information
reported by servers, using a technique called :ref:`Simple Payment Verification <spv>`

What is the seed?
-----------------

The seed is a random phrase that is used to generate your private
keys.

Example:

.. code-block:: none

   slim sugar lizard predict state cute awkward asset inform blood civil sugar

Your wallet can be entirely recovered from its seed. For this, select
the "restore wallet" option in the startup.

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
"Address" field unchanged. That is the destination address and it will
be from your existing electrum wallet. Click on "Sweep". It'll now take 
you to the send tab where you can set an appropriate fee and then click
on "Send" to send the coins to your wallet.

Where is my wallet file located?
--------------------------------

The default wallet file is called default_wallet, which is created when
you first run the application and is located in the /wallets folder.

On Windows:

 - Show hidden files
 - Go to \\Users\\YourUserName\\AppData\\Roaming\\Electrum\\wallets (or %APPDATA%\\Electrum\\wallets)

On Mac:

- Open Finder
- Go to folder (shift+cmd+G) and type ~/.electrum

On Linux:

- Home Folder
- Go -> Location and type ~/.electrum


Can I do bulk payments with Electrum?
-------------------------------------

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
   Currently we only distribute this binary for x86_64 (amd64) architecture.
   Just download it, (verify GPG sig), make it executable, and run it. E.g.:

   .. code-block:: none

      wget https://download.electrum.org/3.3.4/electrum-3.3.4-x86_64.AppImage
      chmod +x electrum-3.3.4-x86_64.AppImage
      ./electrum-3.3.4-x86_64.AppImage


2. Use backports (e.g. in case of Debian, check the packages in stable-backports)

3. Upgrade your distribution (e.g. use Debian testing instead of stable)

4. Compile Python yourself, and then install pyqt5 using pip (as the package
   manager for the distribution will only have PyQt5 for the version of
   Python that is packaged by them).

   .. code-block:: none

      python3 -m pip install --user pyqt5

   (Unfortunately it seems pyqt5 via pip is only available for x86/x86_64.
   On other archs, you might have to build Qt/PyQt yourself.)

5. Use a virtual machine where you run another Linux distribution that has
   more recent packages.

