Basics
======


Thin Client
-----------

Electrum's focus is security, recoverability, versatiliy, and speed.
The servers do the heavy lifting. (without compromising security)
Your private keys are never shared with the server, only addresses.


Seed Words - KEEP THESE SAFE !!!
----------

Your seed words are used to recover your wallet.   They generate your private keys and addresses.

Example:

.. code-block:: none

   #DO NOT SHARE!
   tango execute day arena female win object expect final tank kingdom web


Address
-------

Each seed / wallet will generate new addresses for each new transaction.
You may share these addresses so that others can pay to them.

Example:

.. code-block:: none

   1Lc5FNXcpb7GfBsx6y4i3ucwg2nxZ5TtLa


Transaction ID - TXID
---------------------

When a transaction is created, this ID can be shared to lookup the transaction status.

Example:

.. code-block:: none

   f10275c6788eadc7334850093341b4d3ca8f25dcd82fdc577e03d6afccc93d75

Transaction Fee
---------------

This fee pays for the amount of data in the transaction.  Too low and the transaction will not confirm.
Transactions with the highest fees usually go first.  After a long time, unconfirmed transactions will drop, as if it never happened.

Confirmation
------------

Confirmations occur when a transaction becomes permanently stored in the blockchain.  On average, confirmations will occur within 10 minutes.
