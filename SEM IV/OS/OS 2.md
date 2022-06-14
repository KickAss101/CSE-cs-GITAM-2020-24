## Process Management and CPU Scheduling
__Process Management__ 
- Process concepts
- process scheduling
- Operations on processes
- inter-process communication  

__CPU Scheduling__
- Scheduling-criteria
- scheduling algorithms
- Thread scheduling
- Multiple processor scheduling
- algorithm evaluation
- Multithreaded programming
- Multi-core Programming
- Multi-threading Models
- Thread Libraries

__Learning Outcomes__
• demonstrate the concepts of Process, thread and CPU scheduling
• list out different scheduling algorithms
• analyse scheduling algorithms with different examples

---
### Process Management
[Process Management | neso academy](https://www.youtube.com/watch?v=OrM7nZcxXZU&ab_channel=NesoAcademy)

>__Process:__ A program in execution
__Thread:__ A thread is the unit of execution within a process. 
### Process concepts
#### Process State
[Process State | neso academy](https://www.youtube.com/watch?v=jZ_6PXoaoxo&ab_channel=NesoAcademy)
>- As a process executes, it changes state
>- The state of a process is defined in part by the current activity of that process

![380](process_state.webp)
- __New:__ The process  is being created
- __Ready:__ The process is waiting to be assigned to a processor
- __Running:__ Instructions are being executed
- __Waiting:__ The process is waiting for some event to occur such as I/O completion or reception of a signal
- __Terminated:__ The process has finished execution

 #### Process Control Block (PCB)
 [PCB | neso academy](https://www.youtube.com/watch?v=4s2MKuVYKV8&list=PLBlnK6fEyqRiVhbXDGLXDk_OQAeuVcp2O&index=18&ab_channel=NesoAcademy)
 > Each process is represented in the operating system by a Process Control Block(PCB) or Task Control Block
- Process State
- Process Number
- Program Counter [[COA 2#Computer registers]]
- Registers
- CPU Scheduling information
- Memory Management Information
- Accounting Information
- I/O status information
- List of open files

### Process Scheduling
[Process Scheduling | neso academy](https://www.youtube.com/watch?v=2h3eWaPx8SA&list=PLBlnK6fEyqRiVhbXDGLXDk_OQAeuVcp2O&index=19&ab_channel=NesoAcademy)
>- The objective of _multiprogramming_ is to have some process running at all times, to maximize CPU utilization
>- The objective of _time sharing_ is to switch the CPU among processes so frequently that users can interact with each program while it is running



#### Operations on processes

#### inter-process communication

---

### CPU Scheduling
