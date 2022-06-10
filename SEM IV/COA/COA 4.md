## Input-Output Organization
- Peripheral devices
- I/O Interface
- Asynchronous Data Transfer
- Modes of Transfer
- Priority Interrupt
- DMA
- I/O Processor
- Serial Communication

__Learning Outcomes__
• Understand the peripheral devices
• Explain the modes of data transfer
• Understand I/O interface

---
### Peripheral Devices
A **peripheral** is a device that is used to put information into or get information out of the computer.

There are three different types of peripherals:
- Input devices
- Output devices
- Input/Output devices

__Input Devices:__ An input device is a term for a physical piece of hardware that connects to a primary device, such as a computer, in order to provide user input.
__Output Devices:__ An output device is any hardware device used to send data from a computer to another device or user.
__Input/Output Devices:__ An input/output device is a hardware device that has the ability to accept inputted, outputted or other processed data. It also can acquire respective media data as input sent to a computer or send computer data to storage media as storage output.

##### Common Peripherals
-   Input
    -   Keyboard
    -   Computer mouse
    -   Graphic tablet
    -   Touchscreen
    -   Barcode reader
    -   Image scanner
    -   Microphone
    -   Webcam
    -   Game controller
    -   Light pen
    -   Scanner
    -   Digital camera
-   Output
    -   Computer display
    -   Printer
    -   Projector
    -   Speaker
-   Storage devices
    -   Floppy disk drive
    -   Flash drive
    -   Disk drive
    -   Smartphone or Tablet computer storage interface
    -   CD/DVD drive
-   Input/Output
    -   Modem
    -   Network interface controller (NIC)

---
### I/O Interface
[Geeksforgeeks - blog](https://www.geeksforgeeks.org/introduction-to-input-output-interface/)

__Input-Output Interface__ is used as an method which helps in _transferring of information between the internal storage devices i.e. memory and the external peripheral device_.

__The need for I/O interface (or) Major differences between CPU and peripherals__
- The nature of peripheral devices is electromagnetic and electro-mechanical. The nature of the CPU is electronic. There is a lot of _difference in the mode of operation of both peripheral devices and CPU_.
- There is also synchronization mechanism because the _data transfer rate of peripheral devices are slow than CPU_.
- Peripheral device's _data code and format is different_  from CPU and memory.
- The _operating mode of each peripheral device can be different from each other_. So as not to disturb the operation of other peripheral devices connected to CPU, we use I/O interface.

##### Functions of Input-Output Interface:
1.  It is used to _synchronize the operating speed_ of CPU with respect to input-output devices.
2.  It selects the input-output device which is appropriate for the interpretation of the input-output device.
3.  It is capable of _providing signals like control and timing signals_.
4.  In this _data buffering?_ can be possible through data bus.
5.  There are various _error detectors_.
6.  It _converts serial data into parallel data and vice-versa_.
7.  It also _convert digital data into analog signal and vice-versa_.

__Block diagram of I/O Interface__
![[interface1.png | 600]]

- __Address__ is used to 
- __Data__
- __Control__

---
### Modes of Transfer
- Transfer of data is required between _CPU and peripherals or memory_ or sometimes between any two devices or units of your computer system.
- All the _internal operations_ in a digital system are _synchronized by means of clock pulses_ supplied by a _common clock pulse Generator_.
- The data transfer can be:
	- __Synchronous__
		- When both the _transmitting and receiving units use same clock pulse_ then such a data transfer is called Synchronous process.
	- __Asynchronous__
		- If there is no concept of clock pulses and the _sender operates at different moment than the receiver_ then such a data transfer is called Asynchronous data transfer.
- Some of the data transfer modes use _CPU as an intermediate path_, others transfer the _data directly to and from the memory unit_
- Three modes of data transfer:
	- Programmed I/O
		- 
	- Interrupt-Initiated I/O
		- 
	- Direct Memory Access (DMA)
		- 

---
### Programmed I/O
![[data-transfer-to-cpu.png]]

- In the programmed I/O method, the _I/O device does not have direct access to memory_.  
- When a byte of data is available, the _device places it in the I/O bus and enables its data valid line_. 
- The _interface accepts the byte into its data register and enables the data accepted line_.  
- The _interface sets a bit in the status register_ that we will refer to as an _F or "flag" bit_.  
- The device can now disable the data valid line, but it will not transfer another byte until the data accepted line is disables by the interface.
- A program is written for the computer to check the flag in the status register to  determine if a byte has been placed in the data register by the I/O device.  
- This is done by reading the status register into a CPU register and checking the value of  the flag bit.  
- Once the flag is cleared, the interface disables the data accepted line and the device can then transfer the next data byte.

#### Problems with programmed I/O
- If I/O device is not ready then CPU has to be ideal, that is inefficient approach. 

---
### Interrupted Initiated I/O
- In programmed initiated, CPU stays in a program loop until the I/O unit indicates that it is ready for data transfer.  
- This is a time consuming process since it keeps the processor busy needlessly.  
- It can be avoided by using an interrupt facility and a special command to inform the  interface to issue an interrupt request signal when data is available from the device.
- In the meantime _CPU can proceed to execute another program_.  
- The _interface meanwhile keeps monitoring the device_.  
- When the _interface determines that the device is ready for data transfer, it generates an interrupt request to the computer_.  
- While the CPU is running a program, it does not check the flag. However, _when the flag is set, the computer is momentarily interrupted_ from proceeding with the current program and is informed of the fact that the flag has been set.
- The CPU deviates from what it is doing to take care of the input or output transfer.  
- After the transfer is completed, the computer returns to the previous program to  continue what it was doing before the interrupt. 
- The _CPU responds to the interrupt signal by storing the return address from the program counter into a memory stack and then control branches to a service routine_ that processes the required I/O transfer.
- Multiple interrupts are generated by multiple devices

__Priority interrupt__
- Software approach (Pooling)
	- It is implemented in software program
	- It pools whether a higher priority device generated a interrupt signal or not and goes to next priority device
- Hardware (Daisy Chaining and parallel priority interrupt)
	- Daisy chaining 
		- devices are connected in serial manner
		- ![[Pasted image 20220609235822.png | 300]]
	- Parallel priority interrupt
		- Interrupt register and Mask register
		-  In interrupt register, disk, printer, reader, keyboard
		- In mask register, depending upon the no. of I/O devices

---
### DMA
- ![[Pasted image 20220610001857.png]]
---
### I/O Processor

---
### Serial Communication
- __Serial communication__ is the process of _sequentially transferring the information/bits on the same channel_. Due to this, the cost of wire will be reduced, but it _slows the transmission speed_.
- Generally, communication can be described as the process of interchanging information between individuals in the form of audio, video, verbal words, and written documents. The serial protocol is run on every device that can be our mobile, personal computers, and many more with the help of following some protocols.

