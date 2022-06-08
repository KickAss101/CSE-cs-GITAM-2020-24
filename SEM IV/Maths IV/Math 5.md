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
- A hash function H _accepts a variable-length block of data M as input_ and produces a _fixed-size hash value h = H(M)_
- The values returned by the hash function are called _hash values, hash codes, digests, simply hashes_ 

![[hash_functions-1.jpg | 300]]

__Features of Hash Functions__
- Hash function _coverts data of arbitrary length to a fixed length_. This process is often referred to as **hashing the data**.
-  In general, the _hash is much smaller than the input data_, hence hash functions are sometimes called **compression functions**.
-  Since a hash is a _smaller representation of a larger data_, it is also referred to as a **digest**
-  Hash function with n bit output is referred to as an **n-bit hash function**. Popular hash functions generate values between 160 and 512 bits.
- Computationally hash functions are much _faster than a symmetric encryption_.

__Properties of Hash Functions__
- **Pre-Image Resistance**
	- This property means that it should be _computationally hard to reverse a hash function_.
	- In other words, if a hash function h produced a hash value z, then it should be a _difficult process to find any input value X that hashes to z_.
	-   This property _protects against an attacker who only has a hash_ value and is _trying to find the input_. Like password cracking (confidentiality).
- **Second Pre-Image Resistance**
	- This property means _given an input and its hash, it should be hard to find a different input with the same hash_.
	-   In other words, if a hash function h for an input x produces hash value h(x), then it should be _difficult to find any other input value y such that h(y) = h(x)_.
	-   This property of hash function _protects against an attacker who has an input value and its hash, and wants to substitute different value as legitimate value_ in place of original input value (integrity).
- **Collision Resistance**
	- This property means it should be _hard to find two different inputs of any length that result in the same hash_. This property is also referred to as collision free hash function.
	-   In other words, for a hash function h, it is _hard to find any two different inputs x and y such that h(x) = h(y)_.
	-   Since, hash function is _compressing function with fixed hash length, it is impossible for a hash function not to have collisions_. This property of collision free _only confirms that these collisions should be hard to find_.
	-   This property makes it very _difficult for an attacker to find two input values with the same hash_.
	-   Also, if a hash function is collision-resistant _then it is second pre-image resistant_.
---
### Applications of Cryptographic hash Functions

__Message Authentication__
- 

__One way password file__


__Intrusion detection and prevention__
- Hash functions can be used for intrusion detection and intrusion prevention.
- Store H(F) for each file on a system and secure the hash values.  
- One can later _determine if a file has been modified by recomputing H(F)_.  
- An _intruder would need to change F without changing H(F)_ and that is not likely possible.

__Password Storage__
- Hash functions provide protection to password storage.
-  Instead of storing password in clear, mostly passwords are stored in hashes

__Data Integrity Check__
- Data integrity check is a most common application of the hash functions. It is used to generate the checksums on data files.
- This application provides assurance to the user about integrity of the data.

**Game Boards**
- In a game like Tic-Tac-Toe or chess the position of the game may be stored using hash tables

__Digital Signature__
- A signature is usually used to bind signatory to a message. The digital signature is thus a _technique that binds an entity to a hash/digest_.
- This binding ensures that the person sending the data is solely responsible for being for it and this binding can be verified by the receiver and the third party.

---
### Message Authentication Codes
- MAC stands for __Message Authentication Code__, is an _authentication technique which involves the use of a secret key to generate a small fixed-size block of data_ known as cryptographic _checksum or MAC_, that is _appended to the message_.
- It is a _symmetric key cryptographic technique to provide message authentication_. For _establishing MAC process, the sender and receiver share a symmetric key K_.
- Essentially, a _MAC is an encrypted checksum generated on the underlying message_ that is _sent along with a message to ensure message authentication_.
- ![[mac.jpg | 400]]

- __Process of MAC__
	- The sender uses some publicly known MAC algorithm, _inputs the message and the  secret key K and produces a MAC value_.  
	- Similar to hash, MAC function also _compresses an arbitrary long input into a fixed length output_. The major _difference between hash and MAC is that MAC uses secret key during the compression_.
	- The sender _forwards the message along with the MAC_. Here, we assume that the message is sent in the clear, as we are concerned of providing _message origin authentication_, not confidentiality. If confidentiality is required, then the message needs encryption.
	- _On receipt of the message and the MAC_, the _receiver feeds the received message and the shared secret key K into the MAC algorithm and re-computes the MAC value_.
	- The _receiver now checks equality of freshly computed MAC with the MAC received from the sender_. If they _match, then the receiver accepts the message_ and assures himself that the message has been sent by the intended sender.
	- If the computed MAC does _not match_ the MAC sent by the sender, the _receiver cannot determine whether it is the message that has been altered_ or it is the origin that has been falsified. As a bottom-line, a _receiver safely assumes that the message is not the genuine_.

__Limitations of MAC__
There are two major limitations of MAC due to it's symmetric nature of operation
- _Establishment of Shared Secret_
	- It can provide message _authentication among pre-decided users who have shared key_
	- This requires _establishment of shared secret prior to use of MAC_
- _Inability to Provide Non-Repudiation_
	- Non-repudiation is the _assurance that a message originator cannot deny any  previously sent messages_ and commitments or actions.  
	- MAC technique does not provide a non-repudiation service. If the _sender and  receiver get involved in a dispute over message origination_, MACs _cannot provide a proof that a message was indeed sent by the sender and receiver received it_
	- _Though no third party can compute the MAC_, still _sender could deny having sent the message and claim that the receiver forged it_, as it is _impossible to determine which of the two parties computed the MAC_.

#### Difference between digest and MAC
| Digest | MAC|
|-|-|
|A message digest algorithm takes a single input, a message, and produces a "message digest" (aka hash) which allows you to verify the integrity of the message: Any change to the message will (ideally) result in a different hash being generated. An attacker that can replace the message and digest is fully capable of replacing the message and digest with a new valid pair.|A MAC algorithm takes two inputs, a message and a secret key and produces a MAC which allows you to verify the integrity _and_ the authenticity of the message: Any change to the message _or_ the secret key will (ideally) result in a different MAC being generated. Nobody without access to the secret should be able to generate a MAC calculation that verifies; in other words a MAC can be used to check that the MAC was generated by a party that has access to the secret key.

---
### Digital Signatures
- DSA stand for __Digital Signature Algorithm__. It is used for digital signature and its verification. It is based on mathematical concept of modular exponentiation and discrete logarithm. It was developed by National Institute of Standards and Technology (NIST) in1991.
- 
![[dig_sign.jpg | 500]]

__Procedure__
- Firstly, each person adopting this scheme has a public-private key pair in cryptography. 
- The key pairs used for encryption or decryption and signing, or verifying are different for every signature. Here, the private key used for signing is referred to as the signature key and the public key as the verification key in this algorithm.  
- Then, people take the signer feeds data to the hash function and generates a hash of data of that message. 
- Now, the Hash value and signature key are then fed to the signature algorithm which produces the digital signature on a given hash of that message. This signature is appended to the data and then both are sent to the verifier to secure that message.
- Then, the verifier feeds the digital signature and the verification key into the verification algorithm in this DSA. Thus, the verification algorithm gives some value as output as a ciphertext. 
- Thus, the verifier also runs the same hash function on received data to generate hash value in this algorithm.
- Now, for verification, the signature, this hash value, and output of verification algorithm are compared with each variable. Based on the comparison result, the verifier decides whether the digital signature is valid for this or invalid.  
- Therefore, the digital signature is generated by the 'private' key of the signer and no one else can have this key to secure the data, the signer cannot repudiate signing the data in the future to secure that data by the cryptography.

__Importance of DSA__
- 

---

### Introduction to DSA

