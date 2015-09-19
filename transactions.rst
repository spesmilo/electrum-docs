Serialization of unsigned or partially signed transactions
==========================================================

Electrum 2.0 uses an extended serialization format for transactions.
The purpose of this format is to send unsigned and partially signed
transactions to cosigners or to cold storage.

This is achieved by extending the 'pubkey' field of a transaction
input.


Extended public keys
--------------------

The first byte of the pubkey indicates if it is an
extended pubkey:

- 0x02, 0x03, 0x04: legal Bitcoin public key (compressed or not).
- 0xFF, 0xFE, 0xFD: extended public key.


Extended public keys are of 3 types:

- 0xFF: bip32 xpub and derivation
- 0xFE: legacy electrum derivation: master public key + derivation
- 0xFD: unknown pubkey, but we know the Bitcoin address.

Public key
----------

This is the legit Bitcoin serialization of public keys.

+--------------+-------------------------------------+
| 0x02 or 0x03 |    compressed public key (32 bytes) |
+--------------+-------------------------------------+
| 0x04         | uncompressed public key (64 bytes)  |
+--------------+-------------------------------------+


BIP32 derivation
----------------

+-----------+-----------------+------------------------------+
| 0xFF      | xpub (78 bytes) | bip32 derivation (2*k bytes) |
+-----------+-----------------+------------------------------+

Legacy Electrum Derivation
--------------------------

+-----------+-----------------+----------------------+
| 0xFE      | mpk (64 bytes)  | derivation (4 bytes) |
+-----------+-----------------+----------------------+


Bitcoin address
---------------

Used if we don't know the public key, but we know the
address (or the hash 160 of the output script). The
cosigner should know the public key.

+-----------+-------------------------------------+
| 0xFD      | hash_160_of_script (20 bytes)       |
+-----------+-------------------------------------+

