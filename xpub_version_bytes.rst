Version bytes for BIP32 extended public and private keys
========================================================

This document describes the version bytes used in Electrum for master keys.

Abstract
--------

`BIP32 <https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki>`__
defines a serialization format for extended keys. This serialization
includes four bytes allocated as version bytes. We use these version
bytes to encode the type of output scripts (scriptPubKeys) a wallet
should derive along this HD subtree.

Motivation
----------

Among other changes, the activation of SegWit
(`BIP141 <https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki>`__)
introduced new output script templates usable on Bitcoin mainnet. This
poses a new problem for HD wallets in terms of what type of scripts they
should derive from master keys. Previously most wallets offered deriving
either P2PKH or multi-signature embedded in
`BIP16 <https://github.com/bitcoin/bips/blob/master/bip-0016.mediawiki>`__
P2SH outputs, and it was usually deduced from context which of the two
should be used. We believe it would be better to have this knowledge
explicitly.

Encoding the script type in
`BIP32 <https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki>`__
extended keys is beneficial for wallets. For example, a watch-only
wallet constructed from an extended public key would otherwise have to
either (1) derive all possible scripts in the subtree [1]_, or (2)
prompt the user to enter the script type in a side-channel.

Deriving all possible scripts (1)

-  Potentially wastes resources. Wallets have to monitor more output
   scripts for incoming transactions.
-  Introduces key-reuse. Public keys are reused for each script type.
-  Becomes an ever-growing barrier for developers of new wallet software
   to implement detecting and spending from every type of UTXO.
   Otherwise if they choose not to implement legacy script types that
   can lead to not discovering funds.

Prompting the user to enter the script type (2) as additional
information besides the extended public key just leads to more complex
user interfaces and suboptimal experience.

Users directly interact with master public keys, for watch-only wallets,
or when specifying cosigners for HD multisig. These keys are commonly
serialized as
`BIP32 <https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki>`__
extended keys, hence it makes sense to make the encoding of the script
type user-visible. As version bytes are already used to encode the
network in such a way, this document introduces new constants for
version bytes to further encode the script type.

Considerations
--------------

Without explicit knowledge of the output script type, wallets have no
clear way to communicate to users whether the type of script the user
would expect to be derived is supported/implemented. Casual users would
simply notice funds missing, if they have prior knowledge of funds at
all.

The version byte values defined in
`BIP32 <https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki>`__
do not distinguish P2PKH and P2SH-multisig outputs, and to remain
backwards compatible, this will not be changed. However this has already
resulted in loss of funds in some cases, where e.g. a user restored and
received transactions on a watch-only P2PKH wallet from a master public
key participating in P2SH-multisig that he had no control over (it was a
key of a different cosigner). To try to prevent this kind of situation,
e.g. P2WPKH and P2WSH-multisig is distinguished in this document.

Specification
-------------

In the table below,

-  P2SH stands for a
   `BIP11 <https://github.com/bitcoin/bips/blob/master/bip-0011.mediawiki>`__
   multi-signature script embedded in a
   `BIP16 <https://github.com/bitcoin/bips/blob/master/bip-0016.mediawiki>`__
   pay-to-script-hash output
-  P2WPKH stands for pay-to-witness-public-key-hash (witness version 0),
   as in
   `BIP141 <https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki#p2wpkh>`__
-  P2WPKH-P2SH stands for a P2WPKH script (witness version 0) nested in
   a
   `BIP16 <https://github.com/bitcoin/bips/blob/master/bip-0016.mediawiki>`__
   P2SH output, as in
   `BIP141 <https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki#p2wpkh-nested-in-bip16-p2sh>`__
-  P2WSH stands for a
   `BIP11 <https://github.com/bitcoin/bips/blob/master/bip-0011.mediawiki>`__
   multi-signature pay-to-witness-script-hash (witness version 0)
   script, as in
   `BIP141 <https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki#p2wsh>`__
-  P2WSH-P2SH stands for a
   `BIP11 <https://github.com/bitcoin/bips/blob/master/bip-0011.mediawiki>`__
   multi-signature pay-to-witness-script-hash (witness version 0) script
   nested in a
   `BIP16 <https://github.com/bitcoin/bips/blob/master/bip-0016.mediawiki>`__
   P2SH output, as in
   `BIP141 <https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki#p2wsh-nested-in-bip16-p2sh>`__

Note that an M-of-N multi-signature script is usually constructed from N
extended keys (and M is provided in a side-channel). Hence in most cases
more than one extended key is needed to create such scripts; this is out
of scope of this document.

+---------+---------------+----------+---------------+------------------+
| network | script type   | pub/priv | version bytes | | human-readable |
|         |               |          |               | | prefix         |
+=========+===============+==========+===============+==================+
| mainnet | p2pkh or p2sh | public   | 0x0488b21e    | xpub             |
+---------+---------------+----------+---------------+------------------+
| mainnet | p2pkh or p2sh | private  | 0x0488ade4    | xprv             |
+---------+---------------+----------+---------------+------------------+
| mainnet | p2wpkh-p2sh   | public   | 0x049d7cb2    | ypub             |
+---------+---------------+----------+---------------+------------------+
| mainnet | p2wpkh-p2sh   | private  | 0x049d7878    | yprv             |
+---------+---------------+----------+---------------+------------------+
| mainnet | p2wsh-p2sh    | public   | 0x0295b43f    | Ypub             |
+---------+---------------+----------+---------------+------------------+
| mainnet | p2wsh-p2sh    | private  | 0x0295b005    | Yprv             |
+---------+---------------+----------+---------------+------------------+
| mainnet | p2wpkh        | public   | 0x04b24746    | zpub             |
+---------+---------------+----------+---------------+------------------+
| mainnet | p2wpkh        | private  | 0x04b2430c    | zprv             |
+---------+---------------+----------+---------------+------------------+
| mainnet | p2wsh         | public   | 0x02aa7ed3    | Zpub             |
+---------+---------------+----------+---------------+------------------+
| mainnet | p2wsh         | private  | 0x02aa7a99    | Zprv             |
+---------+---------------+----------+---------------+------------------+
| testnet | p2pkh or p2sh | public   | 0x043587cf    | tpub             |
+---------+---------------+----------+---------------+------------------+
| testnet | p2pkh or p2sh | private  | 0x04358394    | tprv             |
+---------+---------------+----------+---------------+------------------+
| testnet | p2wpkh-p2sh   | public   | 0x044a5262    | upub             |
+---------+---------------+----------+---------------+------------------+
| testnet | p2wpkh-p2sh   | private  | 0x044a4e28    | uprv             |
+---------+---------------+----------+---------------+------------------+
| testnet | p2wsh-p2sh    | public   | 0x024285ef    | Upub             |
+---------+---------------+----------+---------------+------------------+
| testnet | p2wsh-p2sh    | private  | 0x024285b5    | Uprv             |
+---------+---------------+----------+---------------+------------------+
| testnet | p2wpkh        | public   | 0x045f1cf6    | vpub             |
+---------+---------------+----------+---------------+------------------+
| testnet | p2wpkh        | private  | 0x045f18bc    | vprv             |
+---------+---------------+----------+---------------+------------------+
| testnet | p2wsh         | public   | 0x02575483    | Vpub             |
+---------+---------------+----------+---------------+------------------+
| testnet | p2wsh         | private  | 0x02575048    | Vprv             |
+---------+---------------+----------+---------------+------------------+

Backwards Compatibility
-----------------------

This document is backwards compatible with
`BIP32 <https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki>`__;
existing extended keys will keep working. Compatibility is intentionally
broken in the sense that extended keys derived for newer script types will
not have valid
`BIP32 <https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki>`__
version bytes.

Footnotes
---------

.. [1]
   Which is not even possible, given there are an effectively infinite
   number of possible scripts. A wallet could however derive scripts for
   all standard templates.

Reference
---------

-  `BIP11 - M-of-N Standard Transactions
   <https://github.com/bitcoin/bips/blob/master/bip-0011.mediawiki>`__
-  `BIP16 - Pay to Script Hash
   <https://github.com/bitcoin/bips/blob/master/bip-0016.mediawiki>`__
-  `BIP32 - Hierarchical Deterministic Wallets
   <https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki>`__
-  `BIP141 - Segregated Witness (Consensus
   layer) <https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki>`__
