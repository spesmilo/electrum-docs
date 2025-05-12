
How to split your coins using Electrum in case of a fork
========================================================

Note:
-----

This document has been updated for Electrum 2.9.


What is a fork?
---------------

A blockchain fork (or blockchain split) occurs when a deviating
network begins to generate and maintain a conflicting chain of blocks
branching from the original, essentially creating another "version of
bitcoin" or cryptocurrency, with its very own blockchain, set of
rules, and market value.

If there is a fork of the Bitcoin blockchain, two distinct currencies
will coexist, having different market values.


What does it mean to 'split your coins'?
----------------------------------------

An address on the original blockchain will now also contain the same
amount on the new chain.

If you own bitcoin before the fork, a transaction that spends these
coins after the fork will, in general, be valid on both chains. This
means that you might be spending both coins simultaneously. This is
called 'replay'. To prevent this, you need to move your coins using
transactions that differ on both chains.



Fork detection
--------------

Electrum (version 2.9 and higher) is able to detect consensus failures
between servers (blockchain forks), and lets users select their branch
of the fork.

* Electrum will download and validate block headers sent by servers
  that may follow different branches of a fork in the Bitcoin
  blockchain. Instead of a linear sequence, block headers are
  organized in a tree structure. Branching points are located
  efficiently using binary search. The purpose of MCV is to detect and
  handle blockchain forks that are invisible to the classical SPV
  model.
    
* The desired branch of a blockchain fork can be selected using the
  network dialog. Branches are identified by the hash and height of
  the diverging block. Coin splitting is possible using RBF
  transaction (a tutorial will be added).


This feature allows you to pick and choose which chain and network you spend on.


Procedure
---------

   1. Preparation

      a. Menu ➞ View ➞ Show Coins
      b. Menu ➞ Tools ➞ Preferences ➞ Propose Replace-By-Fee ➞ "Always"

   2. Select a chain / network

      a. Menu ➞ Tools ➞ Network

         Notice how the branches have different hashes at different heights.
         You can verify which chain you're on by using block explorers to verify
         the hash and height.

            .. image:: png/coin_splitting/select_main_chain.png
            .. image:: png/coin_splitting/chain_search_height.png
            .. image:: png/coin_splitting/chain_verify_hash.png

   3. Send your coins to yourself

      a. Copy your receiving address to the sending tab.
      b. Enter how many coins you'd like to split. (enter " ! " for ALL)
      c. Check "Replaceable"
      d. Send ➞ Sign ➞ Broadcast

   4. Wait for the transaction to confirm on one network.

      a. You'll want to switch between chains (via the network panel)
         to monitor the transaction status.

      b. Wait until you see the transaction confirm on one chain.

         .. image:: png/coin_splitting/unconfirmed.png
         .. image:: png/coin_splitting/confirmed.png

      c. Immediately use "RBF" on the unconfirmed transaction to "Increase fee"

         .. image:: png/coin_splitting/increase_fee.png

   5. Wait for both chains to confirm the transaction.

   6. Verify the transaction has a different TXID on each chain.

         .. image:: png/coin_splitting/main_chain_txid.png
         .. image:: png/coin_splitting/alternate_chain_txid.png

You will now have coins seperately spendable on each chain.  If it failed,
no harm done, you sent to yourself!  Just try again.
