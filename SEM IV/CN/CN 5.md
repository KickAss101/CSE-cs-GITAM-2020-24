## The Link Layer
- Introduction to the Link Layer
- Multiple Access Links and Protocols
- Switched Local Area Networks  

## Wireless and Mobile Networks
- Introduction
- Wireless Links and Network Characteristics
- Wi-Fi: 802.11 Wireless LANs (Architecture and MAC Protocol)
- Mobile IP  

__Learning Outcomes__
- summarize the protocols used for multiple access links
- compare the characteristics of wireless networks with those of wired networks
- outline the working of IEEE 802.11 standard and Mobile IP

---
### The Link Layer
[NesoAcademy](https://www.youtube.com/watch?v=N1apF49Ih28&ab_channel=NesoAcademy)
- The data link layer of the OSI model _prepares network data for the physical network_. The data link layer is _responsible for network interface card (NIC) to network interface card communications_. 
- __Service offered by the data link layer__
	- Flow control (LLC or DLC (Data Link Control))
	- Framing (MAC)
	- Physical addressing (MAC addressing) (MAC)
	- Error Control (MAC)
	- Access Control (MAC)
- __The data link layer does the following:__
	-   _Enables upper layers to access the media_. The upper layer protocol is completely unaware of the type of media that is used to forward the data.
	-   _Accepts data_, usually Layer 3 packets (i.e., IPv4 or IPv6), and _encapsulates them into Layer 2 frames_.
	-   _Controls how data is placed and received on the media._
	-   _Exchanges frames between endpoints_ over the network media.
	-   _Receives encapsulated data_, usually Layer 3 packets, and _directs them to the proper upper-layer protocol_.
	-   Performs _error detection and rejects any corrupt frame_.
- The IEEE 802 LAN/MAN data link layer Sublayers:
	-   **Logical Link Control (LLC)** - This _IEEE 802.2_ sublayer _communicates between the networking software at the upper layers and the device hardware at the lower layers_. 
	- It places _network protocol data and adds control information_ to help deliver the packet to the destination. This _allows multiple Layer 3 protocols_, such as IPv4 and IPv6, _to use the same network interface and media_
	-   **Media Access Control (MAC)** – Implemented in hardware (NIC). It is responsible for:
		- __Data encapsulation__
			- Frame assembly before transmission and frame disassembly after upon reception of a frame
			- Header and trailer to network layer PDU (Protocol Data Unit) is added here
		-  __Media access control__
			- Responsible for the _placement of frames on the media_ and the removal of frames from the media
			- Communicates directly with the physical layer
		- It _provides data link layer addressing_ (MAC address) and it is integrated with various physical layer technologies.
		- __Three primary functions__
			- Framing
			- Physical addressing and MAC addressing
			- Error control

![[Pasted image 20220610225306.png | 500]]

#### Multiple Access links and protocols


#### Switched Local Area Networks
---
### Wireless and Mobile Networks
#### Wireless Links and Networks Characteristics
#### Wi-Fi: 802.11 Wireless LANs
#### Mobile IP