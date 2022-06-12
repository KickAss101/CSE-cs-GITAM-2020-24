## Introduction and Operating System Structures
__Introduction:__ What Operating Systems Do, Computer System Organization, Computer-System Architecture, Operating System Structure, Operating system operations, Process Management, Memory Management, Storage management, Protection and security, Kernel data structures 

__Operating system Structures:__ operating system services, User and operating system Interface, system calls, Types of System calls, system programs, operating system structure, system boot.  

__Learning Outcomes__
- explain the main responsibilities of an operating system (OS) and the history leading to their current form
- list the most fundamental subsystems and services of OS
- analyse and list out different system calls

---
### Introduction

---
### Types of Operating System
- An operating system is a well-organized collection of programs that manages the computer hardware. It is a type of system software that is responsible for the smooth functioning of the computer system.

__Types of OS__
- Batch OS
- Multiprogramming
- Multiprocessing
- Multitasking
- Network OS
- Distributed OS
- Real-Time OS


##### Batch Operating System
- In the 1970s, Batch processing was very popular. In this technique, _similar types of jobs were batched together and executed in time_. People were used to having a _single computer which was called a mainframe_.
- _Access is given to more than one person_; they submit their respective jobs to the system for the execution.
- The _system put all of the jobs in a queue_ on the basis of first come first serve and then executes the jobs one by one. The _users collect their respective output when all the jobs get executed_.
- The purpose of this was mainly to _transfer control from one job to another_ as soon as the job was completed

![380](Batch-Processing-1.webp)

__Advantages__
- The use of a resident monitor improves computer efficiency as it _eliminates CPU time_ between two jobs.

__Disadvantages__
- _Starvation_ - Batch processing suffers from starvation
- _Not Interactive_ - It is not suitable for jobs that dependent on user's input

##### Multiprogramming
- Multiprogramming is an extension to batch processing where the _CPU is always kept busy_. Each process needs two types of system time: _CPU time and IO time_.
- when a process does its I/O, The CPU can start the _execution of other processes_. Therefore, multiprogramming improves the efficiency of the system.

![380](multi-programming.png)

__Advantages__
-   CPU utilization increased
-   Response time can also be reduced.

__Disadvantages__
-  _No user interaction_ with the computer system

##### Multiprocessing 
- Parallel computing is achieved. _More than one processor present in the system_ can execute more than one process simultaneously, which will _increase the throughput of the system_.

![380](Multiprocessing-System.jpg)

__Advantages__
-   **Increased reliability:** Processing _tasks can be distributed among several processors_. This increases reliability as if _one processor fails, the task can be given to another_ processor for completion.
-   **Increased throughout:** As _several processors increase_, _more work can be done_ in less.

__Disadvantages__
- Is is more _complex and sophisticated_ as it takes care of multiple CPUs simultaneously.
- We can't terminate process in execution to allocate other process which may require less time

##### Multitasking or Time-sharing OS
- It is a _logical extension of a multiprogramming system_ that enables multiple programs simultaneously. It allows a _user to perform more than one task at the same time_.
- Time is distributed among processes.

![380](tutorialwing-os-multitasking.webp)

__Advantages__
- Supports _multiple users simultaneously_.
- Well-defined _memory management_.

__Disadvantages__
- CPU generates more heat since CPU is always busy.

##### Network OS
- An Operating system which includes _software and associated protocols to communicate_ with other computers via a network conveniently and cost-effectively, is called Network Operating System.

![380](Network-OS.jpeg)

__Advantages__
-   _Network traffic reduces due to the division between clients and the server._
-   _Less expensive to set up and maintain._

__Disadvantages__
-   Failure of any node in a system affects the whole system.
-   _Security and performance are important issues_. So _trained network administrators are required_ for network administration.

##### Real Time OS
- _Each job carries a certain deadline_ within which the _job is supposed to be completed_, otherwise, the huge loss will be there, or even if the result is produced, it will be completely useless.
- Real time applications: Hard and Soft real time
- 

![380](real-time-operating-system2.png)

__Advantages__

__Disadvantages__

##### Distributed OS
- The Distributed Operating system is _not installed on a single machine_, it is _divided into parts_, and these _parts are loaded on different machines_.
- A part of the distributed Operating system is installed on each machine to _make their communication possible_. Distributed Operating systems are much _more complex, large, and sophisticated than Network OS_ because they also have to _take care of varying networking protocols_.

__Advantages__
-  Provides _sharing of resources_.
-  _Fault-tolerant._

__Disadvantages__
-   Protocol overhead can dominate computation cost.