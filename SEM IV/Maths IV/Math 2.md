## Classical Encryption Techniques
- Symmetric Cipher Model
- Substitution Techniques
- Transposition Techniques

__Learning Outcomes__   
• discover the concepts of different modes of symmetric ciphers

---
### Symmetric Cipher Model
A symmetric encryption scheme has five ingredients :  
- __Plaintext(P)__: This is the original intelligible message or data that is  
fed into the algorithm as input.  
- __Encryption algorithm (E)__: The encryption algorithm performs  
various substitutions and transformations on the plaintext.  
- __Secret key(K)__ : The secret key is also input to the encryption  
algorithm. The key is a value independent of the plaintext and of the  
algorithm. The algorithm will produce a different output depending on  
the specific key being used at the time. The exact substitutions and  
transformations performed by the algorithm depend on the key.  
- __Ciphertext ( C )__ : This is the scrambled message produced as  
output. It depends on the plaintext and the secret key. For a given  
message, two different keys will produce two different ciphertexts. The  
ciphertext is an apparently random stream of data and, as it stands, is  
unintelligible.  
- __Decryption algorithm (D)__ : This is essentially the encryption  
algorithm run in reverse. It takes the ciphertext and the secret key and  
produces the original plaintext.  
The security of the cryptosystem often depends on keeping the key secret  
to some set of parties.

---

![[Pasted image 20220602190845.png | 500]]

![[Pasted image 20220602192658.png | 500]]

---
### Substitution Techniques

#### Caesar Cipher
- It is a type of substitution cipher in which _each letter in the plaintext  is replaced with the letter standing 3 places further down the alphabets_. 
- The alphabet is wrapped around if it exceeds Z, so that Z follows A

#### Monoalphabetic Cipher
- Monoalphabetic cipher is a substitution cipher in which for a given key, the _cipher alphabet for each plain alphabet is fixed throughout the encryption process_. For example, if ‘A’ is encrypted as ‘D’, for any number of occurrence in that plaintext, ‘A’ will always get encrypted to ‘D’
>__Permutations__
>- A permutation of a finite set of elements 'S' is an ordered sequence of all the elements of 'S', with each element appearing exactly once.
>- Ex: S = {a, b}
>- There are n! permutations possible i.e.,
>	- ab and ba
- The "cipher" line can be any permutation of the 26 alphabetic characters

- _Brute Force attack is hard in this case._
- However, another attack is possible. Human languages are redundant i.e. certain characters are used more frequently than others. This fact can be exploited.  
- In English ‘e’ is the most common letter followed by ‘t’, ‘a’, ’o’,  etc. Letters like ‘q’, ‘x’, ‘j’, 'z' are less frequently used.
- Moreover, _digrams_ like ‘th’ and trigrams like ‘the’ are also more frequent.  
- _Tables of frequency of these letters exist._ These can be used to guess the plaintext if the plaintext is in uncompressed English language.  
- The most common two letter combinations are called as digrams. e.g. th, in, er, re and an.  
- The most common three letter combinations are called as _trigrams_. e.g. the, ing, and, and ion.

#### Playfair Cipher
- In this scheme, _pairs of letters are encrypted_, instead of single letters as in the case of simple substitution cipher.
- In playfair cipher, initially a _key table is created_. The key table is a _5×5 grid of alphabets that acts as the key_ for encrypting the plaintext.
- Each of the _25 alphabets must be unique and i and j are combined in the table_ as we need only 25 alphabets instead of 26. If the plaintext contains i, it can be replaced with j.
- The main drawback of the traditional Playfair cipher is that **the plain text can consist of 25 uppercase letters only**. One letter has to be omitted and cannot be reconstructed after decryption. Also lowercase letters, white space, numbers and other printable characters cannot be handled by the traditional cipher.
![[Pasted image 20220526204801.png | 500]]

#### Hill Cipher
Hill cipher is a polygraphic substitution cipher based on linear algebra. Each letter is represented by a number modulo 26. Often the simple scheme A = 0, B = 1, …, Z = 25 is used, but this is not an essential feature of the cipher. 
- To encrypt a message, each block of n letters (considered as an n-component vector) is multiplied by an invertible n × n matrix, against modulus 26.
- To decrypt the message, each block is multiplied by the inverse of the matrix used for encryption

#### polyalphabetic Cipher
- In a polyalphabetic cipher, _multiple alphabets are used to encipher_.  
- If _two letters are the same in the ciphertext it does not mean they must decipher to the same plaintext letter_.  
- __Polyalphabetic ciphers are__
	- Vigenere Cipher
	- Vernam Cipher

#### Vigenere Cipher
__Encryption__
Ci = (Pi + Ki)  mod 26

__Decryption__
Pi = (Ci - Ki) mod 26

__Key:__ deceptivedecept  
__Plaintext:__ wearediscovered  
__Ciphertext:__ ZICVTWQNGRZGVTW

__Plaintext:__ MICHIGAN TECHNOLOGICAL UNIVERSITY  
__Key:__ HOUGH TONHO UGHTO NHOUG HTONH OUGHT O  
__Ciphertext:__ TWWNP ZOAAS WNUHZ BNWWG SNBVC SLYPM M

#### Vernam Cipher
The Vernam Cipher is an algorithm invented in 1917 to encrypt teletype (TTY) messages by Gilbert Sandford Vernam, it is a symmetric cipher. 
- It is more secure than typical Vigenere cipher.
- Key, we take to encrypt the plain text which _length should be equal to the length of the plain text_.

**Encryption Algorithm:** 
1.  Assign a number to each character of the plain-text and the key according to alphabetical order. 
2.  Add both the number (Corresponding plain-text character number and Key character number). 
3.  Subtract the number from 26 if the added number is greater than 26, if it isn’t then leave it.

__Encryption:__ 𝐶 = 𝑃 + 𝐾  
Where 𝑃 = plaintext, 𝐾 = key, 𝐶 = ciphertext.  
__Decryption:__ 𝑃 = 𝐶 – K

The ciphertext is generated by performing the _bitwise XOR of the plaintext and the key_.  

__Encryption__
𝐶i = 𝑃i ⊕ 𝐾i
Where 𝑃i = ith binary digit of plaintext.  
𝐾i = ith binary digit of key.  
𝐶i = ith binary digit of ciphertext.  
⊕ = exclusive-or (XOR) operation  

__Decryption__
𝑃i = 𝐶i ⊕ 𝐾i

#### One-Time pad Cipher
- In this scheme, a _random key that is as long as the message_ is used.  
- The key is _used to encrypt and decrypt a single message, and then is discarded_.
- Each new message requires a _new key of the same length as the new message_.  
- It produces _random output that bears no statistical relationship to the plaintext_.  
- Because the ciphertext contains no information whatsoever about the plaintext, there is simply no way to break the code.
- For any plaintext of equal length to the ciphertext, there is a key that produces that plaintext. 
- Therefore, if you did an exhaustive search of all possible keys, you would end up with many legible plaintexts, with no way of knowing which the intended plaintext was.  
- Therefore, the code is unbreakable  
- The _security_ of the one-time pad is _entirely due to the randomness of the key_.  
- __Two fundamental difficulties__:  
	- There is the _practical problem of making large quantities of random keys_. Any heavily used system might require millions of random characters on a regular basis. Supplying truly random characters in this volume is a significant task.  
	- Another problem is that of _key distribution and protection_. For every message  to be sent, a key of equal length is needed by both sender and receiver.  
- Because of these difficulties, the one-time pad is _used where very high security is required_.  
---
### Transposition Techniques
#### Rail Fence Cipher
![[Pasted image 20220603104959.png | 500]]

#### Row Column Cipher
![[Pasted image 20220603113406.png | 500]]
