Electrum seed phrases
=====================


          <p>Note: Electrum is not compatible with BIP39.</p>

          <p>Electrum uses a seed phrase made of natural language words
            in order to derive wallet private keys.</p>

          <p>In order to derive the keys in a way that does not depend
            on the wordlist, Electrum uses a hash of the UTF8
            normalized seed phrase. That part is similar to BIP39.
            However, the checksum mechanism is different. BIP39
            requires a predetermined wordlist in order to compute the
            checksum. In contrast, Electrum uses another hash of the
            seed phrase. That hash is used both as a checksum and as a
            version number.</p>

          <div class="toc" id="toc">
            <div id="toctitle">
              <h2>Contents</h2>
            </div>

            <ul>
              <li class="toclevel-1 tocsection-1"><a href="#seed_phrase_normalization">1 seed phrase
                normalization</a></li>

              <li class="toclevel-1 tocsection-2"><a href="#checksum_and_version_number">2 checksum and
                version number</a></li>

              <li class="toclevel-1 tocsection-3"><a href="#current_prefixes_used">3 current prefixes
                used</a></li>

              <li class="toclevel-1 tocsection-4"><a href="#entropy_loss">4 entropy loss</a></li>

              <li class="toclevel-1 tocsection-5"><a href="#length_of_the_seed_phrase">5 length of the seed
                phrase</a></li>
            </ul>
          </div>

          <h3>seed phrase normalization[<a href="https://electrum.orain.org/w/index.php?title=Electrum_seed_phrases&amp;action=edit&amp;section=1" title="Edit section: seed phrase normalization">edit</a>]</h3>

          <pre>normalized_seedphrase = mnemonic.prepare_seed(seed_phrase)
</pre>

          <p><br/>
            Note that the normalization function removes diacritics and
            also spaces between asian CJK characters (this differs from
            bip39).</p>

          <h3>checksum and version number[<a href="https://electrum.orain.org/w/index.php?title=Electrum_seed_phrases&amp;action=edit&amp;section=2" title="Edit section: checksum and version number">edit</a>]</h3>

          <p>The following hash is used:</p>

          <pre>s = hmac_sha_512("Seed version", normalized_seedphrase)
</pre>

          <p>The first bits of s (prefix) must be in a list of accepted
            prefixes. <br/>
            The length of the prefix is given by the first 4 bits of
            the prefix:</p>

          <pre>length = 8 + 4*n</pre>

          <h3>current prefixes used[<a href="https://electrum.orain.org/w/index.php?title=Electrum_seed_phrases&amp;action=edit&amp;section=3" title="Edit section: current prefixes used">edit</a>]</h3>

          <ul>
            <li> 0x01 -&gt; standard wallet (single account)</li>

            <li> 0x101 -&gt; two-factor authentication wallet (long
              seed used to derive two master keys)</li>
          </ul>

          <h3>entropy loss[<a href="https://electrum.orain.org/w/index.php?title=Electrum_seed_phrases&amp;action=edit&amp;section=4" title="Edit section: entropy loss">edit</a>]</h3>

          <p>The seed generation requires to find a seed that has a
            legal version prefix. That constraint results in a loss of
            entropy. This loss is compensated by adding extra bits of
            entropy during the seed generation.</p>

          <h3>length of the seed phrase[<a href="https://electrum.orain.org/w/index.php?title=Electrum_seed_phrases&amp;action=edit&amp;section=5" title="Edit section: length of the seed phrase">edit</a>]</h3>

          <p>In order to generate a seedphrase with 128 bits of entropy
            and 8 bits of prefix, a wordlist of 2048 words will
            typically use 13 words.<br/>
            It is possible to fall back to 12 words seedphrases by
            making the wordlist longer (about 2600 words are needed)</p>
        </div>
