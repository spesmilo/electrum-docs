Electrum protocol specification
===============================

<p>Stratum is a universal bitcoin communication protocol used
mainly by bitcoin client Electrum and miners.</p>

          <div class="toc" id="toc">
            <div id="toctitle">
              <h2>Contents</h2>
              &nbsp;[<a href="#" id="togglelink">hide</a>]&nbsp;</div>

            <ul>
              <li class="toclevel-1 tocsection-1"><a href="#Format">1
                Format</a>
                <ul>
                  <li class="toclevel-2 tocsection-2"><a href="#Request">1.1 Request</a></li>

                  <li class="toclevel-2 tocsection-3"><a href="#Response">1.2 Response</a></li>
                </ul>
              </li>

              <li class="toclevel-1 tocsection-4"><a href="#Methods">2
                Methods</a>
                <ul>
                  <li class="toclevel-2 tocsection-5"><a href="#server.version">2.1 server.version</a></li>

                  <li class="toclevel-2 tocsection-6"><a href="#server.banner">2.2 server.banner</a></li>

                  <li class="toclevel-2 tocsection-7"><a href="#server.donation_address">2.3
                    server.donation_address</a></li>

                  <li class="toclevel-2 tocsection-8"><a href="#server.peers.subscribe">2.4
                    server.peers.subscribe</a></li>

                  <li class="toclevel-2 tocsection-9"><a href="#blockchain.numblocks.subscribe">2.5
                    blockchain.numblocks.subscribe</a></li>

                  <li class="toclevel-2 tocsection-10"><a href="#blockchain.headers.subscribe">2.6
                    blockchain.headers.subscribe</a></li>

                  <li class="toclevel-2 tocsection-11"><a href="#blockchain.address.subscribe">2.7
                    blockchain.address.subscribe</a></li>

                  <li class="toclevel-2 tocsection-12"><a href="#blockchain.address.get_history">2.8
                    blockchain.address.get_history</a></li>

                  <li class="toclevel-2 tocsection-13"><a href="#blockchain.address.get_mempool">2.9
                    blockchain.address.get_mempool</a></li>

                  <li class="toclevel-2 tocsection-14"><a href="#blockchain.address.get_balance">2.10
                    blockchain.address.get_balance</a></li>

                  <li class="toclevel-2 tocsection-15"><a href="#blockchain.address.get_proof">2.11
                    blockchain.address.get_proof</a></li>

                  <li class="toclevel-2 tocsection-16"><a href="#blockchain.address.listunspent">2.12
                    blockchain.address.listunspent</a></li>

                  <li class="toclevel-2 tocsection-17"><a href="#blockchain.utxo.get_address">2.13
                    blockchain.utxo.get_address</a></li>

                  <li class="toclevel-2 tocsection-18"><a href="#blockchain.block.get_header">2.14
                    blockchain.block.get_header</a></li>

                  <li class="toclevel-2 tocsection-19"><a href="#blockchain.block.get_chunk">2.15
                    blockchain.block.get_chunk</a></li>

                  <li class="toclevel-2 tocsection-20"><a href="#blockchain.transaction.broadcast">2.16
                    blockchain.transaction.broadcast</a></li>

                  <li class="toclevel-2 tocsection-21"><a href="#blockchain.transaction.get_merkle">2.17
                    blockchain.transaction.get_merkle</a></li>

                  <li class="toclevel-2 tocsection-22"><a href="#blockchain.transaction.get">2.18
                    blockchain.transaction.get</a></li>
                </ul>
              </li>

              <li class="toclevel-1 tocsection-23"><a href="#External_links">3 External links</a></li>
            </ul>
          </div>

          <h2>Format[<a href="https://electrum.orain.org/w/index.php?title=Stratum_protocol_specification&amp;action=edit&amp;section=1" title="Edit section: Format">edit</a>]</h2>

          <p>Stratum protocol is based on <a class="external text" href="http://www.jsonrpc.org/specification" rel="nofollow">JSON-RPC 2.0</a> (although it doesn't
            include "jsonrpc" information in every message). Each
            message has to end with a line end character (\n).</p>

          <h3>Request[<a href="https://electrum.orain.org/w/index.php?title=Stratum_protocol_specification&amp;action=edit&amp;section=2" title="Edit section: Request">edit</a>]</h3>

          <p>Typical request looks like this: { "id": 0, "method":
            "some.stratum.method", "params": [] }</p>

          <ul>
            <li> id begins at 0 and every message has its unique id
              number</li>

            <li> list and description of possible methods is below</li>

            <li> params is an array, e.g.: [ "1myfirstaddress",
              "1mysecondaddress", "1andonemoreaddress" ]</li>
          </ul>

          <h3>Response[<a href="https://electrum.orain.org/w/index.php?title=Stratum_protocol_specification&amp;action=edit&amp;section=3" title="Edit section: Response">edit</a>]</h3>

          <p>Responses are similar: { "id": 0, "result":
            "616be06545e5dd7daec52338858b6674d29ee6234ff1d50120f060f79630543c"
            }</p>

          <ul>
            <li> id is copied from the request message (this way client
              can pair each response to one of his requests)</li>

            <li> result can be:
              <ul>
                <li> null</li>

                <li> a string (as shown above)</li>

                <li> a hash, e.g.: { "nonce": 1122273605, "timestamp":
                  1407651121, "version": 2, "bits": 406305378 }</li>

                <li> an array of hashes, e.g.: [ { "tx_hash:
                  "b87bc42725143f37558a0b41a664786d9e991ba89d43a53844ed7b3752545d4f",
                  "height": 314847 }, { "tx_hash":
                  "616be06545e5dd7daec52338858b6674d29ee6234ff1d50120f060f79630543c",
                  "height": 314853 } ]</li>
              </ul>
            </li>
          </ul>

          <h2>Methods[<a href="https://electrum.orain.org/w/index.php?title=Stratum_protocol_specification&amp;action=edit&amp;section=4" title="Edit section: Methods">edit</a>]</h2>

          <h3>server.version[<a href="https://electrum.orain.org/w/index.php?title=Stratum_protocol_specification&amp;action=edit&amp;section=5" title="Edit section: server.version">edit</a>]</h3>

          <p>This is usually the first client's message, plus it's sent
            every minute as a keep-alive message. Client sends its own
            version and version of the protocol it supports. Server
            responds with its supported version of the protocol (higher
            number at server-side is usually compatible).</p>

          <p><b>request:</b> { "id": 0, "method": "server.version",
            "params": [ "1.9.5", "0.6" ] }<br/>
            <b>response:</b> { "id": 0, "result": "0.8" }</p>

          <h3>server.banner[<a href="https://electrum.orain.org/w/index.php?title=Stratum_protocol_specification&amp;action=edit&amp;section=6" title="Edit section: server.banner">edit</a>]</h3>

          <p><b>request:</b> { "id": 1, "method": "server.banner",
            "params": [] }</p>

          <h3>server.donation_address[<a href="https://electrum.orain.org/w/index.php?title=Stratum_protocol_specification&amp;action=edit&amp;section=7" title="Edit section: server.donation address">edit</a>]</h3>

          <h3>server.peers.subscribe[<a href="https://electrum.orain.org/w/index.php?title=Stratum_protocol_specification&amp;action=edit&amp;section=8" title="Edit section: server.peers.subscribe">edit</a>]</h3>

          <p>Client can this way ask for a list of other active
            servers. Servers are connected to an IRC channel (#electrum
            at freenode.net) where they can see each other. Each server
            announces its version, history pruning limit of every
            address ("p100", "p10000" etc.–the number means how many
            transactions the server may keep for every single address)
            and supported protocols ("t" = tcp@50001, "h" = http@8081,
            "s" = tcp/tls@50002, "g" = https@8082; non-standard port
            would be announced this way: "t3300" for tcp on port 3300).
          </p>

          <p><i>Note: At the time of writing there isn't a true
            subscription implementation of this method, but servers
            only send one-time response. They don't send notifications
            yet.</i></p>

          <p><b>request:</b> { "id": 3, "method":
            "server.peers.subscribe", "params": [] }<br/>
            <b>response:</b> { "id": 3, "result": [ [ "83.212.111.114",
            "electrum.stepkrav.pw", [ "v0.9", "p100", "t", "h", "s",
            "g" ] ], [ "23.94.27.149", "ultra-feather.net", [ "v0.9",
            "p10000", "t", "h", "s", "g" ] ], [ "88.198.241.196",
            "electrum.be", [ "v0.9", "p10000", "t", "h", "s", "g" ] ] ]
            }</p>

          <h3>blockchain.numblocks.subscribe[<a href="https://electrum.orain.org/w/index.php?title=Stratum_protocol_specification&amp;action=edit&amp;section=9" title="Edit section: blockchain.numblocks.subscribe">edit</a>]</h3>

          <h3>blockchain.headers.subscribe[<a href="https://electrum.orain.org/w/index.php?title=Stratum_protocol_specification&amp;action=edit&amp;section=10" title="Edit section: blockchain.headers.subscribe">edit</a>]</h3>

          <p>A request to send to the client notifications about new
            blocks in form of parsed blockheaders.</p>

          <p><b>request:</b> { "id": 5, "method":
            "blockchain.headers.subscribe", "params": [] }<br/>
            <b>response:</b> { "id": 5, "result": { "nonce":
            3355909169, "prev_block_hash":
            "00000000000000002b3ef284c2c754ab6e6abc40a0e31a974f966d8a2b4d5206",
            "timestamp": 1408252887, "merkle_root":
            "6d979a3d8d0f8757ed96adcd4781b9707cc192824e398679833abcb2afdf8d73",
            "block_height": 316023, "utxo_root":
            "4220a1a3ed99d2621c397c742e81c95be054c81078d7eeb34736e2cdd7506a03",
            "version": 2, "bits": 406305378 } }<br/>
            <b>message:</b> { "id": null, "method":
            "blockchain.headers.subscribe", "params": [ { "nonce":
            881881510, "prev_block_hash":
            "00000000000000001ba892b1717690900ae476857120a78fb50825f8b67a42d4",
            "timestamp": 1408255430, "merkle_root":
            "8e92bdbf1c5c581b5942fc290c6c52c586f091b279ea79d4e21460e138023839",
            "block_height": 316024, "utxo_root":
            "060f780c0dd07c4289aaaa2ef24723f73380095b31d60795e1308170ec742ffb",
            "version": 2, "bits": 406305378 } ] }</p>

          <h3>blockchain.address.subscribe[<a href="https://electrum.orain.org/w/index.php?title=Stratum_protocol_specification&amp;action=edit&amp;section=11" title="Edit section: blockchain.address.subscribe">edit</a>]</h3>

          <p>A request to send to the client notifications when status
            (i.e., transaction history) of the given address changes.
            Status is a hash of the transaction history. If there isn't
            any transaction for the address yet, the status is null.</p>

          <p><b>request:</b> { "id": 6, "method":
            "blockchain.address.subscribe", "params": [
            "1NS17iag9jJgTHD1VXjvLCEnZuQ3rJDE9L" ] }<br/>
            <b>response:</b> { "id": 6, "result":
            "b87bc42725143f37558a0b41a664786d9e991ba89d43a53844ed7b3752545d4f"
            } }<br/>
            <b>message:</b> { "id": null, "method":
            "blockchain.address.subscribe", "params": [
            "1NS17iag9jJgTHD1VXjvLCEnZuQ3rJDE9L",
            "690ce08a148447f482eb3a74d714f30a6d4fe06a918a0893d823fd4aca4df580"
            ] }</p>

          <h3>blockchain.address.get_history[<a href="https://electrum.orain.org/w/index.php?title=Stratum_protocol_specification&amp;action=edit&amp;section=12" title="Edit section: blockchain.address.get history">edit</a>]</h3>

          <p><b>request&nbsp;:</b> {"id": 1, "method":
            "blockchain.address.get", "params":
            ["1NS17iag9jJgTHD1VXjvLCEnZuQ3rJDE9L"] }<br/>
            <b>response&nbsp;:</b> {"id": 1, "result": [{"tx_hash":
            "ac9cd2f02ac3423b022e86708b66aa456a7c863b9730f7ce5bc24066031fdced",
            "height": 340235}, {"tx_hash":
            "c4a86b1324f0a1217c80829e9209900bc1862beb23e618f1be4404145baa5ef3",
            "height": 340237}]}<br/>
          </p>

          <h3>blockchain.address.get_mempool[<a href="https://electrum.orain.org/w/index.php?title=Stratum_protocol_specification&amp;action=edit&amp;section=13" title="Edit section: blockchain.address.get mempool">edit</a>]</h3>

          <h3>blockchain.address.get_balance[<a href="https://electrum.orain.org/w/index.php?title=Stratum_protocol_specification&amp;action=edit&amp;section=14" title="Edit section: blockchain.address.get balance">edit</a>]</h3>

          <p><b>request&nbsp;:</b> { "id": 1, "method":
            "blockchain.address.get_balance", "params":
            ["1NS17iag9jJgTHD1VXjvLCEnZuQ3rJDE9L"] }<br/>
            <b>response&nbsp;:</b> {"id": 1, "result": {"confirmed":
            533506535, "unconfirmed": 27060000}}<br/>
          </p>

          <h3>blockchain.address.get_proof[<a href="https://electrum.orain.org/w/index.php?title=Stratum_protocol_specification&amp;action=edit&amp;section=15" title="Edit section: blockchain.address.get proof">edit</a>]</h3>

          <h3>blockchain.address.listunspent[<a href="https://electrum.orain.org/w/index.php?title=Stratum_protocol_specification&amp;action=edit&amp;section=16" title="Edit section: blockchain.address.listunspent">edit</a>]</h3>

          <p><b>request&nbsp;:</b> { "id": 1, "method":
            "blockchain.address.listunspent", "params":
            ["1NS17iag9jJgTHD1VXjvLCEnZuQ3rJDE9L"] }<br/>
            <b>response&nbsp;:</b>{"id": 1, "result": [{"tx_hash":
            "561534ec392fa8eebf5779b233232f7f7df5fd5179c3c640d84378ee6274686b",
            "tx_pos": 0, "value": 24990000, "height": 340242},
            {"tx_hash":
            "620238ab90af02713f3aef314f68c1d695bbc2e9652b38c31c025d58ec3ba968",
            "tx_pos": 1, "value": 19890000, "height": 340242}]}</p>

          <h3>blockchain.utxo.get_address[<a href="https://electrum.orain.org/w/index.php?title=Stratum_protocol_specification&amp;action=edit&amp;section=17" title="Edit section: blockchain.utxo.get address">edit</a>]</h3>

          <h3>blockchain.block.get_header[<a href="https://electrum.orain.org/w/index.php?title=Stratum_protocol_specification&amp;action=edit&amp;section=18" title="Edit section: blockchain.block.get header">edit</a>]</h3>

          <h3>blockchain.block.get_chunk[<a href="https://electrum.orain.org/w/index.php?title=Stratum_protocol_specification&amp;action=edit&amp;section=19" title="Edit section: blockchain.block.get chunk">edit</a>]</h3>

          <h3>blockchain.transaction.broadcast[<a href="https://electrum.orain.org/w/index.php?title=Stratum_protocol_specification&amp;action=edit&amp;section=20" title="Edit section: blockchain.transaction.broadcast">edit</a>]</h3>

          <h3>blockchain.transaction.get_merkle[<a href="https://electrum.orain.org/w/index.php?title=Stratum_protocol_specification&amp;action=edit&amp;section=21" title="Edit section: blockchain.transaction.get merkle">edit</a>]</h3>

          <p>blockchain.transaction.get_merkle [$txid, $txHeight]</p>

          <h3>blockchain.transaction.get[<a href="https://electrum.orain.org/w/index.php?title=Stratum_protocol_specification&amp;action=edit&amp;section=22" title="Edit section: blockchain.transaction.get">edit</a>]</h3>

          <p>Method for obtaining raw transaction (hex-encoded) for
            given txid. If the transaction doesn't exist, an error is
            returned.</p>

          <p><b>request:</b> { "id": 17, "method":
            "blockchain.transaction.get", "params": [
            "0e3e2357e806b6cdb1f70b54c3a3a17b6714ee1f0e68bebb44a74b1efd512098"
            ] }<br/>
            <b>response:</b> { "id": 17, "result":
            "01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff0704ffff001d0104ffffffff0100f2052a0100000043410496b538e853519c726a2c91e61ec11600ae1390813a627c66fb8be7947be63c52da7589379515d4e0a604f8141781e62294721166bf621e73a82cbf2342c858eeac00000000"
            }<br/>
            <b>error</b>: { "id": 17, "error": "{ u'message': u'No
            information available about transaction', u'code': -5 }" }</p>

          <h2>External links[<a href="https://electrum.orain.org/w/index.php?title=Stratum_protocol_specification&amp;action=edit&amp;section=23" title="Edit section: External links">edit</a>]</h2>

          <ul>
            <li> <a class="external text" href="https://docs.google.com/a/palatinus.cz/document/d/17zHy1SUlhgtCMbypO8cHgpWH73V5iUQKk_0rWvMqSNs/edit?hl=en_US" rel="nofollow">original Slush's specification of Stratum
              protocol</a></li>

            <li> <a class="external text" href="http://mining.bitcoin.cz/stratum-mining" rel="nofollow">specification of Stratum mining
              extension</a></li>
          </ul>
        </div>
