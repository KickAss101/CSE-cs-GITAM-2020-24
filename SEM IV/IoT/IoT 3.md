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
- It does not require that both the client and the server establish a connection at the same time.
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
	- 0 - At most once (Best effort, no ACK)
	- 1 - At least once (Acked, retransmitted if ack not received)
	- 2 - Exactly once (Request to publish, clear to send)
**TOPIC**
- The label provided to the message is checked against the subscription known by the server is known as TOPIC.

![[mqtt-protocol2.jpg | 350]]


![[mqtt-protocol3.jpg| 400]]

- Suppose a device has a temperature sensor and wants to send the rating to the server or the broker. If the phone or desktop application wishes to receive this temperature value on the other side, then there will be two things that happened. 
- The _publisher first defines the topic_; for example, the temperature then publishes the message, i.e., the temperature's value. 
- _After publishing the message_, the phone or the desktop application on the other side will subscribe to the topic, i.e., temperature and then receive the published message, i.e., the value of the temperature. 
- The server or the _broker's role is to deliver the published message_ to the phone or the desktop application

__MQTT Message Format__

![[mqtt-protocol4.jpg]]

#### Constrained Application Protocol (CoAP)

---
### Transport Protocols

#### Bluetooth Low Energy (BLE)

#### Light Fidelity (LiFi)
---
### Addressing and Identification
#### Internet Protocol Version 4

#### Internet Protocol Version 6

#### Uniform Resource Identifier




