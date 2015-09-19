Electrum seed phrases
=====================


Note: Electrum is not compatible with BIP39.

Electrum uses a seed phrase made of natural language words
in order to derive wallet private keys.

In order to derive the keys in a way that does not depend on the
wordlist, Electrum uses a hash of the UTF8 normalized seed
phrase. That part is similar to BIP39.  However, the checksum
mechanism is different. BIP39 requires a predetermined wordlist in
order to compute the checksum. In contrast, Electrum uses another hash
of the seed phrase. That hash is used both as a checksum and as a
version number.


Seed phrase normalization
-------------------------


normalized_seedphrase = mnemonic.prepare_seed(seed_phrase)


Note that the normalization function removes diacritics and
also spaces between asian CJK characters (this differs from
bip39).

Checksum and version number
---------------------------


The following hash is used:

<pre>s = hmac_sha_512("Seed version", normalized_seedphrase)
</pre>

The first bits of s (prefix) must be in a list of accepted
prefixes.

The length of the prefix is given by the first 4 bits of
the prefix:

<pre>length = 8 + 4*n</pre>

List of reserved prefixes
-------------------------

- 0x01 -> standard wallet (single account)
- 0x101 -> two-factor authentication wallet (long seed used to derive two master keys)

Entropy loss
------------

The seed generation requires to find a seed that has a
legal version prefix. That constraint results in a loss of
entropy. This loss is compensated by adding extra bits of
entropy during the seed generation.

Length of the seed phrase
-------------------------
	  
In order to generate a seedphrase with 128 bits of entropy
and 8 bits of prefix, a wordlist of 2048 words will
typically use 13 words.

It is possible to fall back to 12 words seedphrases by
making the wordlist longer (about 2600 words are needed)
