- Cryptographic Hash Function
- Applications of Cryptographic hash Functions
- Hash Functions
- Message Authentication Codes
- Message Digest
- Digital Signatures
- Introduction to DSA

---
### Cryptographic Hash Function
__Cryptographic Hash Function:__ 
- A hash function is a _mathematical algorithm that maps data of an arbitrary size to a fixed length output_ in a deterministic and random manner and it's one-way function.
- A hash function H _accepts a variable-length block of data M as input_ and produces a fixed-size hash value h = H(M)
- The values returned by the hash function are called _hash values, hash codes, digests, simply hashes_ 

__Features of Hash Functions__
- Hash function coverts data of arbitrary length to a fixed length. This process is often referred to as **hashing the data**.
-  In general, the _hash is much smaller than the input data_, hence hash functions are sometimes called **compression functions**.
-  Since a hash is a _smaller representation of a larger data_, it is also referred to as a **digest**.
-  Hash function with n bit output is referred to as an **n-bit hash function**. Popular hash functions generate values between 160 and 512 bits.

__Properties of Hash Functions__
- **Pre-Image Resistance**
	- This property means that it should be computationally hard to reverse a hash function.
	- In other words, if a hash function h produced a hash value z, then it should be a _difficult process to find any input value X that hashes to z_.
	-   This property protects against an attacker who only has a hash value and is trying to find the input. Like password cracking (confidentiality).
- **Second Pre-Image Resistance**
	- This property means _given an input and its hash, it should be hard to find a different input with the same hash_.
	-   In other words, if a hash function h for an input x produces hash value h(x), then it should be _difficult to find any other input value y such that h(y) = h(x)_.
	-   This property of hash function protects against an attacker who has an input value and its hash, and wants to substitute different value as legitimate value in place of original input value (integrity).
- **Collision Resistance**
	- This property means it should be _hard to find two different inputs of any length that result in the same hash_. This property is also referred to as collision free hash function.
	-   In other words, for a hash function h, it is hard to find any two different inputs x and y such that h(x) = h(y).
	-   Since, hash function is compressing function with fixed hash length, it is impossible for a hash function not to have collisions. This property of collision free only confirms that these collisions should be hard to find.
	-   This property makes it very difficult for an attacker to find two input values with the same hash.
	-   Also, if a hash function is collision-resistant **then it is second pre-image resistant.**
---
### Applications of Cryptographic hash Functions


---
### Hash Functions

---
### Message Authentication Codes

---
### Digital Signatures
---

### Introduction to DSA

