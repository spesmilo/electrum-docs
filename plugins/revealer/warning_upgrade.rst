:orphan:

Warning and Upgrade
===================

On August 18th, 2018, Alan Evans published
`Revealer.cc — Deepdive and warning`_, which raised questions about the security
of the Pseudo Random Number Generator and warned against Revealer re-use.

Our Response
------------

Revealer is based on a One Time Pad and should be used to encrypt one single
secret. It is not secure to use the same Revealer multiple times. We understand
that the warning against re-use on our FAQ was not loud enough and have added an
extra warning directly on the software encryption dialog.

To eliminate any further concerns about security of the PRNG Revealer will
upgrade to the provable secure HMAC_DRBG (SHA-512). The code is already patched
in the Electrum master repository and will be available from the next release.
An attack in the current implementation has not been demonstrated.


What's the problem with the Pseudo Random Number Generator?
-----------------------------------------------------------

Observing a sufficient number of outputs from a Mersenne Twister (MT) allows a
attacker to reconstruct the internal state and predict all future outputs. A
secret encrypted with Revealer does not leak enough information to be able to
recover the internal state of MT. A few leaked single bit states won’t help much
in well known attack vectors. We are not aware of any possible attack in the
current implementation. Nevertheless, MT is not recommended for cryptographic
use, and it could become a problem for larger or different versions. From the
next release, the noise will be generated using the Deterministic Random Bit
Generator HMAC_DRBG (SHA-512). It will continue to be seeded with 128bit entropy
from cryptographic secure /dev/urandom.


What’s the problem with using a Revealer to encrypt multiple secrets?
---------------------------------------------------------------------

Revealer is based on a One Time Pad and should be used to encrypt one single
secret. In possession of multiple secrets encrypted for the same Revealer it can
be attacked. We have included a explicit warning in the software to avoid user
mistake. Encrypting more than one secret is still possible, and might be
desirable for some threat models. See more information on our :doc:`faq`.


What should users do?
---------------------

It is recommended to upgrade your backups. The patched version of the software
is merged into Electrum master repository and will be available in the next
release. Only encrypt multiple secrets for the same Revealer if you know what
you are doing and understand the risks involved.

Published: 28.08.2018

.. _Revealer.cc — Deepdive and warning: https://medium.com/@_west_on/revealer-cc-deepdive-and-warning-77892b3a24a1
