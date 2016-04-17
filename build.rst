Build Electrum on Mac OS X
==========================

.. raw:: html

  <div>
    <ul>
      <li class="toclevel-1 tocsection-1"><a href="#Compile_Electrum_.28master.29_on_a_fresh_MacOS_X_Yosemite_.2810.10.5.29_install">1
        Compile Electrum (master) on a fresh MacOS X Yosemite
        (10.10.5) install</a>
        <ul>
          <li class="toclevel-2 tocsection-2"><a href="#Install_Brew_.28http:.2F.2Fbrew.sh.29">1.1
            Install Brew (http://brew.sh)</a></li>

          <li class="toclevel-2 tocsection-3"><a href="#Update_brew">1.2 Update brew</a></li>

          <li class="toclevel-2 tocsection-4"><a href="#Install_python_.28and_thus_pip.29_and_pyqt-4">1.3
            Install python (and thus pip) and pyqt-4</a></li>

          <li class="toclevel-2 tocsection-5"><a href="#Clone_Electrum_from_the_official_git_repository">1.4
            Clone Electrum from the official git repository</a></li>

          <li class="toclevel-2 tocsection-6"><a href="#Install_the_Electrum_module.28s.29">1.5
            Install the Electrum module(s)</a></li>

          <li class="toclevel-2 tocsection-7"><a href="#You_may_want_to_add_the_following_modules_as_well">1.6
            You may want to add the following modules as
            well</a></li>

          <li class="toclevel-2 tocsection-8"><a href="#Link_all_apps">1.7 Link all apps</a></li>

          <li class="toclevel-2 tocsection-9"><a href="#Generate_icons">1.8 Generate icons</a></li>

          <li class="toclevel-2 tocsection-10"><a href="#Compile_the_Electrum_application">1.9
            Compile the Electrum application</a></li>

          <li class="toclevel-2 tocsection-11"><a href="#Build_the_dmg_container">1.10 Build the dmg
            container</a></li>
        </ul>
      </li>

      <li class="toclevel-1 tocsection-12"><a href="#Things_that_need_to_be_fixed_atm">2 Things that
        need to be fixed atm</a>
        <ul>
          <li class="toclevel-2 tocsection-13"><a href="#Incorrect_ca_path">2.1 Incorrect ca_path</a></li>

          <li class="toclevel-2 tocsection-14"><a href="#Invalid_DEFAULT_CA_BUNDLE_PATH">2.2 Invalid
            DEFAULT_CA_BUNDLE_PATH</a></li>

          <li class="toclevel-2 tocsection-15"><a href="#Crash_when_clicking_on_the_qrcode_icon_in_the_.E2.80.9CPay_to.E2.80.9D_field_of_the_.E2.80.9CSend.E2.80.9D_tab">2.3
            Crash when clicking on the qrcode icon in the
            “Pay to” field of the “Send” tab</a></li>

          <li class="toclevel-2 tocsection-16"><a href="#Plot_History_plugin_doesn.E2.80.99t_work">2.4
            Plot History plugin doesn’t work</a></li>

          <li class="toclevel-2 tocsection-17"><a href="#Preference_panel_does_not_work">2.5
            Preference panel does not work</a></li>

          <li class="toclevel-2 tocsection-18"><a href="#.5BErrno_20.5D_Not_a_directory">2.6 [Errno
            20] Not a directory</a></li>

          <li class="toclevel-2 tocsection-19"><a href="#Audio_MODEM">2.7 Audio MODEM</a></li>
        </ul>
      </li>

      <li class="toclevel-1 tocsection-20"><a href="#Other_patches_.28optionals.29:">3 Other patches
        (optionals):</a>
        <ul>
          <li class="toclevel-2 tocsection-21"><a href="#Privacy_headers_url">3.1 Privacy
            headers_url</a></li>

          <li class="toclevel-2 tocsection-22"><a href="#Privacy_DEFAULT_SERVERS">3.2 Privacy
            DEFAULT_SERVERS</a></li>
        </ul>
      </li>
    </ul>
  </div>

  <h1>Compile Electrum (master) on a fresh MacOS X Yosemite
    (10.10.5) install</h1>

  <h2>Install Brew (<a class="external free" href="http://brew.sh/" rel="nofollow">http://brew.sh</a>)</h2>

  <pre>ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"</pre>

  <h2>Update brew</h2>

  <pre>brew update</pre>

  <h2>Install python (and thus pip) and pyqt-4</h2>

  <pre>brew install python pyqt</pre>

  <h2>Clone Electrum from the official git repository</h2>

  <pre>git clone https://github.com/spesmilo/electrum.git
  cd electrum</pre>

  <h2>Install the Electrum module(s)</h2>

  <pre>python setup.py sdist
  pip install --pre dist/Electrum-*tar.gz</pre>

  <h2>You may want to add the following modules as well</h2>

  <p>‘#’ are optionals</p>

  <pre>brew install gmp zbar # Required for gmpy (pip) and zbar (pip)

  pip install certifi cffi configparser crypto cryptography dnspython ecdsa gi gmpy html http jsonrpclib mercurial numpy ordereddict packaging pip ply pyOpenSSL pyasn1 pyasn1-modules pycparser pycrypto setuptools setuptools-svn simplejson wincertstore zbar # Some might be optional

  pip install cython trezor # Trezor support, only these two are needed (no need to have limbs or pyusb)

  #brew install homebrew/python/matplotlib # Required for Plot History (do not install via pip or Electrum will not compile)
  brew install homebrew/python/pillow # Needed for PIL imports as PIL is now depreciated (do not install via pip or Electrum will not compile)
  # pip install amodem # Audio Modem plugin (does not work for OS X)</pre>

  <h2>Link all apps</h2>

  <pre>brew linkapps</pre>

  <h2>Generate icons</h2>

  <pre>pyrcc4 icons.qrc -o gui/qt/icons_rc.py</pre>

  <h2>Compile the Electrum application</h2>

  <pre>ARCHFLAGS="-arch i386 -arch x86_64" sudo python setup-release.py py2app --includes sip</pre>

  <h2>Build the dmg container</h2>

  <pre>sudo hdiutil create -fs HFS+ -volname "Electrum" -srcfolder dist/Electrum.app dist/electrum-VERSION-macosx.dmg</pre>

  <hr/>

  <h1>Things that need to be fixed atm</h1>

  <h2>Incorrect ca_path</h2>

  <p>IN paymentrequest.py, line 44:</p>

  <pre>ca_path = requests.certs.where()</pre>

  <p>FIX: Which can be patched with (temporary and dirty
    solution):</p>

  <pre>#!/bin/sh

  echo "[...] Patching: cacert.pem"

  cp -f build/bdist.macosx-*/python2.7-standalone/app/collect/certifi/cacert.pem dist/Electrum.app/Contents/Resources/lib/python2.7/ &amp;&amp;\
  chmod 755 dist/Electrum.app/Contents/Resources/lib/python2.7/cacert.pem &amp;&amp;\
  sed -i.bak "s/requests.certs.where()/os.path.join(os.path.dirname(__file__), '..\/cacert.pem')/g" dist/Electrum.app/Contents/Resources/lib/python2.7/lib/paymentrequest.py &amp;&amp;\
  rm -f dist/Electrum.app/Contents/Resources/lib/python2.7/lib/paymentrequest.py.bak &amp;&amp;\
  echo "[OK] Patch applied successfully"</pre>

  <p>A proper solution would be to investigate how ca_path is
    obtained.</p>

  <p>It’s the way py2app packages the libs but I don’t know
    how to change that to have a directory instead of a zip
    archive. Similar issue also reported here: <a class="external free" href="http://stackoverflow.com/questions/28073033/running-pytest-on-module-inside-site-packages-zip" rel="nofollow">http://stackoverflow.com/questions/28073033/running-pytest-on-module-inside-site-packages-zip</a>
  </p>

  <h2>Invalid DEFAULT_CA_BUNDLE_PATH</h2>

  <p>IN electrum.py, line 403:</p>

  <pre>assert os.path.exists(requests.utils.DEFAULT_CA_BUNDLE_PATH)</pre>

  <p>FIX: Can be fixed by commenting the line (which is a
    temporary and dirty solution). A correct solution is to dig
    where the DEFAULT_CA_BUNDLE_PATH is set and correct it.</p>

  <pre>#!/bin/sh

  echo "[...] Patching: DEFAULT_CA_BUNDLE_PATH"

  sed -i.bak "s/assert *os.path.exists(requests.utils.DEFAULT_CA_BUNDLE_PATH)/#assert os.path.exists(requests.utils.DEFAULT_CA_BUNDLE_PATH)/g" dist/Electrum.app/Contents/Resources/electrum.py &amp;&amp;\
  rm -f dist/Electrum.app/Contents/Resources/electrum.py.bak &amp;&amp;\
  echo "[OK] Patch applied successfully"</pre>

  <h2>Crash when clicking on the qrcode icon in the “Pay
    to” field of the “Send” tab</h2>

  <p>FIX: Remove this feature to scan QR-Codes because it does
    not work on OSX.</p>

  <h2>Plot History plugin doesn’t work</h2>

  <p>The Plot History plugin does not work properly.</p>

  <p>In “Export History”, when clicking on “Preview
    plot”:</p>

  <pre>Jul 21 12:02:00 dev.local electrum[61643] &lt;Notice&gt;: Traceback (most recent call last):
  Jul 21 12:02:00 dev.local electrum[61643] &lt;Notice&gt;:   File "./Electrum.app/Contents/Resources/lib/python2.7/plugins/plot.py", line 42, in &lt;lambda&gt;
  Jul 21 12:02:00 dev.local electrum[61643] &lt;Notice&gt;:     b.clicked.connect(lambda: self.do_plot(self.wallet, history))
  Jul 21 12:02:00 dev.local electrum[61643] &lt;Notice&gt;:   File "./Electrum.app/Contents/Resources/lib/python2.7/plugins/plot.py", line 58, in do_plot
  Jul 21 12:02:00 dev.local electrum[61643] &lt;Notice&gt;:     tx_hash, confirmations, value, timestamp = item
  Jul 21 12:02:00 dev.local electrum[61643] &lt;Notice&gt;: ValueError: too many values to unpack</pre>

  <p>FIX:&nbsp;???</p>

  <h2>Preference panel does not work</h2>

  <p>The application crashes with “terminated by signal
    SIGSEGV (Address boundary error)”.</p>

  <p>Crash is due to this import (OS X does not seem to support
    video at all for qrscanner):</p>

  <pre>from electrum import qrscanner</pre>

  <p>FIX:</p>

  <pre>#!/bin/sh

  echo "[...] Patching: Preference pane (qrscanner)"

  sed -i.bak -n -e '/^ *def *read_tx_from_qrcode(self):/{' -e 'p' -e ':a' -e 'N' -e '/self.show_transaction(tx)/!ba' -e 's/.*\n/        return #/' -e '}' -e 'p' dist/Electrum.app/Contents/Resources/lib/python2.7/gui/qt/main_window.py &amp;&amp;\
  sed -i.bak -n -e '/^ *from *electrum *import *qrscanner/{' -e ':a' -e 'N' -e '/gui_widgets.append((qr_label, *qr_combo))/!ba' -e 's/.*\n/#/' -e '}' -e 'p' dist/Electrum.app/Contents/Resources/lib/python2.7/gui/qt/main_window.py &amp;&amp;\
  rm -f dist/Electrum.app/Contents/Resources/lib/python2.7/gui/qt/main_window.py.bak &amp;&amp;\
  echo "[OK] Patch applied successfully"</pre>

  <h2>[Errno 20] Not a directory</h2>

  <p>Plugins Labels and Exchange Rate seem to be impacted with
    this issue.</p>

  <p>This issue is caused by requests.request which returns:</p>

  <pre>[Errno 20] Not a directory</pre>

  <p>Maybe because requests is not properly installed, I
    don’t know&nbsp;:(.</p>

  <p>FIX:&nbsp;???</p>

  <h2>Audio MODEM</h2>

  <p>Does not work (activation fails) because MacOS Kernel
    ‘Darwin’ seems not to be supported</p>

  <pre>Jul 21 12:25:18 dev.local electrum[80139] &lt;Notice&gt;: Audio MODEM is available.
  Jul 21 12:25:18 dev.local electrum[80139] &lt;Notice&gt;: Traceback (most recent call last):
  Jul 21 12:25:18 dev.local electrum[80139] &lt;Notice&gt;:   File "./Electrum.app/Contents/Resources/lib/python2.7/gui/qt/main_window.py", line 2799, in &lt;lambda&gt;
  Jul 21 12:25:18 dev.local electrum[80139] &lt;Notice&gt;:     return lambda: do_toggle(cb, name, w)
  Jul 21 12:25:18 dev.local electrum[80139] &lt;Notice&gt;:   File "./Electrum.app/Contents/Resources/lib/python2.7/gui/qt/main_window.py", line 2789, in do_toggle
  Jul 21 12:25:18 dev.local electrum[80139] &lt;Notice&gt;:     plugins[name] = p = module.Plugin(self.config, name)
  Jul 21 12:25:18 dev.local electrum[80139] &lt;Notice&gt;:   File "./Electrum.app/Contents/Resources/lib/python2.7/plugins/audio_modem.py", line 36, in __init__
  Jul 21 12:25:18 dev.local electrum[80139] &lt;Notice&gt;:     }[platform.system()]
  Jul 21 12:25:18 dev.local electrum[80139] &lt;Notice&gt;: KeyError: 'Darwin'</pre>

  <hr/>

  <h1>Other patches (optionals):</h1>

  <h2>Privacy headers_url</h2>

  <p>Remove headers_url to prevent the client to download the
    header file from a centralized/untrusted server (no
    offense):</p>

  <pre>#!/bin/sh

  echo "[...] Patching: headers_url"

  sed -i.bak "s/self.headers_url *= *'.*'/self.headers_url = ''/g" dist/Electrum.app/Contents/Resources/lib/python2.7/lib/blockchain.py &amp;&amp;\
  rm -f dist/Electrum.app/Contents/Resources/lib/python2.7/lib/blockchain.py.bak &amp;&amp;\
  echo "[OK] Patch applied successfully"</pre>

  <h2>Privacy DEFAULT_SERVERS</h2>

  <p>Remove all (untrusted) DEFAULT_SERVERS:</p>

  <pre>#!/bin/sh

  echo "[...] Patching: DEFAULT_SERVERS"

  sed -i.bak -n -e '/^ *DEFAULT_SERVERS *= *{/{' -e 'p' -e ':a' -e 'N' -e '/}$/!ba' -e 's/.*\n//' -e '}' -e 'p' dist/Electrum.app/Contents/Resources/lib/python2.7/lib/network.py &amp;&amp;\
  rm -f dist/Electrum.app/Contents/Resources/lib/python2.7/lib/network.py.bak &amp;&amp;\
  echo "[OK] Patch applied successfully"</pre>

  <p>Note: You’ll either need to add some manually to this
    list or add yours to your Electrum ~/.electrum/config file
    (“server”: “your server.com:50002:s”,) otherwise
    the application will not launch if this is the first time
    you use it. Also make sure to remove the
    ~/.electrum/recent_servers file (to avoid your client to
    connect to previous servers).</p>
