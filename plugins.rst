Plugins
=======

The plugin system of Electrum is designed to allow the development of new features without increasing the core code of Electrum. There are two types of plugins, **internal** and **external** plugins.

To enable or disable Plugins, see **Menu Bar** > **Tools** > **Plugins**.

    .. image:: png/plugins.png
        :align: center


Internal Plugins
----------------

Internal Plugins are shipped with Electrum and maintained in the Electrum repository.

Below you can find a short description of each integrated Tool.

* Audio Modem: Provides support for air-gapped transaction signing. Requires 'amodem' python package http://github.com/romanz/amodem/

* LabelSync : Save your wallet labels on a remote server, and synchronize them across multiple devices where you use Electrum. Labels, transactions IDs and addresses are encrypted before they are sent to the remote server.

* Nostr Wallet Connect: This plugin allows remote control of Electrum lightning wallets via Nostr NIP-47 (Nostr Wallet Connect). A connection string with daily budget and expiry date can be created from the Desktop GUI as well as the command line and then used in Nostr apps like browser extensions or social media clients.

* Nostr Cosigner: This plugin facilitates the use of multi-signatures wallets. It sends and receives partially signed transactions from/to your cosigner wallet. PSBTs are sent and retrieved encrypted using Nostr relays.

* Revealer: Create a visually encrypted backup of your wallet seeds, or of custom alphanumeric secrets.

* Two Factor Authentication: This plugin adds two-factor authentication to your wallet. For more information, visit https://api.trustedcoin.com/#/electrum-help

* Timelock Recovery: This plug-in allows you to create Timelock Recovery Plans for your wallet. See: https://timelockrecovery.com

* Virtual Keyboard: Add an optional virtual keyboard to the password dialog.

* Swapserver [CLI only]: Offer submarine swaps to other Electrum users. See: :ref:`Running a swapserver <swapserver>`

* Payserver [CLI only]: Run a HTTP server for receiving payments. See :ref:`How to accept Bitcoin on a website <merchant>`.

External Plugins
----------------
Electrum supports importing third party plugins from *.zip* files. Once you obtained a plugin you can load it with the **Add** button in the plugins dialog.

To prevent loading malicious plugins (e.g. by malware) Electrum will
require you to define a **plugin password** when loading an external
Plugin the first time. The plugin password is independent of the
currently open wallet and can be reset if forgotten.

Setting up the plugin password
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To check the authenticity of plugins without requiring to enter the
password on each startup Electrum requires you to store a **public key
text string** with root permissions. The root permissions prevent
malware from modifying the string.

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

List of external plugins
^^^^^^^^^^^^^^^^^^^^^^^^
Below is a non-exhaustive list of known external plugins.

These plugins are **not reviewed or endorsed by Electrum** and should be used **at your own risk**.


.. csv-table:: :rst:dir:`List of external Electrum plugins`
   :header: "Name", "Description", "Repository", "GUI", "Added"

    "Guardian", "`Physical coercion resistance <https://delvingbitcoin.org/t/proposal-guardian-address-gaspv1/2006>`_", "`Github <https://github.com/bitcoinguardian/electrum/tree/master/electrum/plugins/guardian>`_", "Qt", "10/2025"
    "LNURL Server", "`Receive LN payments through a static URL <https://github.com/lnurl/luds/blob/luds/06.md>`_", "`Github <https://github.com/f321x/electrum-lnurl-server>`_", "daemon", "10/2025"
    "Joinstr", "`Collaborative Transactions via Nostr <https://joinstr.xyz/>`_", "`Gitlab <https://gitlab.com/invincible-privacy/joinstr/-/tree/main/plugin>`_", "Qt", "10/2025"
    "Notary", "`Proof-of-burn for Nostr events <https://notary.electrum.org/>`_", "`Github <https://github.com/spesmilo/notary>`_", "daemon", "11/2025"
    "PayServer", "HTTP server receiving payments", "`Github <https://github.com/spesmilo/electrum-payserver>`_", "daemon", "11/2025"


If you want to submit a plugin to be added to the list open a Pull Request on the `Electrum docs repository <https://github.com/spesmilo/electrum-docs/>`_.

Plugin Development
------------------

If you are interested in developing your own plugin, please read :ref:`Electrum Plugin development <plugin_dev>`
