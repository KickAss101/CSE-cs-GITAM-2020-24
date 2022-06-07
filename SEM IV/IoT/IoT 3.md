## Protocols for IoT
- __Messaging and Transport Protocols__
	- Messaging Protocols
		- Message Queuing Telemetry Transport (MQTT)
		- Constrained Application Protocol (CoAP)
	- Transport Protocols (Li-Fi,BLE)
		- Bluetooth Low Energy (BLE)
		- Light Fidelity (LiFi)
- __Addressing and Identification__
	- Internet Protocol Version 4 (IPv4)
	- Internet Protocol Version 6 (IPv6)
	- Uniform Resource Identifier (URI)

---
### Messaging Protocols

#### Message Queuing Telemetry Transport (MQTT)
- MQTT stands for **Message Queuing Telemetry Transport**.
- MQTT is a _machine to machine internet of things connectivity protocol_.
- It is an _extremely lightweight and publish-subscribe messaging application layer protocol_.
- This protocol is useful for the connection with the _remote location_ where the bandwidth is a premium. These characteristics make it useful in various situations, including constant environment such as for communication machine to machine and internet of things contexts.
- It is a _publish and subscribe system_ where we can publish and receive the messages as a client. It makes it _easy for communication between multiple devices_.
- It is a simple messaging protocol _designed for the constrained devices_ and with _low bandwidth_, so it's a perfect solution for the internet of things applications.

__Characteristics of MQTT__
- It is a _machine to machine protocol_, i.e., it provides communication between the devices.
- It is designed as a _simple and lightweight messaging protocol that uses a publish/subscribe system_ to exchange the information between the client and the server.
- It provides _faster data transmission_. It's a _real-time messaging protocol_.
- It _allows the clients to subscribe to the narrow selection of topics_ so that they can receive the information they are looking for.

__Architecture of MQTT__
Components of the MQTT
-   **Message**
-   **Client**
-   **Server or Broker**
-   **TOPIC**

__Message__
- The message is the _data that is carried out by the protocol across the network_ for the application. When the message is transmitted over the network, then the message contains the following parameters:
1.  Payload data
2.  Quality of Service (QoS)
3.  Collection of Properties
4.  Topic Name

**Client**
- In MQTT, the _subscriber and publisher are the two roles of a client_.
- The clients subscribe to the topics to publish and receive messages.
- In simple words, we can say that if _any device uses an MQTT library and connects to MQTT broker, then that device is referred to as a MQTT client_. A device is a client if it opens the network connection to the server, publishes messages that other clients want to see, subscribes to the messages that it is interested in receiving, unsubscribes to the messages that it is not interested in receiving, and closes the network connection to the server.
- Client collects information from sensors
- Connects itself to the MQTT server
- Subscribes to topic to publish and receive messages   
- In MQTT, the _client performs two operations_:
	- **Publish:** When the _client sends the data to the server_, then we call this operation as a publish.
	- **Subscribe:** When the _client receives the data from the server_, then we call this operation a subscription.
	
__Server or Broker__
- The _device or a program that allows the client to publish the messages and subscribe to the messages_.
- A server accepts the network connection and messages from the client, _processes the subscribe and unsubscribe requests_, forwards the application messages to the client, and closes the network connection from the client.
- Another _responsibility of the broker is the authentication, authorization_ of clients.
- MQTT also supports QoS levels
	-  0 - At most once (Best effort, no ACK)
	- 1 - At least once (Acked, retransmitted if ack not received)
	- 2 - Exactly once (Request to publish, clear to send)
	
**TOPIC**
- The label provided to the _message is checked against the subscription known by the server_ is known as TOPIC.

![[mqtt-protocol2.jpg | 350]]


![[mqtt-protocol3.jpg| 400]]

- Suppose a device has a temperature sensor and wants to send the rating to the server or the broker. If the phone or desktop application wishes to receive this temperature value on the other side, then there will be two things that happened. 
- The _publisher first defines the topic_; for example, the temperature then publishes the message, i.e., the temperature's value. 
- _After publishing the message_, the phone or the desktop application on the other side will subscribe to the topic, i.e., temperature and then receive the published message, i.e., the value of the temperature. 
- The server or the _broker's role is to deliver the published message_ to the phone or the desktop application

__MQTT Message Format__

![[mqtt-protocol4.jpg | 400]]

#### Constrained Application Protocol (CoAP)
- CoAP stands for Constrained Application Protocol, is a specialized _web transfer protocol (HTTP) for use with constrained nodes and constrained networks_ in the Internet of Things.
- It uses RESTful (Representational State Transfer) API concept that has following methods:
	- GET : Read information
	- PUT: Update information
	- POST: Create new information
	- DELETE: Delete information
- CoAP can transport RESTful call over _thin networks_
- __Features__
	- Web protocol used with _machine-to-machine_ (M2M) with constrained requirements
	- Uses _UDP_ as it's transport layer protocol
	- _Asynchronous_ message exchange
	- _Low overhead_ and very simple to parse
	- _URI and content-type_ support
	- _Proxy and caching_ capabilities
	- Security with _DTLS_ (Datagram Transport Layer Security)

__CoAP layers__
- __Request/Response__
	- The Request/Response layer _manages request/response interaction based on request/response messages_.
- __Messages__
	- The Messages layer deals with _UDP and with asynchronous messages_.
- __CoAP supports 4 different message types__
	- Confirmable (CON) (Reliable)
	- Non-Confirmable (NON) (Non-reliable)
	- Acknowledgment (ACK)
	- Rest (RST)

![[coap-messages-ack.webp | 300]]
![[coap-stack-1.webp | 300]]

---
### Transport Protocols
#### Bluetooth Low Energy (BLE)
- BLE stands for Bluetooth Low Energy, is an open source application layer protocol and a _wireless personal area network_ technology designed and marketed by the Bluetooth SIG (Special Interest Group). Also known as Bluetooth smart.
- BLE has all the features that classic Bluetooth provides with enhancements and with reduced power consumption
- Though BLE improved many features but retained same range
- It is supported by many devices and their Operating Systems
- A BLE device shall be able to _communicate to outside world by two means_:
	- Broadcasting
		- _Sending out message to more than one recipient_. 
		- Data is sent out _one-way_
		- Whichever device is capable of picking the data (receiving), it will. (Radio Broadcast)
	- Connections
		- Connection is permanent.
		- It enables _periodical data transfer between the devices_ (Two devices)
		- The term _Master Slave Configuration_ will come into picture.

__Features of BLE__
- License free
- Support to Multi brand mobile / GPOS
- Low cost - Very much affordable.
- Low power consumption - Very much needed in IoT infra.
- Not huge
- Good range coverage
-  Extreme heterogeneity support

__Components of BLE__
- __Application:__ User application resides here and interacts with the Bluetooth stack
- __Controller:__ The lower layers the Bluetooth stack 
	- It has link layer and Physical layer
	- The link layer _defines packet structure and control_
	- The physical layer takes care of _transmission and reception_
	- Physical layer also takes care of _modulation and de-modulation_, converts analog to digital and vice-versa.
- __Host:__ The upper layers of the Bluetooth stack
	- Generic Access Profile
	- Generic Attribute Profile
	- Attribute Protocol
	- L2CAP
	- Security Manager
- __HCI:__ It provides a interface between Host and Controller

![[Pasted image 20220606133646.png | 300]]


__Applications of BLE__
- Fitness technology like fitness bands/watches
- Sharing of data from nearby devices
- To lock/unlock vehicles
- Tracking devices
![[Pasted image 20220606141541.png | 400]]
#### Light Fidelity (LiFi)
- LiFi stands for Light Fidelity
- Now a days, too many devices are connected to internet.
- Everything and anything, _from watch to water heater_ is connected to internet and _internet is used like oxygen_.
- Li-Fi is a _wireless communication technology_ which utilizes light to transmit data and position between devices. Speed upto stunning: _224Gbps_
- In technical terms, Li-Fi is a _light communication system that is capable of transmitting data at high speeds over the visible light, ultraviolet, and infrared spectrums_. 
- In its present state, only _LED lamps can be used for the transmission of data in visible light_.
- In terms of its end use, the technology is similar to Wi-Fi — the key technical difference is that _Wi-Fi uses radio frequency to induce a voltage in an antenna_ to transmit data, whereas _Li-Fi uses the modulation of light intensity_ to transmit data.
- Li-Fi's ability to _safely function in areas otherwise susceptible to electromagnetic interference_ (e.g. aircraft cabins, hospitals, military) is an advantage.
- About _100 times faster than speeds achievable by WiFi_.

__Advantages__
- Secured
- Efficient
- Fast
- Is an effective alternate to Radio Frequency

__Disadvantages__
- Since, walls are there, it could be short range.
- Infra set up could take a bit more time to make it practically viable.
- Still, A major challenge for us to face : how the receiving device will transmit back to transmitter.

---
### Addressing and Identification
#### Internet Protocol Version 4
- In Internet Protocol version 4 (IPv4), almost 4.3 billion IP addresses are possible (2^32).
- An IPv4 address is a 32-bit address that is represented in dotted decimal notation, with a decimal value representing each of the four octets that make up the address (from 0.0.0.0 to 255.255.255.255)
- About 18 million addresses in three ranges are reserved for use in private networks. 
- Packets addresses in these ranges are not routable in the public Internet; they are ignored by all public routers. 
- Therefore, private hosts cannot directly communicate with public networks, but require network address translation(NAT) at a routing gateway for this purpose.
- An IP consists of a network part and host part that is determined by it's subnet.

__IP Address Classes__
[geeksforgeeks - blog](https://www.geeksforgeeks.org/introduction-of-classful-ip-addressing/)
[YouTube](https://www.youtube.com/watch?v=vcArZIAmnYQ&t=464s&ab_channel=SunnyClassroom)
![](nethostdata.jpg)
__Reserved private IPv4 network ranges__

|Name|CIDR Block|Address Range|No. of Addresses|Classfull|
|-|-|-|-|-|
|24-bit Block|10.0.0.0/8|10.0.0.0 - 10.255.255.255|16777216|Class A|
|20-bit block|172.16.0.0/12|172.16.0.0 – 172.31.255.255|1048576|Class B|
|16-bit block|192.168.0.0/16|192.168.0.0 – 192.168.255.255|65536|Class C|

#### Internet Protocol Version 6

#### Universal Resource Identifier
![[Pasted image 20220607121018.png | 400]]
- It is sequence of characters, used to identify resources.
- Resources can be Logical or Physical.
- Guidelines are issued by IETF (Internet Engineering Task Force)
- URL and URN are children of the parent URI.
- URIs tries to identify a resource through a name and to provide a means of locating the resource by describing its primary access mechanism.
- URI is of two types:
	- Uniform Resource Name (URN)
		- URN defines an item’s unique identity
	- Uniform Resource Locator (URL)
		- URL provides a method to find a resource
		- ![[Pasted image 20220607121532.png | 400]]






