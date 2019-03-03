Hardware wallets on Linux
=========================

The following aims to be a concise guide of what you need to get your
hardware wallet working with Electrum.

If you use the AppImage, that already has all the dependencies and Python
libraries bundled with it, so skip the first two steps.

1. Dependencies
~~~~~~~~~~~~~~~

Currently all hardware wallets depend on ``hidapi``, to be able to build
that, you need:

*ubuntu:*
::

   sudo apt-get install libusb-1.0-0-dev libudev-dev
   
*fedora:*
::

   sudo dnf install libusb-devel systemd-devel

(Package names may be different for other distributions.)

2. Python libraries
~~~~~~~~~~~~~~~~~~~

Then depending on the device you have, you need a python package
(typically a library by the manufacturer):


Trezor
^^^^^^

::

   python3 -m pip install trezor[hidapi]

For more details, refer to `python-trezor <https://github.com/trezor/python-trezor>`_.


Ledger
^^^^^^

::

   python3 -m pip install btchip-python

For more details, refer to `btchip-python <https://github.com/LedgerHQ/btchip-python>`_.


KeepKey
^^^^^^^

::

   python3 -m pip install keepkey

For more details, refer to `python-keepkey <https://github.com/keepkey/python-keepkey>`_.


Digital Bitbox
^^^^^^^^^^^^^^

The Digital Bitbox only needs ``hidapi``.

::

   python3 -m pip install hidapi


Archos Safe-T
^^^^^^^^^^^^^

::

   python3 -m pip install safet

For more details, refer to `python-safet <https://github.com/archos-safe-t/python-safet>`_.


Coldcard
^^^^^^^^

::

   python3 -m pip install ckcc-protocol

For more details, refer to `ckcc-protocol <https://github.com/Coldcard/ckcc-protocol>`_.


3. udev rules
~~~~~~~~~~~~~

You will need to configure udev rules:


Trezor
^^^^^^

See `TREZOR User Manual: Configuration of udev rules <https://doc.satoshilabs.com/trezor-user/settingupchromeonlinux.html#manual-configuration-of-udev-rules>`_

`backup link <https://github.com/trezor/trezor-common/blob/master/udev/51-trezor.rules>`_


Ledger
^^^^^^

See `Ledger Support Center: What to do if my Ledger Nano S is not recognized on Windows and/ or Linux? <https://support.ledgerwallet.com/hc/en-us/articles/115005165269-What-to-do-if-my-Ledger-Nano-S-is-not-recognized-on-Windows-and-or-Linux>`_

`backup link <https://github.com/LedgerHQ/udev-rules/blob/master/add_udev_rules.sh>`_


KeepKey
^^^^^^^

See `KeepKey Support Desk: KeepKey wallet is not being recognized by Linux <https://support.keepkey.com/support/solutions/articles/6000037796-keepkey-wallet-is-not-being-recognized-by-linux>`_

`backup link <https://github.com/keepkey/udev-rules/blob/master/51-usb-keepkey.rules>`_


Digital Bitbox
^^^^^^^^^^^^^^

See `Bitbox | Linux <https://shiftcrypto.ch/start_linux>`_


Archos Safe-T
^^^^^^^^^^^^^

See `this file in their GitHub repository <https://github.com/archos-safe-t/safe-t-common/blob/master/udev/51-safe-t.rules>`_.


Coldcard
^^^^^^^^

See `this file in their GitHub repository <https://github.com/Coldcard/ckcc-protocol/blob/master/51-coinkite.rules>`_.

(It should go into ``/etc/udev/rules.d/51-coinkite.rules``
or ``/usr/lib/udev/rules.d/51-coinkite.rules``)


4. Apply configuration
~~~~~~~~~~~~~~~~~~~~~~


To apply the changes, reload udev rules (or reboot):

::

   sudo udevadm control --reload-rules && sudo udevadm trigger

5. Done
~~~~~~~

That’s it! Electrum should now detect your device.

