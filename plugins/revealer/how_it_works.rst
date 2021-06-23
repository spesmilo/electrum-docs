How It Works
============

.. raw:: html

  <p>
  <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/D5ty8lIiI6o" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  </p>

Technical Details
-----------------

Below is a technical description of the principles behind Revealer, there are
also :doc:`instructions for encrypting your secrets <how_to_use>`.

The plugin uses the Revealer to encrypt your secret following
`this scheme <http://www.wisdom.weizmann.ac.il/~naor/PAPERS/visual_pap.ps.gz>`_
described by legendary cryptographers Moni Naor and Adi Shamir, published in
1994.

.. image:: /png/revealer/revealer-0_11b.png
  :align: center
  :alt: Cropped sample of a Revealer card with ID 06DAA3EC93CC8579ED054A5946EB2277411B

Each Revealer has a unique code. It consists of a single digit version number, a
32 digit random seed (128 bits of entropy in hex format), and a three digit
checksum (the least important bits of SHA256[version number + seed]). The
version number indicates the dimensions of the Revealer, the random seed is used
to generate the pattern, and the checksum offers some protection against
mistypes.

Step 1) Create a 159 x 97 pixel image made up of 15,423 bits of pseudo-random
noise. The pseudo-random bits are generated with the provably secure HMAC_DRBG
(SHA-512) algorithm, which is seeded by the Revealer random seed.

.. _noise-figure:

.. figure:: /png/revealer/noise.png
  :width: 318px
  :align: center
  :alt: Pseudo randomized black and white pixels

  Pseudo-random noise

Step 2) The secret to be encrypted is an alphanumeric string also encoded as an
image.

.. figure:: /png/revealer/secret.png
  :width: 318px
  :align: center
  :alt: IMPROVE PREVENT INCH DURING CANNON WINE PRAISE MAIL BROCCOLI BLIND WHEEL DEPART

  Sample secret

Step 3) A binary operation (XOR) is executed with the noise image (step 1) and
the unencrypted secret image (step 2) to create the encrypted secret image:

.. _encrypted-secret-figure:

.. figure:: /png/revealer/encrypted_secret.png
  :width: 318px
  :align: center
  :alt: Encrypted secret that looks like randomized black and white pixels

  Encrypted secret

Step 4) In order to perform an XOR operation without a computer, the original
images need to be encoded in the following way: For each black pixel we use the
matrix on the left, and for each white pixel the matrix on the right.

.. image:: /png/revealer/code.png
  :align: center
  :alt: Two squares, each divided in 4 sections. First squares section colors in
    clockwise order: white, black, white, black. Second squares section colors
    in clockwise order: black, white, black, white.

The decryption happens by XORing the encrypted Secret with the original noise.
The Revealer is the encoded :ref:`noise <noise-figure>` and the Secret is the encoded
:ref:`encrypted secret <encrypted-secret-figure>`. When they are overlayed, a visual XOR operation
happens and the secret is revealed.
