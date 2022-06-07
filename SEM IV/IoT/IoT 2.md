## Introduction to Sensors
- Introduction to Sensor Interfacing
- Types of Sensors
- Controlling Sensors through Webpages
- Microcontrollers

---
### Sensor Interface
- __Sensor__ is a device which measures a physical quantity and converts it into an observer or by an instructor.
- __Sensor__ is an input device which provides an output (signal) with respect to a specific physical quantity(input).
- It is a device that converts signals from one energy domain to electrical domain.


---
### Types of sensors
#### Classifications of the sensors
- They can be classified as _Active and Passive_
- __Active sensors__ are those which require an external excitation signal or a power signal.
- __Passive sensors__ on the other hand do not require any external power signal and directly generates output response.

- They can also be classified as  _Analog and Digital Sensors_
- __Analog sensors__ produce an analog output i.e., a continuous output signal with respect to the quantity being measured.
- __Digital Sensors__ in contrast to Analog sensors work wit discrete or digital data. The data in digital sensors which is used for conversion and transmission is digital in nature.

#### Types of sensors
- __Gas Sensor (MQ2/MQ05)__
	- This sensor is capable of _detecting H2, LPG, CH4, Alcohol and smoke_.
	- Due to its high sensitivity and fast response time, _measurements can be taken as quick as desired_.
	- When any  flammable gas flows through this sensor the _coil inside this sensor burns and so, the resistance of the coil decreases_. Hence, the output voltage starts increasing, which can be detected using a micro controller.
	- If the _smoke presence is lesser then the output voltage is less_ and if _smoke presence is intense then the output voltage is higher_.
	- _MQ-05 is not sensitive to smoke_. Hence, MQ-02 is preferred for smoke detection applications.
	- _MQ-02 is not very good for detecting the low level LPG presence_ where MQ-05 is preferred.
	- ![[Pasted image 20220607185859.png | 350]]
- __LDR Sensor__
	- 
- __Obstacle  sensor__
	- In real time Applications _IR sensors are used for detecting obstacles_.
	- The Sensor gives an _Output Voltage when it detects an obstacle_ in front of it.
	- This generated voltage is digital (_1 or 0_) which will let the robot to know whether an obstacle is present or not.
	- For example, a Robot is deployed to detect the obstacles in the path.
	- The Robot has to detect  and _alert the presence of an obstacle_. So, IR sensors are used which give either _Zero or one as its digital output based on the presence of the obstacle_.
	- ![[Pasted image 20220607190250.png | 400]]
- __Heartbeat Sensor__
	- There are many Applications that use Heartbeat sensor such as _wearable applications that monitor a person's heartbeat accurately_.
	- The _applications are mostly  in health care domain_ and the sensor is _inexpensive_.
	- This sensor is interfaced with Arduino uno board/NodeMCU and the data is loaded onto the Cloud.
	- ![[Pasted image 20220607191034.png | 400]]
- __Ultrasonic Sound Sensor__
	- 
- __Gyro Sensor__
- __GPS Sensor__
- __Colour Sensor__
- __pH Sensor__


---
### Controlling Sensors thorough Webpages

---
### Microcontrollers
#### 8051 Components
- __Bus Control__
	- Two types of buses: Data bus and Address bus
	- Data bus is used to transfer _8-bit data_ - acts as an electronic channel 
	- Address bus is used transfer _16-bit_ information but not data
- __Four General Purpose parallel I/O ports__
	- Port0, Port1, Port2, Port3
	- Each port is of 8-bit
	- Port 0
		- No external memory support
		- Acts as I/O port
	- Port 1
		- 
- __Timers and Counters__
	- Internal operation can be synchronized using clock circuit
	- XTAL1 and XTAL2 acts as oscillator circuit
	- Four additional pins:
		- EA
		- PSEN
		- ALE -
		- RST -  Reset
- __Internal RAM and ROM__
	- _ROM_ is non-volatile and it is of 4KB
	- It can address program memory as well as 64KB of data memory
	- _RAM_ is a volatile memory
	- It is 128bytes of internal RAM
	- It is divided into 32 working registers
	- 32 working registers are constituted as 4 register banks
	-  Bank 0, Bank 1, Bank 2, Bank 3
	- Each bank hold 8 registers
- __Serial port__
	- SBUF - Serial Port Data buffer hold the data
	- SCON - Serial Control, manager data communication
	- PCON - Power Control, manages data transfer rate
	- Pins: RXD & TXD
- __Interrupt Control Logic__
	- It suspends the microcontroller when an interrupt occurs
	- Two ways of giving interrupt to micorcontrollers
		- By sending Software signal
		- By send Hardware signal
		- Five sources of interrupt
			- 2 external interrupts service
			- 3 external interrupts services
-  __CPU__
	- 

![[8051_architecture.png | 400]]