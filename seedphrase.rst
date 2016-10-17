Electrum Seed Version System
============================

This document describes the Seed Version System used in Electrum
(version 2.0 and higher).

Motivation
----------

Electrum was the first Bitcoin wallet to derive private keys from a
seed phrase made of English words. Early versions of Electrum (before
2.0) used a bidirectional encoding between seed phrase and
entropy. This type of encoding requires a fixed wordlist. This means
that future versions of Electrum must ship with the exact same
wordlist, in order to be able to read old seed phrases.

BIP39 was introduced two years after Electrum. BIP39 seeds include a
checksum, in order to help users figure out typing errors. However,
BIP39 suffers the same shortcomings as early Electrum seed phrases:

 - A fixed wordlist is still required. Following our recommendation,
   BIP39 authors decided to derive keys and addresses in a way that
   does not depend on the wordlist. However, BIP39 still requires the
   wordlist in order to compute its checksum, which is plainly
   inconsistent, and defeats the purpose of our recommendation. This
   problem is exacerbated by the fact that BIP39 proposes to create
   one wordlist per language. This threatens the portability of BIP39
   seed phrases.

 - BIP39 seed phrases do not include a version number. This means that
   software should always know how to generate keys and
   addresses. BIP43 suggests that wallet software will try various
   existing derivation schemes within the BIP32 framework. This is
   extremely inefficient and rests on the assumption that future
   wallets will support all previously accepted derivation
   methods. If, in the future, a wallet developer decides not to
   implement a particular derivation method because it is deprecated,
   then the software will not be able to detect that the corresponding
   seed phrases are not supported, and it will return an empty wallet
   instead. This threatens users funds.

For these reasons, Electrum does not generate BIP39 seeds. Starting
with version 2.0, Electrum uses the following Seed Version System,
which addresses these issues.


Description
-----------

Electrum 2.0 derives keys and addresses from a hash of the UTF8
normalized seed phrase with no dependency on a fixed wordlist.
This means that the wordlist can differ between wallets while the seed remains
portable, and that future wallet implementations will not need
today's wordlists in order to be able to decode the seeds
created today. This reduces the cost of forward compatibility.

In addition, Electrum 2.0 seed phrases include a version number. The
purpose of the version number is to indicate how addresses and keys
are derived from the seed. Similar to keys derivation, the version
number is also obtained by a hash of the UTF8 normalized seed phrase.

The version number is also used to check seed integrity; in order to
be correct, a seed phrase must produce a registered version number.



Version number
--------------

The version number is a prefix of a hash derived from the seed
phrase. The length of the prefix is a multiple of 4 bits. The prefix
is computed as follows:

.. code-block:: python

  def version_number(seed_phrase):
    # normalize seed
    normalized = prepare_seed(seed_phrase)
    # compute hash
    h = hmac_sha_512("Seed version", normalized)
    # use hex encoding, because prefix length is a multiple of 4 bits
    s = h.encode('hex')
    # the length of the prefix is written on the fist 4 bits
    # for example, the prefix '101' is of length 4*3 bits = 4*(1+2)
    length = int(s[0]) + 2
    # read the prefix
    prefix = s[0:length]
    # return version number
    return hex(int(prefix, 16))

The normalization function (prepare_seed) removes all but one space
between words. It also removes diacritics, and it removes spaces
between Asian CJK characters.



List of reserved numbers
------------------------

The following version numbers are used in Electrum.

======== ========= =====================================
Number   Type      Description
======== ========= =====================================
0x01     Standard  P2PKH and Multisig P2SH wallets
0x02     Segwit    Reserved for Segwit
0x101    2FA       Two-factor authenticated wallets
======== ========= =====================================


Seed generation
---------------

When the seed phrase is hashed during seed generation, the resulting hash must
begin with the correct version number prefix. This is achieved by enumerating a
nonce and re-hashing the seed phrase until the desired version number is
created. This requirement does not decrease the security of the seed (up to the
cost of key stretching, that might be required to generate the private keys).


Wordlist
--------

Electrum currently use the same wordlist as BIP39 (2048 words).
A typical seed has 12 words and 132 bits of entropy.

