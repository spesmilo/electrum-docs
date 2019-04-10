Verifying GPG signature of Electrum using Linux command line
============================================================

This can be used to verify the authenticity of Electrum binaries/sources.

Download only from electrum.org and remember to check the gpg signature again every time you download a new version

Obtain public GPG key for ThomasV
---------------------------------

In a terminal enter (or copy):

.. code-block:: bash

   gpg --keyserver keys.gnupg.net --recv-keys 6694D8DE7BE8EE5631BED9502BD5824B7F9470E6 
   
You should be able to substitute any public GPG keyserver if keys.gnupg.net is (temporarily) not working

Download Electrum and signature file (asc)
------------------------------------------

Download the Python Electrum-<version>.tar.gz or AppImage file 

Right click on the signature file and save it as well

Verify GPG signature
--------------------

Run the following command from the same directory you saved the files replacing <electrum file> with the one actually downloaded:

.. code-block:: bash

   gpg --verify <electrum file>.asc <electrum file>

The message should say:

.. code-block:: bash

  Good signature from "Thomas Voegtlin (https://electrum.org) <thomasv@electrum.org>

and 

.. code-block:: bash

  Primary key fingerprint: 6694 D8DE 7BE8 EE56 31BE  D950 2BD5 824B 7F94 70E6

You can ignore this:

.. code-block:: bash

  WARNING: This key is not certified with a trusted signature!
  gpg:          There is no indication that the signature belongs to the owner.

as it simply means you have not established a web of trust with other GPG users
