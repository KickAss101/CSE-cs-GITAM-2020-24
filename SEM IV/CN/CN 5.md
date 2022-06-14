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
### Various IEEE standards
- IEEE 802 - Collection of networking standards that cover the physical and data-link layer specifications for technologies such as Ethernet and wireless.
- IEEE 802.3 - Ethernet Working Group
- IEEE 802.11 - Wireless LAN Working Group
- IEEE 802.15 - Wireless Specialty Network (WSN) Working Group

---
### The Link Layer
[NesoAcademy](https://www.youtube.com/watch?v=N1apF49Ih28&ab_channel=NesoAcademy)
- The data link layer of the OSI model _prepares network data for the physical network_. The data link layer is _responsible for network interface card (NIC) to network interface card communications_. 

 __Service offered by the data link layer__
- Flow control (LLC or DLC (Data Link Control))
- Framing (MAC)
- Physical addressing (MAC addressing) (MAC)
- Error Control (MAC)
- Access Control (MAC)

__The data link layer does the following:__
-   _Enables upper layers to access the media_. The upper layer protocol is completely unaware of the type of media that is used to forward the data.
-   _Accepts data_, usually Layer 3 packets (i.e., IPv4 or IPv6), and _encapsulates them into Layer 2 frames_.
-   _Controls how data is placed and received on the media._
-   _Exchanges frames between endpoints_ over the network media.
-   _Receives encapsulated data_, usually Layer 3 packets, and _directs them to the proper upper-layer protocol_.
-   Performs _error detection and rejects any corrupt frame_.

#### Link layer Sublayers
-   **Logical Link Control (LLC)** 
	- This _IEEE 802.2_ sublayer _communicates between the networking software at the upper layers and the device hardware at the lower layers_. 
	- It places _network protocol data and adds control information_ to help deliver the packet to the destination. This _allows multiple Layer 3 protocols_, such as IPv4 and IPv6, _to use the same network interface and media_
-   **Media Access Control (MAC)** – Implemented in hardware (NIC). 
	- It _provides data link layer addressing_ (MAC address) and it is integrated with various physical layer technologies.
	- It is responsible for:
	-  __Three primary functions__
		- Framing
		- Physical addressing and MAC addressing
		- Error control
	- __Data encapsulation__
		- _Frame assembly before transmission and frame disassembly_ after upon reception of a frame
		- _Header and trailer to network layer PDU_ (Protocol Data Unit) is added here
		-   **Frame delimiting** - The framing process provides important _delimiters to identify fields within a frame_. These delimiting bits provide synchronization between the transmitting and receiving nodes.
		-   **Addressing** - Provides _source and destination addressing_ for transporting the Layer 2 frame between devices on the same shared medium.
		-   **Error detection** - Includes a _trailer used to detect transmission errors_.
	-  __Media access control__
		- Responsible for the _placement of frames on the media_ and the removal of frames from the media
		- _Communicates directly with the physical layer_
		- The MAC sublayer also provides media access control, allowing multiple devices to communicate over a shared (half-duplex) medium. Full-duplex communications do not require access control.

![500](link-layer-0.png)

__At each hop along the path, a router performs the following Layer 2 functions__
1.  Accepts a frame from a medium
2.  De-encapsulates the frame
3.  Re-encapsulates the packet into a new frame
4.  Forwards the new frame appropriate to the medium of that segment of the physical network

#### Multiple Access Link
[DharshanUniversity -YT](https://www.youtube.com/watch?v=aKmBnl8NHz0&ab_channel=DarshanUniversity)
[University of Massachusetts - YT](https://www.youtube.com/watch?v=X2cLpzFRMT4&ab_channel=JimKurose)
- There are two types of network links:
	- __Point-To-Point Link__
		- Consists of a _single sender at one end of the link and a single receiver_ at the other end of the link
	- __Broadcast Link__
		- It can have _multiple sending and receiving nodes_ all connected to the _same, single, shared broadcast channel_.
		- The broadcast term is used here because when any one node transmits a frame, the _channel broadcasts the frame and each of other nodes receives a copy_.
		- Ex: Ethernet, 4G, 5G, Wi-Fi, satellite

#### Multiple Access Protocols
- The __need__ for Multiple Access Protocols:
	- _Collision takes place if a node receives two or more signals at the same time_
- __Multiple access protocol__ is a distributed algorithm that _determines how nodes share channel_ i.e., determine when node can transmit
- _Communication about channel sharing must use channel itself_, no out-of-band channel for coordination

__Types of Multiple Access Protocols__
- Channel Partitioning protocols
- Random Access Protocols
- Taking-Turns Protocols

![[Pasted image 20220611190226.png | 500]]

#### Channel Partitioning Protocols
- _Divides channel into smaller pieces_ (Time slots, frequency slots, code slots)
- Allocate piece to node for exclusive use

__Time Division Multiple Access (TDMA)__
- Access to the channel is _divided into rounds_
- _Each station gets fixed time slot_
- Unused slots go idle
- Suppose the _channel supports N nodes_ and _transmission rate of the channel is R bps_
- TDM divides _time into time frames_ and further divides each _time frame into N time slots_
- Then, _each of the slot is assigned to one of the N nodes_.
- Examples: 2G cellular networks

![[Pasted image 20220611172157.png | 500]]

- Example: 6-station LAN. 1,3,4 have packet, slots 2, 5 & 6 are idle.

__Drawbacks of TDMA__
- A node is _limited to R/N bps_ even when it is the only node with packets to send
- A node must always wait for it's turn in the _transmission sequence_ again, even when it is the only node with a frame to send.

__Frequency Division Access (FDMA)__
- Channel spectrum is _divided into frequency bands_.
- _Each station assigned to a fixed frequency band_
- _Unused transmission time in frequency bands go idle_
- Example: 6-station LAN, 1,3,4 have packets. Frequency bands 2,5,6 idle
- Examples: Walkie-Talkies

![[Pasted image 20220611182936.png | 500]]

__Drawbacks of FDMA__
- _Unused portions of spectrum will be wasted_
- If more than N Users want to communicate, _some of them will be denied permission_, if some users with allocated frequency hardly ever transmit anything

__Code Division Multiple Access__
- CDMA assigns a different _code to each node_.
- Each _node uses it's unique code to encode the data_ bits it sends.
- Different _nodes can transmit simultaneously_.
- Their respective _receiver receives a sender's encoded data bits correctly_ in spite of interfering transmissions by other nodes
- Example: Military and widespread civilian use, BSNL CDMA service

![500](Figure-CDMA-Example-In-above-figure-three-users-A-B-C-communication-with-receiver.png)

#### Taking-Turns Protocols or Controlled Access Protocols
- 

#### Random Access Protocols
- All _stations have same superiority_. Any station can send data _depending on medium's state_ (idle/busy)
- Each station has the _right to the medium without being controlled by any other station_
- If more than one station tires to send, there is an access conflict (collision) and frames will be either destroyed or modified.

__Pure ALOHA__
- Pure ALOHA _allows stations to transmit whenever they have data to be sent_.
- When a station sends data it waits for an acknowledgment
- If _acknowledgment doesn't come_ within the allotted time then the _station waits for a random amount of time called back-off time_ (tb) and re-send the data
- Since _different stations wait for different amount of time_, the _probability of further collision is decreased_.
- The _throughput is maximized when frames are of uniform length_
- When _two frames try to occupy the channel at the same time_, there will be a _collision and both will be garbled_

![[Pasted image 20220611200059.png | 500]]

__Slotted ALOHA__
-  It was _developed to improve the efficiency of pure ALOHA_ as the chances of collision are higher in pure ALOHA
- Time of the shared channel is divided into _discrete time intervals called slots_
- _Sending of data is only allowed at beginning of these time slots._
- If a station misses out the allowed time, it _must wait for the next slot_. This reduces the probability of collision

![500](slotted-aloha.png)

__Carrier Sense Multiple Access Protocol (CSMA)__
-  CSMA developed to _minimize the chance of collision and increase the performance_
- Principle of CSMA - _"Sense before transmit" or "listen before talk"_
- If _channel sensed idle: transmit entire frame_
- If _channel sensed busy: defer transmission_
- Still there's possibility of _collision because of propagation delay_
- __Types of CSMA__
	- 1-Persistent CSMA
	- P-Persistent CSMA
	- Non-Persistent CSMA
	- O-Persistent CSMA

__CSMA with collision detection CSMA/CD__
- Collision _detected within short time_
- _Colliding transmission aborted, reducing channel wastage_
- Collision _detection easy in wired, difficult with wireless_

__CSMA with collision Avoidance CSMA/CA__
- 

#### Switched Local Area Networks
---
### Wireless and Mobile Networks
#### Wireless Links and Networks Characteristics
#### Wi-Fi: 802.11 Wireless LANs
#### Mobile IP