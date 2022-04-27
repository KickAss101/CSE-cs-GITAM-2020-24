## Basic Computer Organization and Design
- Instruction codes
- computer registers
- computer instructions
- timing and control
- instruction cycle
- memory-references instructions
- input-output and interrupt
- complete computer description. 
- Design of the basic computer, design of accumulator logic.  

__Micro programmed Control:__ Control memory, address sequencing, micro program example,  
design of control unit.

__Learning Outcomes:__ 
• Learn different types of memory-reference instructions
• Construct the micro programmed control unit

---
### Instruction code
>A group of bits that instruct the computer  to perform specific operation
It is divided into 2 parts: Opcode and Operand/address

__Instruction Format__
4096(address lines) x 16(opcode) -> 2^12 + 2^4 -> 16 bit memory word
0-11 bits -> Operand/address
12-15 -> Opcode

|opcode|operand|
|-|-|
|15-12|11-0|

__Types of instructions__
- Memory reference instruction
- Register reference instruction
- I/O reference instruction

__Types of opcode/address__
- Immediate address (actual operand)
- Direct address (address that points to operand) [15bit -> 0]
- Indirect address (address of memory word which points to operand address) [15bit -> 1]

__Operation Code(opcode)__
- A group of bits that define the operation
	- Ex: add, subtract, multiply, shift, complement
- No. of bits required for opcode depends on total no. of operation available in computer
- The operation code must consists of at least n-bits for a given 2^n or less distinct operations

__Address(Operand)__
- Specifies the location of operands (register/memory words)
- Memory words are specified by their address
- Registers are specified by their k-bit binary code that specify one of 2^k registers

#### Problem
A computer uses a memory unit with 256k words of 32 bit each. A binary instruction code is stored in one word of memory. The instruction has four parts: an indirect bit. an operation code, a register code part to specify one of 64 registers, and an address part.

a. How many bits are there in the operation code, the register code part, and the address part?
b. Draw the instruction word format and indicate the number of bits in each part.
c. How many bits are there in the data and address inputs of the memory?

__Ans__
a. 
256k words = 2^18
64K = 2^6
Address: 18bits
Register code: 6bits
Indirect bit: 1
Opcode: 32 - 25 = 7bits
b.

|1|opcode|Register|Address|
|-|-|-|-|

c.
Data: 32bits
Address: 18bits

---
### Computer registers
__Register:__ Temporary storage device which is present in the processor.

__Execution Flow__
Control Unit or ALU <-> Registers <-> Cache <-> Main Memory <-> Storage or I/O devices

|CPU|
|-|
|Arithmetic Logic Unit|
|Control Unit|
|Registers|

__Types of Registers__

|Register|Acronym, Size|Use|
|-|-|-|
|Program Counter |PC, 12bit|Holds address of the next instruction|
|Address Register|AR, 12bit|Holds address from memory|
|Instruction Register|IR, 16bit|Holds instruction codes|
|Temporary Register|TR, 16bit|Holds temporary data|
|Output Register|OUTR, 8bit|Holds output characters|
|Input Register|INPR, 8bit|Receives input characters|
|Data Register|DR, 16bit|Holds operands/data|
|Accumulator|AC, 16bit|Processor register, holds immediate result|

---
### Computer Instructions
