Coin Splitting
==============

In the event of a chain split, you may wish to spend one chain's coins,
while keeping the other's.  This feature allows you to pick and choose 
which chain and network you spend on.

Your choice
-----------

We at Electrum believe in your individual right to choose how
your coins may help guide the evolution of Bitcoin. 

Bitcoin follows rules that may change with overwhelming support in the community, 
however, if a significant enough (to be self-sufficient) portion 
of the network were to adopt new rules without the rest, this could 
create a "chain split".   


What is a chain split?
---------------------

A chain split occurs when a deviating network begins to generate and 
maintain a conflicting chain of blocks branching from the original,
essentially creating another "version of bitcoin" or cryptocurrency, 
with its very own blockchain, set of rules, and market value.

Remember, they both share the same original history.  An address on 
the original blockchain will now also contain the same amount on the
new chain.  Whether or not this amount has worth is entirely up to
you, the community, and supply versus demand.


How do I choose?
----------------

Electrum is proud to announce a new feature that allows you to choose
which chain you wish to spend on.  You may choose from any chain the
electrum client detects.  From here, supply and demand takes over.


Procedure
---------

   1. Preparation

      a. Menu ➞ View ➞ Show Coins
      b. Menu ➞ Tools ➞ Preferences ➞ Propose Replace-By-Fee ➞ "Always"

   2. Select a chain / network

      a. Menu ➞ Network

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
