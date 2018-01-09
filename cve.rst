Jsonrpc vulnerability in Electrum 2.6 to 3.0.4
==============================================

On January 6th, a vulnerability was disclosed in the Electrum wallet
software, that allows malicious websites to execute wallet commands
through JSONRPC executed in a web browser. The bug affects versions
2.6 to 3.0.3 of Electrum, on all platforms. It also affects clones of
Electrum such as Electron Cash.


Can funds be stolen?
--------------------

Wallets that are not password-protected are at risk of theft, if they
are opened with an version of Electrum older that 3.0.5 while a web
browser is active.

In addition, the vulnerability allows an attacker to modify user
settings, the list of contacts in a wallet, and the "payto" and
"amount" fields of the user interface while Electrum is running.

Although there is no known occurrence of Bitcoin theft occurring
because of this vulnerability, the risk increases substantially now
that the vulnerability has been made public.


Can wallet data be leaked?
--------------------------

Yes, an attacker can obtain private data, such as: Bitcoin addresses,
transaction labels, address labels, wallet contacts and master public
keys.


Can a password-protected wallet be bruteforced?
-----------------------------------------------

Not realistically. The vulnerability does not allow an attacker to
access encrypted seed or private keys, which would be needed in order
to perform an efficient brute force attack. Without the encrypted
seed, an attacker must try passwords using the JSONRPC interface,
while the user is visiting a malicious page. This is several orders of
magnitude slower than an attack with the encrypted seed, and
restricted in time. Even a weak password will protect against that.


What should users do?
---------------------

All users should upgrade their Electrum software, and stop using old
versions.

Users who did not protect their wallet with a password should create a
new wallet, and move their funds to that wallet. Even if it never
received any funds, a wallet without password should not be used
anymore, because its seed might have been compromised.

In addition, users should review their settings, and delete all
contacts from their contacts list, because the Bitcoin addresses of
their contacts might have been modified.


How to upgrade Electrum
-----------------------

Stop running any version of Electrum older than 3.0.5, and install
Electrum 3.0.5. On desktop, make sure you download Electrum from
https://electrum.org and no other website. On Android, version 3.0.5
is available in Google Play.

If Electrum 3.0.5 cannot be installed or does not work on your
computer, stop using Electrum on that computer, and access your funds
from a device that can run Electrum 3.0.5. If you really need to use
an older version of Electrum, for example in order to access wallet
seed, make sure that your computer is offline, and that no web browser
is running on the computer at the same time.


Should users move their funds to a new address?
-----------------------------------------------

We do not recommend to move your funds if your wallet was password
protected. Even for wallets that have no password, moving funds is an
extreme precaution, that might not be necessary; indeed, if your
wallet had been compromised, it is very likely that the attacker would
have stolen the funds immediately.


How long was the issue known before it was fixed?
-------------------------------------------------

The absence of password protection in the jsonrpc interface was first
reported on November 25, 2017:
https://github.com/spesmilo/electrum/issues/3374

The initial bug report was about the Electrum daemon, a piece of
software that runs on web servers and is used by merchants in order to
receive Bitcoin payments. In that context, connections to the daemon
from the outside world must be explicitly authorized, by setting
'rpchost' and 'rpcport' in your Electrum configuration. At that point,
we did not realize that this was creating a vulnerability.

On January 6th, 2018, Tavis Omandy demonstrated that the jsonrpc
interface could be exploited against the Electrum GUI, and that the
attack could be carried out by a web browser running locally, visiting
a webpage with specially crafted javascript.

We released a new version (3.0.4) in the hours following Tavis' post,
with a patch written by mithrandi (Debian packager), that addressed
the attack demonstrated by Tavis. In addition, the github remained
open, because mithrandi's patch was not adding password protection to
the jsonrpc interface.

Shortly after the 3.0.4 release we started to work on adding proper
password protection to the JSONRPC interface of the daemon, and that
part was ready on Sunday, January 7th. We also learned on Sunday
afternoon that the first patch was not effective against another,
similar attack, using POST. This is why we did not delay the 3.0.5
release, which includes password protection, and completely disables
JSONRPC in the GUI.
