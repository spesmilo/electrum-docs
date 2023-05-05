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

Then, depending on the device you have, you need a python package
(typically a library by the manufacturer).
For a usually more up-to-date list (including potential version requirements), refer to
`requirements-hw.txt <https://github.com/spesmilo/electrum/blob/master/contrib/requirements/requirements-hw.txt>`_
in the client source.


Trezor
^^^^^^

::

   python3 -m pip install trezor[hidapi]

For more details, refer to `python-trezor <https://github.com/trezor/trezor-firmware/tree/master/python>`_.


Ledger
^^^^^^

::

   python3 -m pip install hidapi btchip-python ecdsa ledger-bitcoin

For more details, refer to
`LedgerHQ/app-bitcoin-new <https://github.com/LedgerHQ/app-bitcoin-new/tree/develop/bitcoin_client>`_
and
`LedgerHQ/btchip-python <https://github.com/LedgerHQ/btchip-python>`_.


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


BitBox02
^^^^^^^^

::

   python3 -m pip install bitbox02

For more details, refer to `python-bitbox02 <https://github.com/digitalbitbox/bitbox02-firmware/tree/master/py>`_.


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

Jade
^^^^^^^^

::

   python3 -m pip install pyserial cbor

For more details, refer to `jadepy <https://github.com/spesmilo/electrum/tree/master/electrum/plugins/jade/jadepy>`_.


3. udev rules
~~~~~~~~~~~~~

You will need to configure udev rules.
See `electrum/contrib/udev <https://github.com/spesmilo/electrum/tree/master/contrib/udev>`_


4. Done
~~~~~~~

That's it! Electrum should now detect your device.

