Plugins
=======

The plugin system of Electrum is designed to allow the development of new features without increasing the core code of Electrum. There are two types of plugins, **internal** and **external** plugins.

To enable or disable Plugins, see **Menu Bar** > **Tools** > **Plugins**.

    .. image:: png/plugins.png
        :align: center


Internal Plugins
----------------

Internal Plugins are shipped with Electrum and maintained in the Electrum repository.

External Plugins
----------------
Electrum supports importing third party plugins from *.zip* files. Once you obtained a plugin you can load it with the **Add** button in the plugins dialog.

Alternatively, if you are running Electrum from sources, you may clone
a third-party plugin repository, and add a symbolic link in your
electrum/electrum/plugins directory.

.. note::
    A list of internal and external plugins can be found at `plugins.electrum.org <https://plugins.electrum.org>`_.

Setting up the plugin password
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To prevent loading malicious plugins (e.g. by malware) Electrum will
require you to define a **plugin password** when loading an external
Plugin the first time. The plugin password is independent of the
currently open wallet and can be reset if forgotten.

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

Plugin Development
------------------

If you are interested in developing your own plugin, please read :ref:`Electrum Plugin development <plugin_dev>`
