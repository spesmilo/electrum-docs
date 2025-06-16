Electrum Plugin development
===========================


Note: If you are interested in developing your own plugin, have a look at
the https://github.com/spesmilo/electrum-plugins repository and
internal plugins in the electrum repository for examples.



Plugin Hooks
------------

Plugins interact with the Electrum code through ''hooks''.


Plugin code:

.. code-block:: python

	class MyPlugin(Plugin):

		@hook
		def alpha(self, params):
		    do_stuff()

Electrum code:

.. code-block:: python

	run_hook('alpha', params)


Directory structure
-------------------

Your plugin should contain:
 * manifest.json: this file describes the plugin.
 * __init__.py: this file includes commands and config variable declarations
 * one or several plugin modules: a module that contains a Plugin class, which inherits from electrum.BasePlugin.
   It will be imported at runtine. Examples: qt.py, qml.py, cmdline.py



The manifest.json file
----------------------

This file is pre-loaded in order to display plugin information in the Electrum client.
It contains the list of GUIs for which the plugin is available.


In our example, this is how the manifest.json looks like:

.. code-block:: json

    {
	"name": "virtualkeyboard",
	"fullname": "Virtual Keyboard",
	"description": "Add an optional virtual keyboard to the password dialog.\nWarning: do not use this if it makes you pick a weaker password.",
	"available_for": ["qt"],
	"author": "The Electrum developers",
	"license": "MIT",
        "icon":"keyboard-icon.svg",
	"version": "0.0.1"
    }


In the 'available_for' field, this plugin declares that it is available for the Qt gui.
Therefore, Electrum will expect a Plugin class in the 'qt.py' file.


The plugin module:
-------------------

This is how the plugin looks like:

.. code-block:: python

    from electrum.plugin import BasePlugin, hook

    class Plugin(BasePlugin):

        @hook
        def password_dialog(self, pw, grid, pos):
	    # we create a button
            vkb_button = QPushButton('')
	    # we add the plugin icon to our button
            vkb_button.setIcon(read_QIcon_from_bytes(self.read_file("keyboard-icon.svg")))
	    # we connect it to our method
            vkb_button.clicked.connect(lambda: self.toggle_vkb(grid, pw))
	    # add the button to the grid passed by the GUI
            grid.addWidget(vkb_button, pos, 2)

        def toggle_vkb(self, grid, pw):
	    # here be dragons
	    ...

Creating a zip file
-------------------

Plugins distributed by third-parties must be packaged in a zip file.
Use the electrum/contrib/make_plugin script to generate the zip file.

Example:

.. code-block:: bash

   git clone https://github.com/spesmilo/electrum-plugins.git /opt/electrum-plugins
   cd /opt/electrum
   ./contrib/make_plugin /opt/electrum-plugins/virtualkeyboard
     creating /opt/electrum/virtualkeyboard.zip
     added virtualkeyboard/./manifest.json
     added virtualkeyboard/./qt.py
     added virtualkeyboard/./__init__.py
     added virtualkeyboard/./keyboard-icon.png
     added virtualkeyboard/./keyboard-icon.svg
     added virtualkeyboard/blah/__init__.py
     Created /opt/electrum/virtualkeyboard-0.0.1.zip

This creates a virtualkeyboard-0.0.1.zip file in your local directory.
The file can be imported in Electrum


Hardware wallet plugins
-----------------------

Hardware wallet plugins are not displayed in the list of plugins
visible in the GUI.  Instead, they are enabled by the Electrum wizard.
It is possible to import a third-party hardware wallet plugin from the
Electrum wizard.

    .. image:: png/plugin_wizard.png
        :align: center

It is possible to distribute a hardware wallet plugin as a zip file,
if you include all your python dependencies in the zip
file.

Non-python dependencies (such as hidapi) are typically bundled
in Electrum binaries. See the list here:
https://github.com/spesmilo/electrum/blob/master/contrib/requirements/requirements-hw.txt
