Plugins
=======

The plugin system of Electrum is designed to allow the development of new features without increasing the core code of Electrum. There are two types of plugins, **internal** and **external** plugins.

To enable or disable Plugins, see **Menu Bar** > **Tools** > **Plugins**.


Internal Plugins
----------------

Internal Plugins are shipped with Electrum and maintained in the Electrum repository.

Below you can find a short description of each integrated Tool.


Audio Modem
^^^^^^^^^^^

Provides support for air-gapped transaction signing.
requires 'amodem' python package http://github.com/romanz/amodem/


LabelSync
^^^^^^^^^

Save your wallet labels on a remote server, and synchronize them across multiple devices where you use Electrum. Labels, transactions IDs and addresses are encrypted before they are sent to the remote server.


Nostr Wallet Connect
^^^^^^^^^^^^^^^^^^^^

This plugin allows remote control of Electrum lightning wallets via Nostr NIP-47 (Nostr Wallet Connect). A connection string with daily budget and expiry date can be created from the Desktop GUI as well as the command line and then used in Nostr apps like browser extensions or social media clients.


PSBT over Nostr
^^^^^^^^^^^^^^^

This plugin facilitates the use of multi-signatures wallets. It sends and receives partially signed transactions from/to your cosigner wallet. PSBTs are sent and retrieved encrypted using Nostr relays.


Revealer
^^^^^^^^

This plug-in allows you to create a visually encrypted backup of your wallet seeds, or of custom alphanumeric secrets.


Two Factor Authentication
^^^^^^^^^^^^^^^^^^^^^^^^^

This plugin adds two-factor authentication to your wallet.
For more information, visit https://api.trustedcoin.com/#/electrum-help


Virtual Keyboard
^^^^^^^^^^^^^^^^

Add an optional virtual keyboard to the password dialog.
Warning: do not use this if it makes you pick a weaker password.


External Plugins
----------------
Electrum supports importing third party plugins from *.zip* files. Once you obtained a plugin you can load it with the **Add** button in the plugins dialog.

To prevent loading malicious plugins (e.g. by malware) Electrum will require you to define a **plugin password** when loading an external Plugin the first time. The plugin password is independent of the currently open wallet and can be reset if forgotten.

Setting up the plugin password
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
To check the authenticity of plugins without requiring to enter the password on each startup Electrum requires you to store a **public key text string** with root permissions. The root permissions prevent some malware from modifying the string.

On Linux
""""""""
Open a *Terminal* and run the following commands:

| 1. Create the directory:
| $ sudo mkdir -p /etc/electrum

| 2. Open a text editor with root permissions:
| $ sudo nano /etc/electrum/plugin_pubkey

| 3. Paste the public key string in the text editor.
| 4. Exit the nano editor with CTRL + X.

On Windows
""""""""""
| 1. Open a *Run Dialog* using Windows + R keys.
| 2. Enter 'regedit' and press Enter.
| 3. Navigate to 'HKEY_LOCAL_MACHINE\\SOFTWARE'.
| 4. Create a new directory named 'Electrum'.
| 5. In the directory 'Electrum', create a new directory called 'PluginKey'.
| 6. Inside the 'PluginKey' directory, create an entry with your **public key string** as value.

    See the following **screenshot**:

    .. image:: png/external_plugin_windows_regedit.png
        :align: center

Plugin development
------------------
If you are interested in developing your own plugin, have a look at the https://github.com/spesmilo/electrum-plugins repository and internal plugins in the electrum repository for examples.