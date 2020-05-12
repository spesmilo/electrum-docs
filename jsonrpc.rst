JSONRPC interface
=================


Commands to the Electrum daemon can be sent using JSONRPC. This is
useful if you want to use electrum in a PHP script.

Note that the daemon uses a random port number by default. In order to
use a stable port number, you need to set the 'rpcport' configuration
variable (and to restart the daemon):

.. code-block:: bash

   electrum setconfig rpcport 7777

Further, starting with Electrum 3.0.5, the JSON-RPC interface is
authenticated using `HTTP basic auth`_.

.. _`HTTP basic auth`: https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication#Basic_authentication_scheme

The username and the password are config variables.
When first started, Electrum will initialise both;
the password will be set to a random string. You can of course
change them afterwards (the same way as the port, and then restart
the daemon). To simply look up their value:

.. code-block:: bash

   electrum getconfig rpcuser
   electrum getconfig rpcpassword

Note that HTTP basic auth sends the username and the password unencrypted as
part of the request. While using it on localhost is fine in our opinion,
using it across an untrusted LAN or the Internet is not secure.
Hence, you should take further measures in such cases, such as wrapping the
connection in a secure tunnel. For further details, `read this`_.

.. _`read this`: https://bitcoin.org/en/release/v0.12.0#rpc-ssl-support-dropped

After setting a static port, and configuring authentication,
we can perform queries using curl or PHP. Example:

.. code-block:: bash

   curl --data-binary '{"jsonrpc":"2.0","id":"curltext","method":"getbalance","params":[]}' http://username:password@127.0.0.1:7777

Query with named parameters:

.. code-block:: bash

   curl --data-binary '{"jsonrpc":"2.0","id":"curltext","method":"listaddresses","params":{"funded":true}}' http://username:password@127.0.0.1:7777

Create a payment request:

.. code-block:: bash

   curl --data-binary '{"jsonrpc":"2.0","id":"curltext","method":"addrequest","params":{"amount":"3.14","memo":"test"}}' http://username:password@127.0.0.1:7777
