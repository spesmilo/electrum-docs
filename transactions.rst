Serialization of unsigned or partially signed transactions
==========================================================

          <p>Electrum 2.0 uses an extended serialization format for
            transactions.<br/>
            The purpose of this format is to send unsigned and
            partially signed transactions to cosigners or to cold
            storage.<br/>
            This is achieved by extending the 'pubkey' field of a
            transaction input.<br/>
          </p>

          <div class="toc" id="toc">
            <div id="toctitle">
              <h2>Contents</h2>
            </div>

            <ul>
              <li class="toclevel-1 tocsection-1"><a href="#Extended_public_keys">1 Extended public keys</a></li>

              <li class="toclevel-1 tocsection-2"><a href="#Public_key">2 Public key</a></li>

              <li class="toclevel-1 tocsection-3"><a href="#BIP32_derivation">3 BIP32 derivation</a></li>

              <li class="toclevel-1 tocsection-4"><a href="#Legacy_Electrum_Derivation">4 Legacy Electrum
                Derivation</a></li>

              <li class="toclevel-1 tocsection-5"><a href="#Bitcoin_address">5 Bitcoin address</a></li>
            </ul>
          </div>

          <h3>Extended public keys[<a href="https://electrum.orain.org/w/index.php?title=Serialization_format_of_transactions&amp;action=edit&amp;section=1" title="Edit section: Extended public keys">edit</a>]</h3>

          <p>The first byte of the pubkey indicates if it is an
            extended pubkey:</p>

          <ul>
            <li> 0x02, 0x03, 0x04&nbsp;: legal Bitcoin public key
              (compressed or not)</li>

            <li> 0xFF, 0xFE, 0xFD&nbsp;: extended public key.</li>
          </ul>

          <p>Extended public keys are of 3 types:</p>

          <ul>
            <li> 0xFF&nbsp;: bip32 xpub and derivation</li>

            <li> 0xFE&nbsp;: legacy electrum derivation: master public
              key + derivation</li>

            <li> 0xFD&nbsp;: unknown pubkey, but we know the Bitcoin
              address</li>
          </ul>

          <p><br/>
          </p>

          <h3>Public key[<a href="https://electrum.orain.org/w/index.php?title=Serialization_format_of_transactions&amp;action=edit&amp;section=2" title="Edit section: Public key">edit</a>]</h3>

          <p>This is the legit Bitcoin serialization of public keys.</p>

          <table class="wikitable">
            <tbody>
              <tr>
                <td> 0x02 or 0x03</td>

                <td> compressed public key (32 bytes)</td>
              </tr>

              <tr>
                <td> 0x04</td>

                <td> uncompressed public key (64 bytes)</td>
              </tr>
            </tbody>
          </table>

          <h3>BIP32 derivation[<a href="https://electrum.orain.org/w/index.php?title=Serialization_format_of_transactions&amp;action=edit&amp;section=3" title="Edit section: BIP32 derivation">edit</a>]</h3>

          <table class="wikitable">
            <tbody>
              <tr>
                <td> 0xFF</td>

                <td> xpub (78 bytes)</td>

                <td> bip32 derivation (2*k bytes)</td>
              </tr>
            </tbody>
          </table>

          <h3>Legacy Electrum Derivation[<a href="https://electrum.orain.org/w/index.php?title=Serialization_format_of_transactions&amp;action=edit&amp;section=4" title="Edit section: Legacy Electrum Derivation">edit</a>]</h3>

          <table class="wikitable">
            <tbody>
              <tr>
                <td> 0xFE</td>

                <td> mpk (64 bytes)</td>

                <td> derivation (4 bytes)</td>
              </tr>
            </tbody>
          </table>

          <h3>Bitcoin address[<a href="https://electrum.orain.org/w/index.php?title=Serialization_format_of_transactions&amp;action=edit&amp;section=5" title="Edit section: Bitcoin address">edit</a>]</h3>

          <p>Used if we don't know the public key, but we know the
            address (or the hash 160 of the output script). The
            cosigner should know the public key.</p>

          <table class="wikitable">
            <tbody>
              <tr>
                <td> 0xFD</td>

                <td> hash_160_of_script (20 bytes)</td>
              </tr>
            </tbody>
          </table>
        </div>
