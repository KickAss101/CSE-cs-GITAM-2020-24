## Register Transfer and Micro operations
- Register transfer language
- register transfer
- bus and memory transfers
- arithmetic micro operations
- logic micro operations
- shift micro operations
- arithmetic logic shift unit

__Learning Outcomes__
- Demonstrate the register transfer language
- Learn different types of micro operations

---
### Register Transfer language
- The symbolic notation used to describe the microoperation transfers among registers is called a register transfer language. 
- The term "register transfer" implies the availability of hardware logic circuits that can perform a stated microoperation and transfer the result of the operation to the same or another register.  
- The word "language" is borrowed from programmers, who apply this term to programming languages.  
- A register transfer language is a system for expressing in symbolic form the  microoperation sequences among the registers of a digital module.  
- It is a convenient tool for describing the internal organization of digital computers in  concise and precise manner.  
- It can also be used to facilitate the design process of digital systems.  
- Information transfer from one register to another is designated in symbolic form by  means of a replacement operator.  
- The statement below denotes a transfer of the content of register R1 into register R2.  R2 ← R1  
- A statement that specifies a register transfer implies that circuits are available from the outputs of the destination register has a parallel load capability.  
- Every statement written in a register transfer notation implies a hardware construction for implementing the transfer.

---
### Microoperations
- The operations implemented on data stored in registers are known as micro-operations.
- A micro-operation is a _basic operation implemented on the data saved in one or more registers_.
- There are four categories of the most common microoperations
	- __Register Transfer__
		- Transfer binary information from one register to another
	- __Arithmetic__
		- Perform arithmetic operations on numeric data stored in registers
	- __Logic__
		- Perform bit manipulation operations on non-numeric data stored in registers
	- __Shift__
		- Perform shift operations on data stored in registers.
---
### Arithmetic micro operations
- Arithmetic microoperations _perform arithmetic operations on numeric data stored in registers_.
- The basic arithmetic microoperations are _addition, subtraction, increment, decrement, and shift_.
- Multiply and divide are not included as microoperations

![[Pasted image 20220609181416.png | 600]]

__4 bit Arithmetic Microoperations__

![[arithmetic-microoperations.png | 400]]

