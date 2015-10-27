The Python Console
==================

Most Electrum commands are available not only using the command-line,
but also in the GUI Python console. 

The results are Python objects, even though they are sometimes
rendered as JSON for clarity.

Let us call listunspent(), to see the list of unspent outputs in the
wallet:

.. code-block:: python

   >> listunspent()
   [
    {
        "address": "12cmY5RHRgx8KkUKASDcDYRotget9FNso3",
        "index": 0,
        "raw_output_script": "76a91411bbdc6e3a27c44644d83f783ca7df3bdc2778e688ac",
        "tx_hash": "e7029df9ac8735b04e8e957d0ce73987b5c9c5e920ec4a445130cdeca654f096",
        "value": 0.01
    },
    {
        "address": "1GavSCND6TB7HuCnJSTEbHEmCctNGeJwXF",
        "index": 0,
        "raw_output_script": "76a914aaf437e25805f288141bfcdc27887ee5492bd13188ac",
        "tx_hash": "b30edf57ca2a31560b5b6e8dfe567734eb9f7d3259bb334653276efe520735df",
        "value": 9.04735316
    }
   ]

Note that the result is rendered as JSON.  However, if we save it to a
Python variable, it is rendered as a Python object:

.. code-block:: python

   >> u = listunspent()
   >> u 
   [{'tx_hash': u'e7029df9ac8735b04e8e957d0ce73987b5c9c5e920ec4a445130cdeca654f096', 'index': 0, 'raw_output_script': '76a91411bbdc6e3a27c44644d83f783ca7df3bdc2778e688ac', 'value': 0.01, 'address': '12cmY5RHRgx8KkUKASDcDYRotget9FNso3'}, {'tx_hash': u'b30edf57ca2a31560b5b6e8dfe567734eb9f7d3259bb334653276efe520735df', 'index': 0, 'raw_output_script': '76a914aaf437e25805f288141bfcdc27887ee5492bd13188ac', 'value': 9.04735316, 'address': '1GavSCND6TB7HuCnJSTEbHEmCctNGeJwXF'}]

This makes it possible to combine Electrum commands with Python. For
example, let us pick only the addresses in the previous result:

.. code-block:: python

   >> map(lambda x:x.get('address'), listunspent())
   [
    "12cmY5RHRgx8KkUKASDcDYRotget9FNso3",
    "1GavSCND6TB7HuCnJSTEbHEmCctNGeJwXF"
   ]

Here we combine two commands, listunspent and dumpprivkeys, in order
to dump the private keys of all adresses that have unspent outputs:

.. code-block:: python

   >> dumpprivkeys( map(lambda x:x.get('address'), listunspent()) )
   {
    "12cmY5RHRgx8KkUKASDcDYRotget9FNso3": "***************************************************",
    "1GavSCND6TB7HuCnJSTEbHEmCctNGeJwXF": "***************************************************"
   }

Note that dumpprivkey will ask for your password if your
wallet is encrypted.
The GUI methods can be accessed through the gui variable.
For example, you can display a QR code from a string
using gui.show_qrcode. Example:

.. code-block:: python

   gui.show_qrcode(dumpprivkey(listunspent()[0]['address']))
