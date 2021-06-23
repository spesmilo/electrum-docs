Plugins
=======

The plugin system of Electrum is designed to allow the development of new features without increasing the core code of Electrum. To enable or disable Plugins, see menubar > `Tools` > `Plugins`. 

Below you can find a short description of each available tool.


Audio Modem
-----------

Provides support for air-gapped transaction signing.
requires 'amodem' python package http://github.com/romanz/amodem/


Cosigner Pool
-------------

This plugin facilitates the use of multi-signatures wallets. It sends and receives partially signed transactions from/to your cosigner wallet. Transactions are encrypted and stored on a remote server.


Email	
-----

Send and receive payment request with an email account
keys.


LabelSync
---------

Save your wallet labels on a remote server, and synchronize them across multiple devices where you use Electrum. Labels, transactions IDs and addresses are encrypted before they are sent to the remote server.


Revealer
--------

This plug-in allows you to create a visually encrypted backup of your wallet seeds, or of custom alphanumeric secrets.

.. toctree::
  :maxdepth: 1
  :glob:

  revealer/how_to_use
  revealer/how_it_works
  revealer/faq


Two Factor Authentication
-------------------------

This plugin adds two-factor authentication to your wallet.
For more information, visit https://api.trustedcoin.com/#/electrum-help



Virtual Keyboard
----------------

Add an optional virtual keyboard to the password dialog.
Warning: do not use this if it makes you pick a weaker password.
