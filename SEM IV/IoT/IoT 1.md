## Introduction to Internet of Things (IoT)
- Introduction and Definition of Internet of Things
- IoT Growth
- Application Areas of IoT
- Characteristics of IoT
- Things in IoT
- IoT Stack
- Enabling Technologies
- IoT Challenges
- IoT Levels
- IoT vs. Cyberphysical Systems
- IoT vs WSN

__Learning Outcomes__
- explain IoT architecture
- interpret the design principles that govern connected devices
- summarize the roles of various organizations for IoT

#### Resources
- [YouTube Channel](https://www.youtube.com/c/ShriramVasudevan)

---
###  Introduction and Definition of Internet of Things
__The Internet of Things__ describes physical objects with sensors, processing ability, software, and other technologies that connect and exchange data with other devices and systems over the Internet or other communications networks
- “IoT refers to the interconnection via the Internet of computing devices embedded in everyday objects, enabling them to send and receive data”
---
### IoT Growth & Application Areas of IoT
#### Growth of IoT
- Overall enterprise Internet of Things (IoT) spending grew 22.4% in 2021 to $158 billion.
- Key macro tailwinds for the IoT market size going forward include maturing technologies such as AI, 5G, and cloud as well as the role that IoT plays in reaching sustainability goals.
- Key macro headwinds include rising input prices, intensified skill/labor shortages, and the ongoing chip shortage

#### Application areas in IoT
- Smart Homes
- Wearable’s
- Smart Cars
- Industries
- Smart Cities
- IoT in Agriculture
- Healthcare
- Power Engagement

---
### Characteristics of IoT
- __Connectivity:__ Things in iot should be connected to the infrastructure and _connectivity is an important character/requirement for an iot infra_. _Anyone, anywhere, anytime_ – _connectivity should be guaranteed in the iot infra_. Without connection, we can't call anything as an IoT.
- __Intelligence and identity:__ The _extraction of knowledge from the generated data_ is very important. _Sensors generate data, the data is to be interpreted properly_.  Each _iot device has an unique identity_ (like an IP address). This _identity is helpful in tracking the equipment_ and at times to _query the status_.
- __Scalability:__ The number of things getting connected to iot infra is getting increased day by day. Hence, _an iot setup shall be capable to handle the massive expansion_. Also, the _data generated shall be massive_ and it _should be handled appropriately_.
- __Dynamic and self adapting (complexity):__ the iot devices should _dynamically adapt itself to the changing contexts_. Assume a camera meant for surveillance. It may have to work in different conditions as different light situations (morning, afternoon, night) 
- __Architecture:__ Architecture _cannot be homogeneous in nature_. It should be _hybrid, supporting different manufacturer's product_ to be in the iot network.
- __SAFETY:__ Having got all the things connected to internet, the _personal data is under threat_. Hence, _securing the data is a major challenge_ . Not only data security, the equipment getting involved in IoT network is huge. Hence, _persona safety is also to be considered_. PRIVACY with PROTECTION should be a goal of an IoT.

---
### Things in IoT
- Things refer to variety of devices. Not really just one device become things.
- At times, you and I are things! (Think, How)
- Anything to qualify as a “THING” require identity.
- The “thing” can monitor/measure etc. means, a temperature sensor could be a thing!
- Things are capable of exchanging data (could be sharing) with other connected devices in the infra.
- The data could be stored in a centralized server (cloud computing), processed there and a control action could be initiated. The devices involved In getting this accomplished are things!!!!
- Some of the famous things which you are aware of:
	- Temperature sensors
	- Pressure sensors
	- Humidity sensors etc.
- The data from above sensors are collected (real time) and sent to the cloud. (sometimes, it could be a local server)
- Based on the data analysis, the control action would be taken.
- Example: switching off the water heater remotely, when the water is heated as per requirement. 
- Not just sensors, the following also can be called as things (see RHS).
- Industrial motors
- Wearables (your watch, band)
- Vehicles
- Shoes
---
### IoT Stack


![[Pasted image 20220607152652.png | 300]]
	__Physical Layer__
- The _physical components are mainly sensors_ such as humidity sensor, temperature sensor, pressure sensor, heartrate sensor, pH sensor, odour sensor etc.
- The _sensors are used for sensing of various parameters as per application of use_. There are plenty of sensors available for same functionality and hence _appropriate selection of sensor is done based on cost and quality_. It is this layer-1 which _provides sensed data to IoT stack for further processing_. Hence _selection of sensor is pivotal_.

__Process and Control Action Layer__
- _Microcontroller/Processor and operating system play vital role at this layer_. 
- Various development kits can be used for this purpose such as _Arduino, NodeMCU (based on ESP32 or ESP8266) , ARM(Advanced Risk machines), PIC(peripheral interface controller)_ etc. 
- Typical _operating systems_ used are Android, Linux, IOS but it can support all major operating systems. The _data collected from the sensors are processed here_ in this layer and _determine if the data is meaningful, microcontroller should be present_.

__Hardware Interface Layer__
- This layer include components or _interfaces used for communication such as RS232, RS485, SPI(serial peripheral interface), I2C(inter integrated circuit), CAN(controller area network), SCI(Serial communication interface)_ etc.
- These interfaces are used for _serial or parallel communication at various baud rates in synchronous/asynchronous modes_. The above-mentioned interface protocols ensure flawless communication.

__RF Layer__
- This radio frequency layer _houses RF technologies based on short range or long range and data rate_ desired by the application of use. 
- The common _indoor RF/wireless technologies include Wi-Fi, Bluetooth, Zigbee, Zwave, NFC(near field communication), RFID_ etc. 
- The common _outdoor RF cellular technologies include GSM (global system for mobiles)/GPRS(general packet radio service), CDMA, LTE-M, NB-IoT, 5G_ etc.
- RF layer does _communication of data using radio frequency-based EM waves_. There is another technology which uses _light waves for data communication_. This light based data communication is referred as _Li-Fi_.

__Session/Message Layer__
- There are protocols which over see _how messages(data) are broadcasted to the cloud_.
- This layer deals with various _messaging protocols such as MQTT, CoAP, HTTP, FTP (or Secured FTP), SSH_ etc. It _defines how messages are broadcasted to the cloud_.

__User Experience Layer__
- This layer deals with _providing best experience to the end users_ of IoT products.
- To fulfill this, this layer takes care of _rich UI designs with lots of features_. Various languages and tools are developed for the design of Graphical User Interface.
- These include _objected oriented and procedure-oriented technologies as well database languages_ (DBMS, SQL) in addition to _analytics tools_.

__Application Layer__
- Application layer talks about the possible applications which can be _built with the support of the rest of the layers_.
- It can range from a _simple automation application to smart city application_.

---
### Enabling Technologies
- Wireless Sensor Network
	- 
- Cloud Computing
- Big Data Analytics
- Communications Protocols
- Embedded System

---
### IoT Challenges
---
### IoT Levels
__Level 1 (Sensor)__
- Less complex, _single sensor_ is involved 
- Data is stored locally
- Data analysis is to be done
- Data is not huge, no big data is involved here.
- Monitoring/Control is done through an application (mobile or desktop or web application)
- This is used for simple applications with limited complexity or no complexity.

![[Pasted image 20220607172400.png | 400]]
__Level 2 (Cloud Storage)__
- Data is spontaneous and voluminous
- Data is _stored on cloud_
- Data _analysis is done locally_
- Monitoring/Control can be done through an application (mobile or desktop or web application)
- Examples: Agriculture applications, room freshening etc

![[iot-level-2.png | 400]]

__Level 3 (Cloud Analysis)__
- This little more complex
- Data is more spontaneous and big data
- Storage is done on cloud
- Data _analysis is also done on the cloud_
- Control and Action happens through the applications

![[Pasted image 20220607174446.png | 400]]

__Level 4 (Cloud Computing)__
- It is more complex level
- Data is a real time big data
- Data is stored and analyzed on the cloud
- _Multiple independent sensors_ are involved

![[Pasted image 20220607181630.png | 400]]

__Level 5 (Coordinator node)__
- Same like level 4 but _Coordinator node is used_
- The _coordinator node takes the data from sensors and microcontrollers and forwards the data to the cloud_
- Data is big data
- Data is stored and analyzed on the cloud
- More complex

![[Pasted image 20220607174846.png | 400]]

---
###  IoT vs. Cyberphysical Systems
- IoT is all about things getting uniquely identified through an address or identifier.
- The thing also can be accessed from anywhere, anytime by an authorised party.
- The information, the sensed data can be as simple as an RFID read.
- Hence, the complexity involved in IoT application is minimal and not complex.
- For complex levels of operation and to address larger network of “things”, a new term is  introduced called Cyber Physical System, or CPS.
- __Cyber-physical systems__(CPS) combine, and build on, elements from different scientific theories and engineering disciplines, including cybernetics, embedded systems, distributed control, sensor networks, control theory and systems engineering
- CPS is not IoT. It has _IoT as one of its components_.
- CPS is _more complex than IoT_ and is _very challenging_ as well.
- It is a _combination of multiple engineering domains coming together, which includes computer science, electronics, electrical and mechanical engineering_.
- It also has IoT as one of the components. Obviously the complexity increases by volumes. An _aeroplane can be seen as a CPS_ which has the influence of _multiple domains of engineering_.
- CPS is expected to be much more brilliant and autonomous, taking appropriate decisions as and when needed.
- It is not merely about identifying, it is more about understanding and taking decisions in a much more dynamic way.
- CPS is mainly _concerned about the collaborative activity of sensors/actuators to achieve a certain goal and to do this CPS uses an IoT system to achieve the collaborative work of the distributed systems_.
---
###  IoT vs WSN
- WSN stands for Wireless Sensor Network.
- The network is _built with multiple autonomous sensors_.
- The sensors could be _pressure, moisture, temperature, humidity, sound_ and so on.
- All the _sensed data are passed to the centrally located server_.
- The _data passing happens in a coordinated pattern_. WSN is basically composed of nodes.
- _Each node has one or more sensors_.
- Simply WSN is all _about coordinated data collection_.
- Whereas _IoT is much more than just data collection and the systems are more intelligent_.
