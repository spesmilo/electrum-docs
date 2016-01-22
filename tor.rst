Using Electrum Through Tor
==========================================================

Please note that when using electrum through tor there is two main ways.
The first way has the most Privacy but also requires the most trust in the server you are connecting too. This is because normally
Electrum connects to a few different servers and downloads block headers and checks that they match. This prevents / makes it more difficult for 
Rogue servers to send you bad information. However this can also present a privacy issue because you could be connecting to none .onion servers for these headers.

Thus the two different options are, Connect to 1 server ONLY and get block headers and transaction info from that server.
Or
Connect to 8 block header servers and connect to 1 .onion server for the general use.

List of Active .onion servers
-----------------------------
Check the list here;

http://electrumserv.noip.me/onionservers.txt

If you wish to be added to this list email me at:

danielcryptos@gmail.com


LINUX
-----

Option 1: Single Server
-----------------------

Note: Please understand you are sacrificing some security here for extra privacy.


Check out https://electrum.org/#download

Grab the download from python source

Make sure you have dependencies installed

sudo apt-get install python-qt4 python-pip


Extract the electrum download;

tar -xvzf Electrum-2.*.*.tar.gz

Go into the extracted electrum folder and then run;

electrum -1 -s electrumaay7a3lc.onion:50001:t -p socks5:localhost:9050

Quick explanation,

-1 means connect to 1 server only.

-s is defining which server. You can change this to any .onion server you want. (Check the list at the top)

-p Is saying what proxy server to use to get into the tor network. Generally this will be localhost but the port bit after : could be different.

You might need to change the port bit depending on what system you are running;

Currently The port is;

Tor Browser Bundle: 9150

General Tor (Installed): 9050


Option 2: Multiple servers but Tor Main
---------------------------------------
Same as above until the command to launch electrum, Remove the -1 making it

electrum -s electrumaay7a3lc.onion:50001:t -p socks5:localhost:9050

For this one you can also just launch electrum and click on the Green or Red icon on the bottom right to bring up server information

Untick the box for Auto and enter;

electrumaay7a3lc.onion

50001

Into the boxes.

At the bottom select SOCKS5 for proxy and then

localhost

9150 or 9050


WINDOWS
-------


Option 1: Connecting to a single Server
---------------------------------------
Install electrum from the main download page;
https://electrum.org/#download

Note: Please understand you are sacrificing some security here for extra privacy.

In windows, On your desktop you will have a electrum icon. Copy and paste this to make a copy. If not you can find the electrum folder in C:\Program Files (x86)\Electrum\

Right click on electrum.exe and create shortcut. It will say cannot make a shortcut here make one on the desktop instead? Ok this.

With your new shortcut or a copy of your old one Right click it and go properties, click shortcut at the top bar, in the box named target:

It should already say something similar to what’s in between the speech bubbles. If yours is different don’t change that bit to match.

What we want to do is add on the bit after the last speech bubble. Make a space and then enter / copy and paste.

"C:\Program Files (x86)\Electrum\electrum.exe" -1 -s electrumaay7a3lc.onion:50001:t -p socks5:localhost:9050

Apply and Ok the change... You can go back to the General Tab if you want and Where it says "electrum.exe - Shortcut" you could change that to Electrum - Tor or something

Click apply and ok again.

Now when you launch Electrum with this shortcut it will use 1 tor server only.

Quick explanation,

-1 means connect to 1 server only.

-s is defining which server. You can change this to any .onion server you want.

-p Is saying what proxy server to use to get into the tor network. Generally this will be localhost but the port bit after : could be different.

You might need to change the port bit depending on what system you are running;

Currently The port is;

Tor Browser Bundle: 9150

General Tor (Installed): 9050

Option 2
----------
In windows, On your desktop you will have a electrum icon. Copy and paste this to make a copy. If not you can find the electrum folder in C:\Program Files (x86)\Electrum\

Right click on electrum.exe and create shortcut. It will say cannot make a shortcut here make one on the desktop instead? Ok this.

With your new shortcut or a copy of your old one Right click it and go properties, click shortcut at the top bar, in the box named target:

It should already say something similar to what’s in between the speech bubbles. If yours is different don’t change that bit to match.

What we want to do is add on the bit after the last speech bubble. Make a space and then enter / copy and paste.


"C:\Program Files (x86)\Electrum\electrum.exe" -s electrumaay7a3lc.onion:50001:t -p socks5:localhost:9050

Apply and Ok the change... You can go back to the General Tab if you want and Where it says "electrum.exe - Shortcut" you could change that to Electrum - Tor or something

Click apply and ok again.

Now when you launch Electrum with this shortcut it will use 1 tor server only.

You might need to change the port bit depending on what system you are running;

Currently The port is;

Tor Browser Bundle: 9150

General Tor (Installed): 9050


For this one you can also just launch electrum and click on the Green or Red icon on the bottom right to bring up server information
Untick the box for Auto and enter;

electrumaay7a3lc.onion

50001

Into the boxes.

At the bottom select SOCKS5 for proxy and then

localhost

9150 or 9050
