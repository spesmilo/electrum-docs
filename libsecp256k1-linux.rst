libsecp256k1 on Linux
=========================

Notes about getting libsecp256k1 to work with Electrum on Linux.


1. Using package manager
~~~~~~~~~~~~~~~~~~~~~~~~

On recent versions of Ubuntu/Debian, libsecp256k1 should be available
through the package manager:

::

    sudo apt-get install libsecp256k1-0


Electrum should be able to find the ``.so`` file and use it.


2. How library is searched for
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The command Electrum uses to find the library, on Linux, is the following:

::

    import ctypes; ctypes.cdll.LoadLibrary('libsecp256k1.so.0')


If the library does not seem to be picked up by Electrum, consider
opening a python interpreter to see for yourself.


3. If you compile libsecp256k1 yourself
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you compile from source, the ``.so`` files are typically placed in
``/usr/local/lib``.

Unfortunately, ``ctypes.cdll.LoadLibrary`` does not seem to find them there.

Two workarounds:

Set LD_LIBRARY_PATH env var
^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can set the LD_LIBRARY_PATH environment variable.
Start Electrum like this:

::

    LD_LIBRARY_PATH=/usr/local/lib electrum


Symlink .so file
^^^^^^^^^^^^^^^^

You can symlink the ``.so`` file. ``/usr/lib`` seems to work.

::

    sudo ln -s /usr/local/lib/libsecp256k1.so.0 /usr/lib/libsecp256k1.so.0

