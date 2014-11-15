Python Cryptography
===================

Cryptography is the study and practice of secure communication typically
involving an insecure channel (such as the internet).

Secure communication (in theory) has some or all of the following attributes:

* confidentiality - only intended recipients see communication
* authentication - the message comes from the correct sender
* integrity - the data has not been tampered with en route


Python cryptography
-------------------

The Python cryptography library has a couple aims:

* secure by default
* high level (simple) API for common use cases
* flexible C/C++ backend (OpenSSL, CommonCrypto)
* Python3 support, PyPy support, testability


High level API
--------------

* There are a million ways to do cryptography and almost a million of those
  ways are wrong.
* Fernet is the symmetric key encryption high level API. Symmetric encryption
  uses the same key for encryption and decryption.
* All the outputs such as the token and key are urlsafe_base64
* The token being valid implies that it was encrypted by the key and has not
  been changed before being decrypted.
* Notice that you did not choose an encryption key. If the key is generated
  randomly, it is tough to use a weak one.
* You did not even pick how to encrypt it. Fernet uses AES128-GCM


Fernet format
_____________

* Encryption datetime is public information in this cryptosystem
* Should be impossible for somebody to guess a message that will decrypt
* HMAC is computed from all the rest of the message and uses the secret key
  so it is (in theory) impossible to fake. Provides integrity.


Hazmat
------

These are largely cryptographic primitives -- pieces that could be used
to build a cryptosystem. However, there is great potental for misuse here.


Public key cryptography
_______________________

* There are other supported algorithms like DSA
* Typically slower than symmetric encryption - sometimes paired
* Public key can be given out to anybody - anybody can verify signatures
  and anybody can encrypt (although not decrypt)
* Similar to a system like PGP/GPG


Two-factor auth
_______________

rfc6238


PBKDF2
______

There is an implementation of this in Django, but it is useful for password
storage.


Constant time
_____________

Tell story about Django timing attack
