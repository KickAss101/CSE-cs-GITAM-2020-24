## Memory Organization
- Memory Hierarchy
- Main Memory
- Auxiliary Memory
- Associative Memories
- Cache Memory
- Virtual Memories
- Memory Management Hardware

---
### Memory Hierarchy

---
### Main Memory


---
### Auxiliary Memory

---
### Associative Memories
- An associative memory can be considered as a memory unit whose stored data can be identified for _access by the content of the data itself rather than by an address or memory location_. This type of search _helps in reducing the search time by a large extent_.
- It is also known as _Content Addressable Memory(CAM)_.

__Working of Associative Memory__  
- Data is _stored at the very first empty location_ found in memory.  
- When data is stored at a particular location then _no address is stored_ along with it.  
- When the _stored data need to be searched then only the key (i.e. data or part of data) is provided_.
- A _sequential search is performed in the memory_ using the specified key to find out the matching key from the memory.
- If the _data content is found then it is marked for reading_ by the memory. 
![[coa-associative-memory.png | 400]]
- An associative memory consists of a _memory array and logic for 'm' words with 'n' bits per word_.
- The functional registers like the argument register **A** and key register **K** each have **n** bits, one for each bit of a word. The match register **M** consists of **m** bits, one for each memory word.
- The words which are kept in the memory are _compared in parallel with the content of the argument register_.

__Associative memory organization__
- memory array
- logic for m words with n bits per word
- Several registers like input register, mask register, select register and output register.

__Argument Register (A):__ It contains the word to be searched

__Key Register (K):__ It specifies which part of the argument needs to be compared with words in the memory.
- If all bits are set '1' then entire word needs to compared else only the bits having '1' will be compared.

__Associative Memory Array:__ It contains the words which are to be compared with the argument word. 

__Match Register (M):__ After matching process, the bits corresponding to matching words are set '1' in match register.

__Input Register:__ It holds data that is to be written into associative memory.

__Output Register (Y):__ It contains the matched data word that is retrieved from associative memory

![[coa-associative-memory2.png | 400]]

__Advantages__
- Associative memory searching process is fast.  
- Associative memory is suitable for parallel searches.

__Disadvantages__
- Associative memory is expensive than RAM

---
### Cache Memory
- The _data or contents of the main memory that are used frequently by CPU are stored in the cache memory_ so that the processor can easily access that data in a shorter time.
- Whenever the CPU needs to access memory, it first checks the cache memory. If the data is not found in cache memory, then the CPU moves into the main memory.

![[coa-cache-memory.png | 500]]

__The basic operation of a cache memory__
-   When the CPU needs to access memory, the cache is examined. If the word is found in the cache, it is read from the fast memory.
-   If the word addressed by the CPU is _not found in the cache_, the _main memory is accessed_ to read the word.
-   The performance of the cache memory is frequently measured in terms of a quantity called **hit ratio**.
-   When the _CPU refers to memory and finds the word in cache_, it is said to produce a **hit**.
-   If the _word is not found in the cache_, it is in main memory and it counts as a **miss**.
-   The _ratio of the number of hits divided by the total CPU references to memory_ (hits plus misses) is the __hit ratio__.

#### Cache Mapping
- Cache mapping is a _technique that defines how contents of main memory are brought into cache_.

>32k \* 12  (each word is 12 bits)
>32K = 2^5\*2^10 = 2^15 | so 15 bits are for CPU address bits.

![[Cache-Mapping-Diagram-2.png | 500]]

**Fully Associative Mapping**
- A block of main memory can map to any line of the cache that is freely available at that moment. 
- This makes associative mapping more flexible than direct mapping.
- The associative memory _stores both the address and content (data) of the memory word_.
- The address value of 15 bits is shown as a five-digit octal number and its  corresponding 12-bit word is shown as a four-digit octal number.
- A _CPU address of 15 bits is placed in the argument register_ and the associative memory is searched for a matching address.
- If the address is found, the _corresponding 12-bit data is read and sent to the CPU_. If no match occurs, the main memory is accessed for the word. The address data pair is then transferred to the _associative cache memory_.
![[associative-mapping-cache.png | 350]]
**Direct Mapping**
- The CPU address of _15 bits is divided into two fields_. The _nine least significant bits constitute the index field_ and the remaining _six bits form the tag field_.
- In the general case, there are _2^k words in cache memory_ and _2^n words in main memory_. (512 words - 2^9, k=9(index) | 32k - 2^15 | n=15(tag))
- The n-bit memory address is divided into two fields: _k bits for the index field_ and _n-k bits for the tag field_.
- _n-bit address is used to access the main memory_ and the _k-bit index to access the cache_.
- When the CPU generates a memory request, the _index field is used for the address to access the cache_. The _tag field of the CPU address is compared with the tag in the word_ read from the cache.
- If the two tags match, there is a hit and the desired data word is in cache.
- If there is no match, there is a miss and the required word is read from main memory. It is then stored in the cache together with the new tag, replacing the previous value.
- The word at address zero is presently stored in the cache (index = 000, tag = 00, data = 1220). Suppose that the CPU now wants to access the word at address 02000. The index address is 000, so it is used to access the cache. The two tags are then compared. The cache tag is 00 but the address tag is 02, which does not produce a match. Therefore, the main memory is accessed and the data word 5670 is transferred to the CPU. The cache word at index address 000 is then replaced with a tag of 02 and data of 5670.
![[Pasted image 20220604212522.png | 300]]
**Set-associative Mapping**
- 
![[Pasted image 20220605103046.png | 350]]
---
###    Virtual Memories

![[virtual-memory1.png | 400]]
![[Pasted image 20220605104428.png | 400]]

---
### Memory Management Hardware
[[OS 4#Memory Management]]
- A memory management system is a _collection of hardware and software procedures for managing the various programs residing in memory_.
- The memory management software is _part of an operating system_ available in many computers. Here we are concerned with the hardware unit associated with the memory management system

__Basic Components of Memory Management Unit__
- __Dynamic address relocation:__ Facility for dynamic storage relocation that map logical memory to physical memory addresses
- __Sharing Common Programs:__ Provision for sharing common programs stored in memory by different users
- __Protection:__ Protection of information against unauthorized access and preventing users from changing OS functions.

#### Dynamic Address Relocation
- The dynamic storage relocation hardware is a _mapping process_ similar to the paging system.
- The fixed page size used in the virtual memory system causes certain difficulties with respect to _program size and the logical structure of programs_.
- It is more convenient to divide programs and data into logical parts called segments.
- A __segment__ is a _set of logically related instructions or data elements associated with a given name_. Segments may be _generated by the programmer or by the operating system_.
- Examples of segments are a subroutine, an array of data, a table of symbols, or a user's program.

![[F1_S.B_Madhu_19.05.20_D4.png]]
![[F1_S.B_Madhu_19.05.20_D5.png]]
#### Sharing of Common Programs
- It is an integral part of _multiprogramming_.
- Other system programs residing in memory are also shared by all users in a multiprogramming system _without having to produce multiple copies_.
- The other issue in multiprogramming is _protecting one program from unwanted interaction with another_. An example of unwanted interaction is one user's unauthorized copying of another user's program.
- Another aspect of protection is concerned with _preventing the occasional user from performing operating system functions_ and thereby interrupting the orderly sequence of operations in a computer installation.

#### Memory Protection
- Memory protection can be assigned to the physical address or the logical address.
- The protection of memory through the physical address can be done by _assigning a number of protection bits for each block in memory_ that indicate the _type of access allowed to its corresponding block_.
- 