Tails currently ships with an outdated and insecure version of Electrum that can no longer be used on the public Electrum server network as of March 2019. Unfortunately installed software on Tails cannot be permanently upgraded since it is a fixed (read-only) image - you have to wait for Tails to upgrade.

However, you can still use the most current Electrum with Tails that eliminates the phishing message and includes other improvements. Electrum distributes an appimage which is a self-contained file that works on Tails (a linux distribution). These steps work on the current Tails (3.12.1) but may work on older versions too:

1. Write down your wallet seed words and store them securely off the computer.
2. Enable and configure persistent storage: from Applications/Tails menu select "Configure persistent volume" and ensure "Personal data" and "Bitcoin client" sliders are enabled. Reboot if necessary and make sure the persistent volume is unlocked.
3. Download the Linux Appimage file under "Sources and Binaries" near the top of the page from electrum.org using Tor browser and save it to the default "Tor browser" folder.
4. Open Home/Tor browser folder and drag appimage to Persistent folder (lower left side of the window). Tails is very sensitive to user writeable file locations and Electrum may not work in others.
5. Open Home/Persistent folder (where the appimage will now live), right click on the appimage, select permissions tab and click "Allow executing file as program" then close the dialog. More detailed instructions with screenshots are here.

Now you can simply click on the appimage icon in your persistent folder to run Electrum. Your wallet can be recreated by re-entering the seed words when prompted. This image and any data (wallets) it creates will remain on your Tails USB drive as long as you've saved it to persistent storage.
