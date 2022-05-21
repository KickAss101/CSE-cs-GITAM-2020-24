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

__Input-Output Interface__ is used as an method which helps in transferring of information between the internal storage devices i.e. memory and the external peripheral device .

__The need for I/O interface (or) Major differences between CPU and peripherals__
- The nature of peripheral devices is electromagnetic and electro-mechanical. The nature of the CPU is electronic. There is a lot of _difference in the mode of operation of both peripheral devices and CPU_.
- There is also synchronization mechanism because the _data transfer rate of peripheral devices are slow than CPU_.
- There is a _difference in the data code and formats_ are between CPU and memory.
- The _operating mode of each peripheral device can be different from each other_. So as not to disturb the operation of other peripheral devices connected to CPU, we use I/O interface.

##### Functions of Input-Output Interface:
1.  It is used to synchronize the operating speed of CPU with respect to input-output devices.
2.  It selects the input-output device which is appropriate for the interpretation of the input-output device.
3.  It is capable of providing signals like control and timing signals.
4.  In this data buffering can be possible through data bus.
5.  There are various error detectors.
6.  It converts serial data into parallel data and vice-versa.
7.  It also convert digital data into analog signal and vice-versa.

__Block diagram of I/O Interface__
![[interface1.png | 600]]

- __Address__ is used to 