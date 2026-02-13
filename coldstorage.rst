.. _coldstorage:

Cold Storage
============

This document shows how to create an offline wallet that
holds your Bitcoins and a watching-only online wallet that
is used to view its history and to create transactions that
have to be signed with the offline wallet before being
broadcast on the online one.


Create an offline wallet
------------------------

Create a wallet on an offline machine, as per the usual process (file
-> new) etc.

After creating the wallet, go to Wallet -> Information.

.. image:: png/wallet_info.png

The Master Public Key of your wallet is the string shown in this popup
window.  Transfer that key to your online machine somehow.


Create a watching-only version of your wallet
---------------------------------------------

On your online machine, open up Electrum and select File ->
New/Restore. Enter a name for the wallet and select "Standard wallet".

.. image:: png/standard_wallet.png

Select "Use public or private keys"

.. image:: png/public_or_private.png

Paste your master public key in the box.

.. image:: png/restore_key.png

Click Next to complete the creation of your wallet. 
When you're done, you should see a popup informing you that you are opening a watching-only wallet.

.. image:: png/watchingonly.png

Then you should see the transaction history of your cold wallet.

Create an unsigned transaction
------------------------------

Go to the "Send" tab on your online watching-only wallet,
input the transaction data and press "Preview". A window pops up:

.. image:: png/unsigned.png


Press "Export" to save the transaction to a file on your computer.

.. note::
   In newer versions of Electrum, the "Save" button stores the
   transaction locally in the wallet file. To export the transaction
   to a file for transfer, use the "Export" button instead.

Close the window and transfer the transaction file to your offline
machine (e.g. with a USB stick).

Get your transaction signed
---------------------------

On your offline wallet, select Tools -> Load transaction -> From file
in the menu and select the transaction file created in the previous
step.

.. image:: png/sign.png

Press "Sign". Once the transaction is signed, the Transaction ID
appears in its designated field.

.. image:: png/signed.png

Press "Export" to save the signed transaction to a file on your
computer, and transfer it back to your online machine.

Broadcast your transaction
--------------------------


On your online machine, select Tools -> Load transaction -> From File
from the menu. Select the signed transaction file. In the window that
opens up, press "Broadcast". The transaction will be broadcast over
the Bitcoin network.

