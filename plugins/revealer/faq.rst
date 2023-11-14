FAQ
===

What is the Revealer card?
--------------------------

A secure, visual representation of an ecryption key.


What is the Secret card?
------------------------

A secure, visual representation of a secret encrypted by the Revealer.


Can I reuse a Revealer to encrypt multiple secrets?
---------------------------------------------------

Yes, but you shouldn't.

The Revealer is a one time pad, it only has perfect security as long as it’s
used once. An adversary in possession of multiple Secrets, encrypted by the same
Revealer, may be able to attack the Revealer. Depending on your threat model you
might want to have more than one secret encrypted by the same Revealer. In this
case, you need to make sure an adversary has no way of accessing two (or more)
different Secrets encrypted by the same Revealer.


Can I encrypt other secrets that are not an Electrum seed?
----------------------------------------------------------

Yes, you can encrypt any alphanumeric string. Use the ‘custom secret’ field at
the encryption dialog of the software. BIP 39 and AEZEED seeds will fit on the
card, but will have a smaller font size. The software will adjust the font size
automatically after a certain amount of characters.


How is the noise generated?
---------------------------

The deterministic noise is generated with the provably secure HMAC_DRBG
(SHA-512) algorithm, seeded with 128 bits of entropy from the cryptographically
secure /dev/urandom.


Why should I use it?
--------------------

Unencrypted secrets may still be vulnerable to physical attacks (e.g., theft or
copying). If your secrets are encrypted, an adversary with physical access can't
read them. This allows you to create redundant backups without reducing safety.
Ultimately it adds a layer of noise to your seed or password. Encrypting it
visually, in two-factors, has the benefit that it doesn't require computers or
expertise to decrypt.


How to reveal the secret?
-------------------------

Place your Revealer card precisely on top of the Secret card.

Observing the marks on diagonally opposing corners and pressing the card
slightly down will give you a good image.


What happens if I mistype the Revealer code?
--------------------------------------------

The code includes a checksum so the software detects it and does not let you
proceed.


What are the codes on the Revealers and Secrets?
-------------------------------------------------

On the Revealer, the first digit is the version number, followed by a 32 digit
random seed (128 bits of entropy in hex format) used to generate the pattern,
and finally a three digit checksum (the least important bits of
``SHA256(version number + seed)``).

On the Secret, the code consists of a version number and checksum (formatted as
`VersionNumber_Checksum`). It's an identifier to facilitate matching it with the
correct Revealer. It can't be used to reverse engineer the Revealer.


Why only 128 bits?
------------------

If you can break 128 bits you can break bitcoin directly and won’t bother
breaking revealer.


I printed the PDFs but the cards don't line up.
-----------------------------------------------

Make sure that you print your PDF at 100% size, not ‘fit to paper’. If you still
have difficulties reading your secrets, you might want to use the Printer
Calibration tool.


What is printer calibration and how does it work?
-------------------------------------------------

Printer calibration allows you to generate a PDF that is adjusted to your
printer/paper. Each printer/paper will have (at least) a sub-milimiter
difference in the size they print out. Revealer is a precision device, if those
differences are big enough it might not be possible to read all the words at the
same time, rather one line or a word a time depending on how big the size
difference is.
