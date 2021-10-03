Using the most current Electrum on Tails
========================================

Software installed on Tails cannot be permanently upgraded since it is a fixed (read-only) image. You can run the most recent version of Electrum with Tails by using the AppImage binary we distribute (a self-contained executable that should work on any x86_64 Linux including Tails).

Tails version 4 (since October 2019) ships with a working version of Electrum at the time of its release - these instructions can be used to run the latest version of Electrum between Tails/Debian releases.

Tails version 3 (prior to October 2019) ships with an outdated version of Electrum that can no longer be used on the public Electrum server network. It is recommended instead to upgrade to the latest Tails since it will have many other security improvements as well.

These steps have been tested on Tails versions 3 and 4.

Steps to use AppImage
---------------------

1. Write down your wallet seed words and store them securely off the computer.
2. Enable and configure persistent storage. In Tails enter the Applications/Tails menu and select "Configure persistent volume". Ensure "Personal data" and "Bitcoin client" sliders are enabled. Reboot if necessary and make sure the persistent volume is unlocked.
3. Ensure your Tails is connected to a network and the onion icon at the top confirms Tor network is ready. 
4. Using Tor browser download the Linux Appimage file under "Sources and Binaries" near the top of the download page on electrum.org_  and save it to the default "Tor browser" folder. Tails and Tor are not as fast as your regular operating system, and the download may take much longer than normally expected especially if you have a slow computer or USB drive - Tor download speed depends entirely on the Tor network connections. Your AppImage will not start nor will it give any error message if you do not download the entire file.
5. Open Home/Tor browser folder and drag the appimage to the Persistent folder (lower left side of the window). Tails is very sensitive to user writeable file locations and Electrum may not work in another location.
6. Recommended: Check the PGP signature of the AppImage by following these_ instructions before using the AppImage.
7. Open Home/Persistent folder (where the appimage will now live), right click on the appimage and select Properties. Select the Permissions tab and click "Allow executing file as program" then close the dialog. More detailed instructions with screenshots are available here_.

.. _electrum.org: https://electrum.org/#download
.. _here: https://docs.appimage.org/user-guide/run-appimages.html
.. _these: https://github.com/spesmilo/electrum-docs/blob/master/gpg-check.rst#verifying-gpg-signature-of-electrum-using-linux-command-line 

You can now simply click on the Electrum AppImage icon in your persistent folder to run the newest Electrum. Your new AppImage should use any previous Electrum data (if there is any) without difficulty and the wallet(s) will remain on your Tails USB drive if you've enabled persistent storage. If there is any question about your wallet(s) being corrupted, erase the files in ~/.electrum/wallets and reinitialize from seed words. 

**Caution:** Do not use the old Electrum available in the Tails version 3 menus. 
