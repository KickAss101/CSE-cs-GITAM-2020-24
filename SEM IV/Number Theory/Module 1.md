## Basic Concepts in Number Theory
- Divisibility
- Greatest Common Divisors/Factors
- Euclidean Algorithm
- Factorization of integers
- Congruence
- Modular arithmetic
- Quadratic residues
- Fermat's theorem
- Cauchy 's theorem
- Chinese Remainder theorem
- Primality testing algorithm
- Euclid's algorithm for integers
- Quadratic residues
- Legendre symbol
- Jacobi symbol  

__Learning Outcomes__ 
• develop the basics of number theory
• perceive the congruence modulo, modular arithmetic and quadratic residues

---

### Divisibility



---
### Greatest Common Divisors/Factors


---
### Euclidean Algorithm

---
### Factorization of integers

---
### Congruence
__Definition:__  Two integers a & b are congruent modulo m if and only if they have same remainder when divided by m.

__Note__ 
- a ≡ b(mod m) means a mod m = b mod m
- a ≡ b(mod m) iff m divided a - b 

__Equivalence Relation__
- Reflexive
- Symmetric
- Transitive

##### Reflexive
Let a ∈ Z then a ≡ a(mod m)
__Proof__
a-a = 0, and m divided 0

##### Symmetric
If a,b ∈ Z such that a ≡ b(mod m) then b ≡ a(mod m)
__Proof__
Assume a ≡ b(mod m) that implies m divides a-b
There is an integer K such that mK = a-b
(-K)m = -(a-b) = b-a 
=> b-a/m => b ≡ a(mod m)

##### Transitive
If a,b,c ∈ Z with a ≡ b(mod m) and b ≡ c(mod m) then a ≡ c(mod m)

__Proof__
Assume a ≡ b(mod m) and b ≡ c(mod m)
This means a-b/m and b-c/m


---
### Quadratic residues

__Definition:__ Let a,z ∈ Z with n>0 and GCD(a,n) = 1. Then a is said to be a quadratic residue modulo n if x^2 = a(mod n) is solvable otherwise it is a non-quadratic residue.