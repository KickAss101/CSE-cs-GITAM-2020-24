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
	![[bigPic.jpg | 500]]

__Transport Service Available to application__


__Transport service provided by internet__


__Application layer protocol__


---
### The Web and HTTP

---
### Electronic Mail in the Internet

---
### DNS - The Internet’s Directory Service
- __DNS__ stands for "Domain Name System".  It is the hierarchical and decentralized naming system used to identify computers reachable through the Internet or other IP networks
 

---
### Socket Programming: Creating Network Applications 

