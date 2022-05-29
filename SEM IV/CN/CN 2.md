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
	- Socket is an _interface between the Application layer and Transport layer_
	-  _TCP keeps the data in its buffer while sending and receiving the data._
- __Addressing Processes__
	- In a network, a host is identified by it's _IP address & a port_ number to identify the process that is in communication.
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

#### HTTP Request Message Format
```http
GET / HTTP/1.1
Host: www.yahoo.com
Connection: close  
User-agent: Mozilla/5.0  
Accept-language: en-us
```

#### HTTP Response Message Format
```http
HTTP/1.1 200 ok
Connection: close  
date: Sat, 28 May 2022 15:44:04 GMT  
Server: Apache/2.2.3 (CentOS)  
Last-Modified: Sat, 28 May 2022 15:11:03 GMT  
Content-Length: 6821  
Content-Type: text/html
```
#### HTTP Status Codes
![[HTTP-Status-Codes-1.png | 500]]
#### User-Server Interaction: Cookies
- _HTTP server is stateless._ This simplifies server design and has permitted engineers to develop high-performance Web servers that can handle thousands of simultaneous TCP connections. 
- However, it is often desirable for a Web site to identify users, either because the server wishes to restrict user access or because it wants to serve content as a function of the user identity. For these purposes, HTTP uses cookies.
- __Cookies__ allow sites to keep track of users. 
- An **HTTP cookie** is a _small piece of data that a server sends to a user's web browser_. The _browser may store the cookie and send it back to the same server with later requests_. Typically, an HTTP cookie is used _to tell if two requests come from the same browser_—keeping a user logged in, for example. 
![[cookie.png | 450]]
#### Web Caching
- A Web cache, also called a proxy server, is a _network entity that satisfies HTTP requests on the behalf of an origin Web server_. The Web cache _has its own disk storage and keeps copies of recently requested objects in this storage_.
- A user’s _browser can be configured_ so that all of the user’s HTTP requests are first directed to the Web cache.
1. The browser establishes a TCP connection to the Web cache and sends an HTTP request for the object to the Web cache.
2. The Web cache _checks to see if it has a copy of the object stored locally. If it does, the Web cache returns the object within an HTTP response message to the client browser_.
3. If the Web cache does not have the object, the Web cache opens a TCP connection to the origin server. The _Web cache then sends an HTTP request for the object into the cache-to-server TCP connection_.
4. After receiving this request, the origin server sends the object within an HTTP response to the Web cache. When the Web cache receives the object, it stores a copy in its local storage and sends a copy, within an HTTP response message, to the client browser (over the existing TCP connection between the client browser and the Web cache)
![[kurose_320719_c02f10.gif | 400]]

#### The Conditional GET
- Although caching can reduce user-perceived response times, it introduces a new problem - the copy of an object residing in the cache may be stale. In other words, the object housed in the Web server may have been modified since the copy was cached at the client. 
- Fortunately, HTTP has a mechanism that allows a cache to verify that its objects are up to date. This mechanism is called the _conditional GET_.
- An HTTP request message is a so-called conditional GET message if:
1. the request message uses the GET method and
2. the request message includes an `If-Modified-Since:` header line

#### File Transfer Protocol(FTP)
![[ftp-diagram.gif | 350]]
- FTP is an application layer protocol that is used to transfer files across the internet
- FTP uses _port 21 as control connection_ and _port 20 for data transfer_
- 
![[kurose_320719_c02f14.gif | 300]]
---
### Electronic Mail in the Internet
E-mail has three major components: user agents, mail servers, and the Simple Mail Transfer  Protocol (SMTP)
__User agent:__ It allows users to read, reply to, forward, save, and compose messages.
__Mail Server:__ It is an application that receives incoming email from local users and remote senders and forwards outgoing messages for delivery. A computer dedicated to running these applications is also called a _mail server_.
__SMTP:__ It is an application layer protocol for electronic mail. It uses the reliable data transfer service of TCP to transfer mail from _sender's mail server to the recipient's mail server_.

__Types of Mail servers__
[blog - mail service protocols](https://www.navigator.ca/support/imap-pop3-smtp/)
- incoming mail servers (POP3, IMAP)
- outgoing mail servers (SMTP)

__Incoming Mail Servers__
- __POP3__
	- POP3 stands for __Post Office Protocol 3__. It is a mail protocol used to _retrieve mail from a remote server to a local email client_.  
	- POP3 _copies only the inbox folder_ from the remote server into the local mail client which means it doesn't download remaining folders like sent box, drafts etc.
	- _Mail is deleted after it is downloaded from the server_. This saves space on the server. Optionally, you may have a option to leave a copy on the server depending upon the email service you're using.
	- POP3 _lacks synchronization_ across multiple devices. 
	- However, POP3 is a very simple mail protocol making it less prone to errors and allows for a much _easier implementation_.
- __Ports used for POP3__
	-   Port 110 – Default POP3 port.
	-   Port 995 – POP3 port used for SSL/TLS.
- __IMAP__
	- IMAP stands for __Internet Message Access Protocol__. It is an application layer protocol which is used to _receive the emails from the mail server_. 
	- It allows viewing the emails from multiple devices, _email is kept on email server_ and caches local copies of the email onto all of the devices.
	- And, also it _synchronizes all the folders and it's contents_ across all of the devices like inbox, trash, sent box, drafts
- __Ports used by IMAP__
	-   Port 143: It is a non-encrypted IMAP port.
	-   Port 993:  IMAP encrypted.
- ![[3537.png | 450]]
- __SMTP__
	- SMTP stands for __Simple Mail Transfer Protocol__. It is an application layer protocol for electronic mail. It uses the reliable data transfer service of TCP to transfer mail from _sender's mail server to the recipient's mail server_.
	- The main purpose of SMTP is used to _set up communication rules between servers_.
	- It is usually _used with one of two other protocols, POP3 or IMAP_, that let the user save messages in a server mailbox and download them from the server.
- __Ports used by SMTP__
	- 25 - default SMTP port
	- 2525, 587 - alternative ports

![[smtp-message-flow.png | 500]]

---
### DNS - The Internet’s Directory Service
[YouTube - DNS Records](https://www.youtube.com/watch?v=6uEwzkfViSM&ab_channel=itfreetraining) [YouTube - DNS Explained](https://www.youtube.com/watch?v=72snZctFFtA&ab_channel=DNSMadeEasyVideos)
- __DNS__ stands for "Domain Name System". It is the _hierarchical and decentralized naming system used to identify computers reachable through the Internet or other IP networks_
- DNS is a _directory service_ that provides a _mapping between the name of a host on the network and its numerical address_.
- DNS is required for the functioning of the internet.
- DNS is a _service that translates the domain name into IP addresses_. This allows the users of networks to utilize user-friendly names when looking for other hosts instead of remembering the IP addresses.
- For example, suppose user wants to reach google.com that has an IP address of  142.250.195.206, most people would reach this site by specifying www.google.com. Therefore, the domain name is more reliable than IP address.

##### DNS Hierarchy
![[xOdVIPZ.png | 500]]

__Root Zone Server__
- The root is the base of the DNS hierarchy tree. 
- It's called the Root Zone because there are actually 13 Root servers. These servers are spread out geographically and are the _starting place for traversing DNS via resolution_.
- These servers can directly _answer queries for records stored or cached within the root zone_, and they can also _refer other requests to the appropriate Top Level Domain server_

__Top Level Domain__
- A TLD nameserver _maintains information for all the domain names that share a common domain extension_, such as .com, .net etc. For example, a .com TLD nameserver contains information for every website that ends in ‘.com’.
- Management of TLD nameservers is handled by the _Internet Assigned Numbers Authority_ (IANA). The IANA breaks up the _TLD servers into two main groups_:
- __Generic top-level domains:__ These are domains that are not country specific, some of the best-known generic TLDs include .com, .org, .net, .edu, and .gov.
- __Country code top-level domains:__ These include any domains that are specific to a country or state. Examples include .uk, .us, .ru, .in and .jp.
- When a _TLD gets a dns query request, it would respond by pointing to the authoritative nameserver_  for that domain.

__Authoritative Name Server__
- When a recursive resolver receives a response from a TLD nameserver, that response will direct the resolver to an authoritative nameserver. The authoritative nameserver is usually the resolver’s last step in the journey for an IP address.
- The _authoritative nameserver contains information specific to the domain name it serves_ (e.g. google.com) and it can provide a recursive resolver with the IP address of that server found in the DNS "A" record.

__Third Level Domain__
- A third-level domain is the next highest level following the second-level domain in domain name hierarchy.
- It is the segment that is _found directly to the left of the second-level domain_. The third-level domain is often called a "subdomain"

__DNS Query__
- A __recursive resolver__ (also known as a DNS recursor) is the first stop in a DNS query. The recursive resolver _acts as a middleman between a client and a DNS nameserver_.
- After receiving a DNS query from a web client, a _recursive resolver will either respond with cached data, or send a request to a root nameserver_, followed by another request to a TLD nameserver, and then one last request to an authoritative nameserver.
- After receiving a response from the authoritative nameserver containing the requested IP address, the _recursive resolver then sends a response to the client_.
- During this process, the _recursive resolver will cache information received from authoritative name servers_.
![[60ec9048a730906ff0bfc36d_DNS_SERVER_UPDATE-01.png | 500]]

 

---
### Socket Programming: Creating Network Applications 


