How to split your coins using Electrum in case of a BU Hard Fork
================================================================

Notes:
------

1. I, Thomas Voegtlin, support Segregated Witness as a scaling
solution for Bitcoin, and I am opposed to a hard fork initiated by
miners running Bitcoin Unlimited. However, I also believe that
Electrum users should be free to choose between Bitcoin Core and BU,
and that I should not abuse my position in order to favor one party. I
have tried to keep this documentation as neutral as possible.

2. Despite the various announcements that have been made by both
parties, I believe that the probability of a BU hard fork is fairly
low. Nevertheless, Electrum users have expressed concerns about a hard
fork. This document is intended to address these concerns.

3. This document explains how to split your coins using the existing
Electrum software. I am currently working on an improved version of
Electrum, where blockchain forks will be detected and managed using
checkpoints. However, if a fork occurs now, users will want to be able
to trade their BTC/BTU coins as soon as possible, without waiting for
a new software release. This is the purpose of the present document.


What does it mean to 'split your coins'?
----------------------------------------

If there is a fork of the Bitcoin blockchain, two distinct currencies
will coexist, having different market values. They are referred to as
BTC and BTU here.

If you own Bitcoins before the fork, a transaction that spends these
coins after the fork will, in general, be valid on both chains. This
means that you will be spending BTC and BTU simultaneously. This is
called a 'replay attack'. To prevent this, you need to move your coins
using transactions that differ on both chains.


Electrum and SPV
----------------

Electrum fetches block headers from the Bitcoin network in order to
verify that your transactions are included in the Bitcoin
blockchain. When a transaction is displayed as 'verified' by the GUI,
it means that Electrum received a proof that the transaction is in the
blockchain.

By default, Electrum trusts the longest blockchain to be the valid
blockchain. Electrum is not able to know if block headers correspond
to blocks that follow the Bitcoin Core or BU rules; it only checks
that blocks have been mined with a valid Proof of Work, and that
transactions are included in these blocks.

Electrum has two different modes for fetching your wallet history:
manual server selection and auto-connect. In auto-connect mode,
Electrum will always request your wallet history from a node that has
the longest blockchain. If auto-connect is disabled, your wallet
history will be fetched from a server you choose. If there is a fork,
you will want to select your history server. This option is available
in the GUI and from the command line.

In addition, Electrum has two different modes for fetching the block
headers used to verify your history: it can receive block headers from
a single node (your history server), or from a group of randomly
selected nodes. By default, it will listen to a group of random nodes,
and it will consider that the longest blockchain is the valid
blockchain. If the 'oneserver' option is activated, it will receive
block headers from your history server only. Unfortunately, the
'oneserver' option is only available from command line.



Step 1: Use separate directories for BTC and BTU
------------------------------------------------

While it would be technically possible to use the same directory and
wallet files for both BTC and BTU, doing so will force your client to
discard and re-download transaction histories and headers everytime
you switch between BTC and BTU. In order to prevent that, duplicate
your entire Electrum directory; one will be used for BTC, one for BTU.

With the command line, you can use the -D option to select the
directory used by Electrum:

.. code-block:: bash

   electrum -D <directory>

If you are running Electrum binaries on Windows, you do not have
access to the command line. You can use the 'portable' version of
Electrum instead; it will use the 'electrum_data' directory located in
the directory where the binary is located.


Step 2: Choose your wallet history server
-----------------------------------------

You can select your server from the GUI. Disable the 'auto-connect'
checkbox in the network dialog, and choose a server that you trust to
run Core or BU. Usually servers advertise this information in the
Console tab. There is no way to verify that the server actually runs
what they claim, but this will not be a problem for us; if the server
is dishonest, you will be able to see that your coins have not been
split.

Note that you can also select your server from the command line, with:

.. code-block:: bash

   electrum --server <server>


Step 3. Fetch block headers from the same node as your history.
---------------------------------------------------------------

If you are running Electrum from the command line, you can use the
'oneserver' option as follows:

.. code-block:: bash

   electrum --oneserver

This option starts Electrum in 'one server' mode. When you open the
Network dialog, you will see 'Getting block headers from 1 node'. Now
all your transactions will be verified using the headers sent by your
history server.

This option is only available through the command line; if you are
running an Electrum binary, you will not be able to use it. In that
case, Electrum will fail to verify transactions that are on the
minority chain, and it will display them as 'unverified' once they are
confirmed (this is different from 'unconfirmed', although the GUI icon
is the same). To address this, if you are not using the command line
you should check that your post-fork transactions are confirmed on the
shortest chain using an independent source, such as a block explorer.


Step 4: Split your coins
------------------------

Different solutions have been proposed to split your coins. The
cleanest method is probably to mix your coins with coins that have
been mined after the fork. However, mixing your coins with newly
minted outputs could be much slower, because you would need miners to
send you new coins.

Here we propose to use RBF transactions: it will work with the
existing software, and without the help of miners.

Launch two instances of Electrum, from your your Core and BU
directories. Note that you can run them simultaneously. If you use the
command line, you can combine all the options we explained above:

.. code-block:: bash

   electrum --oneserver --server <electrum_btc_server> -D <electrum_btc_dir>
   electrum --oneserver --server <electrum_bu_server> -D <electrum_bu_dir>

Create a replaceable (RBF) transaction that sends your coins back to
yourself, and broadcast it on both networks (it should actually be
broadcasted on both networks, because there is no replay protection at
the network level. If that does not work, just copy-paste the
transaction from one instance of Electrum to the other, and
rebroadcast it manually).

Once the transaction is visible in both networks, bump its fee on your
BTC version of Electrum. BU nodes might still receive the second
transaction, but they will not propagate it because they do not
implement RBF.

Wait until your transactions are confirmed on both networks, and check
that they have different transaction IDs. If you cannot use the
command line with the --oneserver option, check that transactions are
confirmed using a block explorer website.

You will need to check that the transaction IDs are different on both
chains, because this method is not guaranteed to work (although it
should work most of the time). It will fail if your transaction is
confirmed on the Core chain before you bump its fee, or if a malicious
BU miner decide to confirm the second transaction, despite it not
being normally accepted by BU nodes. If this method fails, you will
only lose the mining fee, and a bit of time. If the BU chain is faster
than the Core chain (or has lower fees), you may increase your chances
by waiting until BU confirms your transaction before you bump its fee
on Core.
