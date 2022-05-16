## Communication in the IoT
- Internet Principles
- __Internet Communications__ 
	- An Overview, IP, TCP, The IP Protocol Suite (TCP/IP), UDP, IP Addresses, DNS, Static IP Address Assignment, Dynamic IP Address Assignment, IPv6, MAC Addresses, TCP and UDP Ports
- __An Example:__ HTTP Ports, Other Common Ports
- __Application Layer Protocols__
	- HTTP
	- HTTPS: Encrypted HTTP
	- Other Application Layer Protocols.  

__Learning Outcomes__
• interpret different protocols and compare them
• select which protocol can be used for a specific application
• utilize the Internet communication protocols for IoT applications

---
### Internet Principles
> Chapter 3 in given E-book
---
### Internet Communications
#### IP
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

#### TCP
[YouTube](https://www.youtube.com/watch?v=xMtP5ZB3wSk&ab_channel=SunnyClassroom)
- TCP stands for Transmission Control Protocol
- It is a _reliable and connection-oriented_ transport protocol
- With TCP, data can be delivered successfully and accurately
- Many application such as web, email and FTP use TCP
- Before TCP transmit data, it'll use _three-way handshake_ to establish a connection
-  __Three-way Handshake:__
	- Client sends a SYN (synchronize) packet to server
	- If the server is up, it replies with SYN-ACK packet which means synchronization is acknowledged and asks for the client to open a connection
	-  The client replies with ACK (acknowledgement) with a connection open
	- Then the two way connection is established
	<img src=a2VfMV8ucG5n.webp width=500>
	<img src=Y2Vzcy5wbmc.webp width=500>

#### TCP/IP Suite
<img src=LmpwZw.webp width=500>

#### UDP
#### IP Addresses
#### DNS
[YouTube - DNS Records](https://www.youtube.com/watch?v=6uEwzkfViSM&ab_channel=itfreetraining) [YouTube - DNS Explained](https://www.youtube.com/watch?v=72snZctFFtA&ab_channel=DNSMadeEasyVideos)
- DNS stands for Domain Name System

##### DNS Records
- __["A" Record](https://dnsmadeeasy.com/post/what-is-an-a-record) and AAAA__
	- An A record stores IPv4 address for a domain name
	- The AAAA record stores IPv6 address for a domain name
- __Canonical Name (CNAME)__
	- Canonical name is an alternative record or alias that maps one domain name to another.
	- Oftentimes, when sites have subdomains such as blog.example.com or shop.example.com, those subdomains will have CNAME records that point to a root domain (example.com). This way if the IP address of the host changes, only the DNS "A" record for the root domain needs to be updated and all the CNAME records will follow along with whatever changes are made to the root.

![[627d639cbbc41b8058488033_A_RECORD_DNS_EXAMPLE.png | 300]]
- __Mail Exchange (MX)__
	[YouTube - MX Record](https://www.youtube.com/watch?v=aWWZ85UAsCg&t=135s&ab_channel=GoogleWorkspace)
	- MX record identifies mail servers for a domain name 
	- It consists of list of mail servers that receive incoming mails
	- The priority values indicate preference; the lower 'priority' value is preferred.

|example.com|record type|priority|value|TTL|
|-|-|-|-|-|
|@|MX|10|mailhost1.example.com|45000|
|@|MX|20|mailhost2.example.com|45000|

- __Service Record (SRV)__
	- 
- __Start of Authority__
- __Name Server (NS)__
- __Pointer (PTR)__

##### DNS Query

![[FSpdrzuUAAAS0BX.jpg | 750]]

#### Static IP Address Assignment
#### Dynamic IP Address Assignment
#### IPv6
#### MAC Addresses
#### TCP and UDP Ports
#### HTTP Ports, Other Common Ports

---
### Application Layer Protocols
#### HTTP
#### HTTPS
#### Other Application Layer Protocols
