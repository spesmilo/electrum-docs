Electrum Seed Version System
============================

This document describes the Seed Version System used in Electrum
(version 2.0 and higher).

Description
-----------

Electrum derives its private keys and addresses from a seed phrase
made of natural language words. Starting with version 2.0, Electrum
seed phrases include a version number, whose purpose is to indicate
which derivation should be followed in order to derive private keys
and addresses.

In order to eliminate the dependency on a fixed wordlist, the master
private key and the version number are both obtained by hashes of the
UTF8 normalized seed phrase. The version number is obtained by looking
at the first bits of:

.. code-block:: python

    hmac_sha_512("Seed version", seed_phrase)

The version number is also used to check seed integrity; in order to
be correct, a seed phrase must produce a registered version number.


Motivation
----------

Early versions of Electrum (before 2.0) used a bidirectional encoding
between seed phrase and entropy. This type of encoding requires a
fixed wordlist. This means that future versions of Electrum must ship
with the exact same wordlist, in order to be able to read old seed
phrases.

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

Electrum 2.0 derives keys and addresses from a hash of the UTF8
normalized seed phrase with no dependency on a fixed wordlist.
This means that the wordlist can differ between wallets while the seed remains
portable, and that future wallet implementations will not need
today's wordlists in order to be able to decode the seeds
created today. This reduces the cost of forward compatibility.




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

The following version numbers are used for Electrum seeds.

======== ========= =====================================
Number   Type      Description
======== ========= =====================================
0x01     Standard  P2PKH and Multisig P2SH wallets
0x100    Segwit    Segwit: P2WPKH and P2WSH wallets
0x101    2FA       Two-factor authenticated wallets
======== ========= =====================================

In addition, the version bytes of master public/private keys indicate
what type of output script should be used, and on which network. The
prefixes are detailed `here <xpub_version_bytes.html>`__.


Seed generation
---------------

When the seed phrase is hashed during seed generation, the resulting hash must
begin with the correct version number prefix. This is achieved by enumerating a
nonce and re-hashing the seed phrase until the desired version number is
created. This requirement does not decrease the security of the seed (up to the
cost of key stretching, that might be required to generate the private keys).


Security implications
---------------------

Electrum currently use the same wordlist as BIP39 (2048 words). A
typical seed has 12 words, which results in 132 bits of entropy in the
choice of the seed.

Following BIP39, 2048 iterations of key stretching are added for the
generation of the master private key. In terms of hashes, this is
equivalent to adding an extra 11 bits of security to the seed
(2048=2^11).

From the point of view of an attacker, the constraint added by
imposing a prefix to the seed version hash does not decrease the
entropy of the seed, because there is no knowledge gained on the seed
phrase. The attacker still needs to enumerate and test 2^n candidate
seed phrases, where n is the number of bits of entropy used to
generate the seed.

However, the test made by the attacker will return faster if the
candidate seed is not a valid seed, because the attacker does not need
to generate the key. This means that the imposed prefix reduces the
strength of key stretching.

Let n denote the number of entropy bits of the seed, and m the number
of bits of difficulty added by key stretching: m =
log2(stretching_iterations). Let k denote the length of the prefix, in
bits.

On each iteration of the attack, the probability to obtain a valid seed is p = 2^-k

The number of hashes required to test a candidate seed is: p * (1+2^m) + (1-p)*1 = 1 + 2^(m-k)

Therefore, the cost of an attack is: 2^n * (1 + 2^(m-k))

This can be approximated as 2^(n + m - k) if m>k and as 2^n otherwise.

With the standard values currently used in Electrum, we obtain:
2^(132 + 11 - 8) = 2^135. This means that a standard Electrum seed
is equivalent, in terms of hashes, to 135 bits of entropy.

