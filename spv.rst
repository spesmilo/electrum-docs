.. _spv:

Simple Payment Verification
===========================

Simple Payment Verification (SPV) is a technique described
in Satoshi Nakamoto's paper. SPV allows a lightweight
client to verify that a transaction is included in the
Bitcoin blockchain, without downloading the entire
blockchain. The SPV client only needs download the block
headers, which are much smaller than the full blocks. To
verify that a transaction is in a block, a SPV client
requests a proof of inclusion, in the form of a Merkle
branch.

SPV clients offer more security than web wallets, because
they do not need to trust the servers with the information
they send.

Reference: `Bitcoin: A peer-to-peer Electronic Cash System <http://bitcoin.org/bitcoin.pdf>`_

