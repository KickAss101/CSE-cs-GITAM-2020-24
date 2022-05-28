## Application Layer
- Principles of Network Applications
- The Web and HTTP
- Electronic Mail in the Internet
- DNS - The Internet’s Directory Service
- Socket Programming: Creating Network Applications 

__Learning Outcomes__ 
• summarize the principles governing the working of network applications
• outline the working of popular applications in the Internet
• develop simple network applications using socket programming

---
### Principles of Network Applications
[github - blog](https://jerry4013.github.io/Github-blog/2019/09/27/Network-9.html) [YouTube - 1 (poor)](https://www.youtube.com/watch?v=OrwRTNJYghY&ab_channel=NehaSharma) [YouTube - 2 (ok)](https://www.youtube.com/watch?v=ZJFP4u-IOeI&ab_channel=MITMysoreCSE)
- Network Application Architecture
- Process Communicating
- Transport Service Available to application
- Transport service provided by internet
- Application layer protocol

__Network Application Architecture__
Types of Network Application Architecture
- Client-Server
- Peer-to-Peer

>__Client:__ A client is the receiving end of a service or the requestor of a service.
__Server:__ A server is a computer equipped with specific programs and/or hardware that enables it to offer services to clients on its network.

- __Client-Server:__ It is a distributed application structure that partition tasks or workloads between the providers of a resource or service called servers, and service requesters called clients.

- __Peer-to-Peer:__ It is a distributed application architecture that partitions tasks or workloads among peers. Peers are equally privileged nodes in a network.

__Process Communicating__
- The process that initiates the communication is labeled as _client_ and the process that waits to be contacted to begin the session is the _server_
- __The Interface Between the Process and Network__
	- Processes on different end systems communicate with each other through a software interface known as _sockets_
	- Socket is an interface between the Application layer and Transport layer
- __Addressing Processes__
	- In a network, a host is identified by it's _IP address & a port_ number to identify the process that is in communication.
- __TCP Buffer__
	- 
	![[bigPic.jpg | 500]]

__Transport Service Available to application__
[blog - eletronicspost](https://electronicspost.com/transport-services-available-to-applications/)
We can broadly classify the possible services along four dimensions: reliable data transfer, throughput, timing, and security.

- __Reliable Data Transfer__
	- If a protocol provides a guaranteed data delivery service _correctly and completely_ to the other end of the application then it is said to provide **reliable data transfer**.
	- The applications like multimedia applications such as conversational audio/video can tolerate some amount of data loss, such application are called as __loss-tolerant applications__.
- __Throughput__
	- >The amount of data moved _completely and successfully_ from one place to another in a given time period is called throughput

	- Transport-layer protocol could provide _guaranteed available throughput at some specified rate_.
	- With such a service, the _application could request_ a **guaranteed** throughput of r bits/sec and the transport protocol would then ensure that the available throughput is always at least r  bits/sec. 
	- Applications that have throughput requirements are said to be **bandwidth-sensitive** applications.
	- The available throughput can fluctuate with time.
	- Elastic applications can make use of as much, or as little, throughput as happens to be available. For example, e-mail, file transfer, and Web transfers.

- __Timing__
	- A transport-layer protocol can also provide timing guarantees. 
	- Interactive real-time applications, such as Internet telephony, virtual environments, teleconferencing, and multiplayer games _require tight timing constraints on data delivery_ in order to be effective.
- __Security__
	- A transport protocol can _encrypt all data transmitted by the sending process_, and in the receiving host, the transport-layer protocol can decrypt the data before delivering the data to the receiving processes. 
	- A transport protocol can also provide other security services in addition to _confidentiality, including data integrity and end-point authentication_.
	-  ___Just for example:___

![[Requirements+of+Selected+Network+Applications.jpg | 500]]

__Transport service provided by internet__
- The Internet makes two transport protocols available to applications, UDP and TCP.
- __TCP__ service model includes a _connection-oriented service and a reliable data transfer service_
	- __Connection-oriented service:__ After the handshaking phase, a **TCP connection** is said to exist between the sockets of the two processes. The connection is a full-duplex connection in that the two processes can send messages to each other over the connection at the same time. When the application finishes sending messages, it must tear down the connection.
	- __Reliable data transfer service:__ The communicating processes can rely on TCP to deliver all data sent without error and in the proper order.
	- TCP also includes a congestion-control mechanism.
- __UDP__ 
	- UDP is _connectionless_, so there is _no handshaking_ before the two processes start to communicate. 
	- UDP provides an _unreliable data transfer service_—that is, when a process sends a message into a UDP socket, UDP provides no guarantee that the message will ever reach the receiving process. 
	- UDP does not include a congestion-control mechanism (so the sending side of UDP can pump data into the layer below (the network layer) at any rate it pleases)

__Application layer protocol__
- An application-layer protocol defines _how an application’s processes, running on different end systems, pass messages to each other_. It defines:
- The types of messages exchanged, for example, request messages and response messages
- The syntax of the various message types, such as the fields in the message and how the fields are delineated
- The semantics of the fields, that is, the meaning of the information in the fields
- Rules for determining when and how a process sends messages and responds to messages.
---
### The Web and HTTP
#### Brief note on Web
[YouTube - Web&HTTP](https://www.youtube.com/watch?v=jRM5ShKyIWI&ab_channel=DarshanUniversity)
- In the early 1990s, the internet was used only by researchers, academics and in universities.
- In 1989, Tim Berners-Lee invented _World Wide Web_
- The World Wide Web (WWW), commonly known as Web, is the world's dominant software platform. 
- WWW is an _information space where documents and other web resources are identified by URL and can be accessed_ through the internet using a web browser. 
- The web resources may be any type downloadable media like images, videos, audio files, pdfs, e-books etc. 
- With the Web, on demand is available unlike TV and Radio
- __Web pages__ are documents interconnected by hypertext links formatted in Hypertext Markup Language (HTML), hypertext links permit users to navigate to other web resources. 
- The __URL__ (Uniform Resource Locator) consists of subdomain, second-level domain, top-level domain and a path to the resource that we want to access.
#### Overview of HTTP
- __HTTP__ stands for HyperText Transfer Protocol, an application layer protocol
- It is implemented in two programs: server program and client program
- The client and server communicate with each other by exchanging HTTP messages
-  HTTP _defines the structure of these messages and how the client and server exchange the messages_.
- When a user requests a Web page, the browser sends HTTP request message for the objects in the page to the server. The server receives the requests and responds with HTTP response messages that contain the objects.
- HTTP uses _TCP as it's underlying transport protocol_. The HTTP client first initiates a TCP connection with server. Once the connection is established, the _browser and the server processes access TCP through their socket interfaces_.
- HTTP is a _stateless protocol_ because it doesn't store any state information about the client.
- ![[httprequestflow.png | 500]]
- __HTTP connection types:__
	- Non-persistent HTTP (Separate TCP connection)
	- Persistent HTTP (Same TCP connection)
- __Non-persistent HTTP__
	- The HTTP _client process initiates a TCP connection to the server on port number 80_, which is the default port number for HTTP. Associated with the TCP connection, there will be a socket at the client and a socket at the server.
	- The HTTP _client sends an HTTP request message to the server via its socket_. The request message includes the path name for the resource. 
	- The HTTP server process receives the request message via its socket, retrieves the object from its storage (RAM or disk), _encapsulates the object in an HTTP response message, and sends the response message_ to the client via its socket.  
	- The HTTP _server process tells TCP to close the TCP connection_.  
	- The HTTP _client receives the response message. The TCP connection terminates._ The message indicates that the encapsulated object is an HTML file. The client extracts the file from the response message, examines the HTML file, and finds references to the remaining resources like images, videos etc.  
	- The _first four steps are then repeated for each of the referenced objects_.
	- ![[kurose_320719_c02f07-1.gif | 380]]
	- Round-trip time (RTT) is the _time it takes for a small packet to travel from client to server and then back to the client_. 
	- The RTT includes _packet-propagation delays, packet queuing delays_ in intermediate routers and switches, and _packet-processing delays_.  
	- When a user clicks on a hyperlink, the browser initiate a TCP connection between the browser and the Web server; this involves a “three-way handshake”—the client sends a small  TCP segment to the server, the server acknowledges and responds with a small TCP segment, and, finally, the client acknowledges back to the server.
	- The _first two parts of the three way handshake take one RTT_.  
	- After completing the first two parts of the handshake, the _client sends the HTTP request message combined with the third part of the three-way handshake_ (the acknowledgment) into the TCP connection.  
	- Once the request message arrives at the server, the _server sends the HTML file into the TCP connection_. This HTTP request/response eats up another RTT. Thus, roughly, the _total response time is two RTTs plus the transmission time_ at the server of the HTML file.
- __Persistent HTTP__
	- A _brand-new connection must be established and maintained for each requested object_. For each of these connections, _TCP buffers must be allocated and TCP variables must be kept in both the client and server_. This can place a _significant burden on the Web server_, which may be serving requests from hundreds of different clients simultaneously.  
	- _Each object suffers a delivery delay of two RTTs— one RTT to establish the TCP connection and one RTT to request and receive an object._ With persistent connections, the server leaves the _TCP connection open after sending a response_. 
	- _Subsequent requests and responses between the same client and server can be sent over the same connection_ which reduces latency in subsequent requests(no handshaking and no slow start). Reduced CPU usage and round-trips because of fewer new connections. In particular, an _entire Web page can be sent over a single persistent TCP connection_. 
	- Moreover, multiple Web pages residing on the same server can be sent from the server to the same client over a single persistent TCP connection.




---
### Electronic Mail in the Internet

---
### DNS - The Internet’s Directory Service
- __DNS__ stands for "Domain Name System".  It is the hierarchical and decentralized naming system used to identify computers reachable through the Internet or other IP networks
 

---
### Socket Programming: Creating Network Applications 

