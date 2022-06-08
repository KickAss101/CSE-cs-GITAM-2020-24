## Public Key Cryptography
- Principles of Public-Key Cryptosystems
- The RSA Algorithm
- Diffie-Hellman Key Exchange Algorithm
- Elliptic Curve Cryptosystem
- Probabilistic encryption

__Learning Outcomes__
• estimate the importance of Public Key Cryptography
• apply RSA algorithm and Elliptic Curve Cryptograph

---
### Principles of Public-Key Cryptosystems

---
### The RSA Algorithm

---
### Diffie-Hellman Key Exchange Algorithm
- Not an encryption algorithm
- Exchange secret/_symmetric key_
- Asymmetric encryption: public & private keys are used

__Algorithm__
- Assume prime number __q__
- Select **α** such that α is _primitive root of q and α < q_
- Assume X(a) (Private Key), X(a) < q
- Calculate Y(a) (Public Key), Y(a) = α ^(X(a)) mod q
- Calculate Y(b)

__Key Generation__

![[Pasted image 20220601211718.png | 700]]


---
### Elliptic Curve Cryptosystem
__Elliptic curves__ can _intersect almost 3 points when a straight line is drawn intersecting the curve_. Elliptic curve is _symmetric about the x-axis_. This property plays a key role in the algorithm.
- 

__Curve formula__ => y^2 = x^3 +ax + b

__Trapdoor Function__
- It is a _one-way function_ that is easy to compute in one direction, yet difficult to computer in the opposite direction (finding it's inverse) without special information called trapdoor.

__Popular Elliptic Curves in Cryptography__
- NIST P-256 (Prime-256v1)
- X25519
- P-521
- P-384


---
### Probabilistic encryption
Probabilistic encryption is the _use of randomness in an encryption algorithm_, so that when encrypting the same message several times it will, in general, yield different ciphertexts. The term ‘probabilistic encryption’ is typically _used in reference to public key encryption algorithms_.

---