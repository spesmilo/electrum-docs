How To Use
==========

Encrypting a secret is a simple four step process.

1. `Enable the plugin`_
2. `Create or load a Revealer`_
3. `Encrypt your secret`_
4. `Test your backup`_


Enable the plugin
-----------------

Revealer plugin is included with Electrum Bitcoin Wallet since version 3.2.
Start Electrum, go to the menu ‘Tools->Plugins’, and activate the Revealer
plugin.

.. image:: /png/revealer/enable-plugin.png
  :alt: Electrum plugins window with Revealer plugin enabled

After restarting Electrum, the revealer icon is shown in the main window status
bar.

.. image:: /png/revealer/electrum-gui-with-revealer.png
  :alt: Electrum main window with Revealer plugin icon


Create or load a Revealer
-------------------------

Click the Revealer icon to open the setup dialog. Click "Create a new Revealer"
or enter the code of an existing Revealer.

.. image:: /png/revealer/setup.png
  :alt: Revealer setup dialog window

When creating a new Revealer, the path to the new PDF and PNG will be shown.


Encrypt your secret
-------------------

Click next on the Revealer setup window. Choose to encrypt your current wallet's
seed or enter a secret in the text area.

.. image:: /png/revealer/encrypt.png
  :alt: Revealer encrypt dialog window

The path to your encrypted secret PDF and PNG will be shown.

Print the Revealer and Secret
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Open the Revealer and Secret PDFs and print them out.

.. image:: /png/revealer/print.png
  :alt: Electrum dialog window showing the path to the newly encrypted secret

Test your backup
----------------

Make sure you test that your backups work by printing and overlaying them to
reveal the encrypted secret.

.. image:: /png/revealer/one_card_revealer_zero_perspective_transparent.png
  :alt: Sample Revealer and Secret overlayed on each other
