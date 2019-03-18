Using the most current Electrum on Tails
========================================

Tails currently ships with an outdated version of Electrum that can no longer be used on the public Electrum server network as of March 2019. Unfortunately installed software on Tails cannot be permanently upgraded since it is a fixed (read-only) image - you have to wait for Tails to upgrade.

However, you can use a recent version of Electrum with Tails by using the AppImage binary we distribute (a self-contained executable that works on x86_64 Linux (including Tails)). 

These steps have been tested on Tails 3.12.1.

Steps to use appimage
---------------------

1. Write down your wallet seed words and store them securely off the computer.
2. Enable and configure persistent storage. In Tails enter the Applications/Tails menu and select "Configure persistent volume". Ensure "Personal data" and "Bitcoin client" sliders are enabled. Reboot if necessary and make sure the persistent volume is unlocked.
3. Using Tor browser download the Linux Appimage file under "Sources and Binaries" near the top of the download page on electrum.org_  and save it to the default "Tor browser" folder.
4. Open Home/Tor browser folder and drag appimage to the Persistent folder (lower left side of the window). Tails is very sensitive to user writeable file locations and Electrum may not work in another location.
5. Open Home/Persistent folder (where the appimage will now live), right click on the appimage, select permissions tab and click "Allow executing file as program" then close the dialog. More detailed instructions with screenshots are available here_.

.. _electrum.org: https://electrum.org/#download
.. _here: https://docs.appimage.org/user-guide/run-appimages.html

Now you can simply click on the appimage icon in your persistent folder to run Electrum. Your wallet can be recreated by re-entering the seed words when prompted. This image and any data (wallets) it creates will remain on your Tails USB drive as long as you've saved it to persistent storage.
