Hardware wallets on Linux
=========================

The following aims to be a concise guide of what you need to get your
hardware wallet working with Electrum.

1. Dependencies
~~~~~~~~~~~~~~~

Currently all hardware wallets depend on ``hidapi``, to be able to build
that, you need:

::

   sudo apt-get install libusb-1.0-0-dev libudev-dev

At least, these are the names of the packages on Ubuntu/Debian. For
other distros, you might need to find the corresponding packages.

2. Python libraries
~~~~~~~~~~~~~~~~~~~

Then depending on the device you have, you need a python package
(typically a library by the manufacturer):


Trezor
^^^^^^

::

   python3 -m pip install trezor

For more details, refer to `python-trezor`_.


Ledger
^^^^^^

::

   python3 -m pip install btchip-python

For more details, refer to `btchip-python`_.


KeepKey
^^^^^^^

::

   python3 -m pip install keepkey

For more details, refer to `python-keepkey`_.


Digital Bitbox
^^^^^^^^^^^^^^

The Digital Bitbox does not have (nor need) its own library but it still
needs ``hidapi``.

::

   python3 -m pip install hidapi

3. udev rules
~~~~~~~~~~~~~

You will need to configure udev rules:


Trezor
^^^^^^

See `TREZOR User Manual: Configuration of udev rules <https://doc.satoshilabs.com/trezor-user/settingupchromeonlinux.html#manual-configuration-of-udev-rules>`_

Ledger
^^^^^^

See `Ledger Support Center: What to do if my Ledger Nano S is not recognized on Windows and/ or Linux? <https://support.ledgerwallet.com/hc/en-us/articles/115005165269-What-to-do-if-my-Ledger-Nano-S-is-not-recognized-on-Windows-and-or-Linux>`_


KeepKey
^^^^^^^

See `KeepKey Support Desk: KeepKey wallet is not being recognized by Linux <https://support.keepkey.com/support/solutions/articles/6000037796-keepkey-wallet-is-not-being-recognized-by-linux>`_


Digital Bitbox
^^^^^^^^^^^^^^

See `Bitbox | Linux <https://shiftcrypto.ch/start_linux>`_

 
4. Apply configuration
~~~~~~~~~~~~~~~~~~~~~~


To apply the changes, reload udev rules (or reboot):

::

   sudo udevadm control --reload-rules && sudo udevadm trigger

5. Done
~~~~~~~

That’s it! Electrum should now detect your device.

