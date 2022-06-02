## Classical Encryption Techniques
- Symmetric Cipher Model
- Substitution Techniques
- Transposition Techniques

__Learning Outcomes__   
• discover the concepts of different modes of symmetric ciphers

---
### Symmetric Cipher Model

---

![[Pasted image 20220602190845.png | 500]]

![[Pasted image 20220602192658.png | 500]]

---
### Substitution Techniques

#### Caesar Cipher

#### Monoalphabetic Cipher
>__Permutations__
>- A permutation of a finite set of elements 'S' is an ordered sequence of all the elements of 'S', with each element appearing exactly once.
>- Ex: S = {a, b}
>- There are n! permutations possible i.e.,
>	- ab and ba
- The "cipher" line can be any permutation of the 26 alphabetic characters

- Brute Force attack is hard in this case.
- However, another attack is possible. Human languages are redundant i.e. certain characters are used more frequently than others. This fact can be exploited.  
- In English ‘e’ is the most common letter followed by ‘t’, ‘a’, ’o’,  etc. Letters like ‘q’, ‘x’, ‘j’, 'z' are less frequently used.
- Moreover, _digrams_ like ‘th’ and trigrams like ‘the’ are also more frequent.  
- Tables of frequency of these letters exist. These can be used to guess the plaintext if the plaintext is in uncompressed English language.  
- The most common two letter combinations are called as digrams. e.g. th, in, er, re and an.  
- The most common three letter combinations are called as _trigrams_. e.g. the, ing, and, and ion.


 

#### Playfair Cipher
![[Pasted image 20220526204801.png]]

#### Hill Cipher

#### polyalphabetic Cipher

#### Vigenere Cipher





---
### Transposition Techniques

