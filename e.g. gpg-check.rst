First, you need ThomasV fingerprint. 

Open your terminal and type:

.. code-block:: bash

gpg --recv-keys 6694D8DE7BE8EE5631BED9502BD5824B7F9470E6

Or save from: [7F9470E6] (https://pgp.mit.edu/pks/lookup?op=vindex&search=0x2BD5824B7F9470E6) as ThomasV.asc

Go back to Electrum website and download Electrum-X.X.X.tar.gz and its signature Electrum-X.X.X.tar.gz.asc

Copy all the 3 files to the same folder, open the terminal and use command 'cd' to navigate to that folder or right click on the folder and select "Open in Terminal" and run these commands.

.. code-block:: bash

gpg --import ThomasV.asc

.. code-block:: bash

gpg --verify Electrum-X.X.X.tar.gz.asc Electrum-X.X.X.tar.gz

If the message returned says Good signature and that it was signed by ThomasV with a Primary key fingerprint: 6694 D8DE 7BE8 EE56 31BE  D950 2BD5 824B 7F94 70E6, then the software is authentic.

Remember to check again the pgp signature every time you make a new download.
