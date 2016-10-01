Electrum Seed Version System
============================

Electrum has been the first Bitcoin wallet to derive private keys from
a seed phrase made of English words. Early versions of Electrum used a
bidirectional encoding between seed phrase and entropy, requiring a
fixed wordlist.

Starting with version 2.0, Electrum derives its master key from a hash
of the UTF8 normalized seed phrase, in a way that does not depend on
the wordlist. This means that the wordlist can be updated without
breaking existing seeds, and that future wallet implementations will
not need to carry today's wordlists in order to be able to decode seeds
created today. The rationale is to minimize the cost of forward
comptibility.

In addition, Electrum 2.0 seed phrases include a version number. The
purpose of the version number is to indicate how addresses and keys
are derived from the seed. Similar to keys derivation, the version
number is obtained by a hash of the UTF8 normalized seed phrase.

The version number is also used to check seed integrity; to be
correct, a seed phrase must produce a registered version number.


Seed phrase normalization
-------------------------

.. code-block:: python

  normalized_seedphrase = mnemonic.prepare_seed(seed_phrase)

Note that the normalization function removes diacritics and
also spaces between asian CJK characters (this differs from
bip39).


Version number
--------------

The following hash is computed from the seed phrase:

.. code-block:: python

  s = hmac_sha_512("Seed version", normalized_seedphrase)

The version number is a prefix of s.  The length of the prefix is a
multiple of 4 bits:

.. code-block:: python

  length = 4*(n+2)

where n is encoded on the first four bits of s.
For example, the prefix '0x101' is of length 12 bits = 4*(1+2)


List of reserved prefixes
-------------------------

The following seed types are used in Electrum.

======== ========= =============================
Prefix   Type      Description
======== ========= =============================
0x01     Standard  P2PKH, single account
0x02     Segwit    Reserved for Segwit
0x101    2FA       Two-factor authenticated
======== ========= =============================


Seed generation
---------------

Seed generation requires to find a phrase whose hash has the desired
prefix. This can only be achieved by enumeration, so the existence of
that constraint does not decrease the security of the seed (up to the
cost of key stretching required to generate the private keys).


Wordlist
--------

Electrum currently use the same wordlist as BIP39 (2048 words).
A typical seed has 12 words and 132 bits of entropy.


Comparison to BIP39
-------------------

This system is not compatible with BIP39. BIP39 requires a
predetermined wordlist in order to compute its checksum.
BIP39 also lacks a version number.

