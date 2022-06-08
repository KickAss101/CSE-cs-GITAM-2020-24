## Cloud for IoT:
- IoT with Cloud – Challenges
- Selection of Cloud Service Provider for IoT Applications
- Introduction to Fog Computing
- Cloud Computing: Security Aspects
- Case Study: How to use Adafruit Cloud?

---
### IoT with Cloud - Challenges
- __Privacy and Security__
	- Security is a _major concern in the field of IoT_.
	- Valuable data goes into the cloud, outside the firewall this data becomes hackable.
- __Bandwidth Cost__
	- Bandwidth is one of the challenges because of _continuous data transferring from the IoT devices_.
	- IoT is all about data, and in most cases, this would be _big data_. 
	- _Cloud computing is preferred for storage and processing in IoT_.
	- Small-scale IoT application demand less resources.
	- But if the application is data concentrated, then the _investment in bandwidth would be considerable_.
- __Migration and Portability__
	- When data is to be migrated from the cloud, we have to take care of the followings.
		- How _easy and safe_ is it to move the data?
		- How much _downtime_ would this process require?
		- What is the _strategy to migrate_ data to the cloud?
		- How much would it _cost_?
		- Would there be _support offered to migrate smoothly_ to another cloud service provider?
	- All these challenges are doubled with IoT as the data comes from the various sensory nodes at a very high speed.
- __Availability, Reliability and Robustness__
	- Continuous monitoring and reading of the data need to have _continuous cloud service availability_ in IoT.
	- In downtime, it would miss critical data so reliability of the process has to be monitored.
	- The _process should be robust towards handling data at different rates_.
	- _Data could be flooded or slowed at anytime_, in the both situations it should be _handled effortlessly_.
- __Cost__
	- One of the main advantages of cloud is that _it can scale up with rising demand_.
	- While it is scalable and flexible, an organization should _plan its budget carefully_.
	- _Wrong selection for subscription without having clear vision and planning, it may lead to unnecessary cost_.
- __Data Ownership__
	- The _data stored by the user on the cloud is owned by the user_.
	- This means that the data is under the ownership of the person who generates it.
	- However, when opting for cloud storage, the _data is under the custody of the cloud service provider_.
	- Then, it appears that the service provider owns the data.
	- When it comes to IoT, the _data is generated at multiple points_ and _ownership could lie with multiple participating parties_.
	- Hence, in IoT the _ownership-related challenges are multiplied_.
- __Expertise__
	- To use the cloud with IoT requires a _specific skill set_.
	- The cloud platform gets updated every now and then and so _experts have to constantly upgrade themselves_.
	- Expertise is a definite challenge.
	- When IoT and cloud comes together then it will be more challenging
	- To _understand the sensors and at the same time, to be updated on cloud development_ is a challenging task.


---
### IoT Cloud Computing
- Cloud computing is the _delivery of computing services over the internet_, by providing flexible, affordable, effective and efficient resources for development.
- That includes _servers, storage, databases, networking, software, analytics, and intelligence_.
- Cloud computing provide _economical freedom along with technical strength to the application_.
- In other word, it is about _outsourcing of IT services and infrastructure to make them available anywhere via the Internet_.

#### Types of Cloud Computing
![[Pasted image 20220606184846.png]]
#### Public
- The cloud _resources are owned and managed by a third-party_ cloud service provider.
- _Pay as per_ usage approach makes it most cost effective model.

__Advantages__
- __Cost__: Cloud computing eliminates the _cost of purchasing hardware and software, setting up and infrastructure management_.
- __Setting up a cloud service__: Cloud computing services are provided as self service and on demand. With a few mouse clicks, we can set up a cloud service.
- __Data Security__: Cloud offers many _advanced features related to security_ and ensures that data is securely stored and handled.
- __Reliability__: Cloud computing has _data backup, disaster recovery_.
- __Scalability__: Ability  to _scale up and flexibility_. It means increasing and decreasing IT resources are easy on cloud computing. Like power, storage, bandwidth etc
-  __Excellent accessibility__: Cloud allows us to _quickly and easily access store information anywhere, anytime_ in the whole world, using an internet connection

__Disadvantages__
- __Difficult to migrate:__ Organizations may face problems when transferring their services from one vendor to another. As different vendors provide different platforms, that can cause _difficulty moving from one cloud to another_.
- __Limited Control:__ As we know, cloud infrastructure is completely owned, managed, and monitored by the service provider, so the cloud users have less control over the function and execution of services within a cloud infrastructure.
- __Security:__ Although cloud service providers implement the best security standards to store important information. While sending the data on the cloud, there may be a chance that your organization's information can be hacked by Hackers.
- __Privacy:__ Though cloud providers offer good security and privacy policies there can always be a chance of insider's threat, hackers stealing and leaking confidential information from these cloud services using any security vulnerability that the cloud computing service provider has.
- __Requires Internet:__ It is _compulsory to have internet_ in order to access the services/data that the cloud service provider offer.

#### Private
- Private cloud provides _computing services within the organization’s private network_ and selected other users.
- In this cloud model all the hardware, software, datacenter, employees, infrastructure, etc., are _maintained, monitored, and installed by the organization_.
- This particular deployment model can be _chosen wherever __confidentiality__ matters the most_.

__Advantages__
- _High level of security and privacy_
- _More control and flexibility_ in terms of deciding and managing the resources

__Disadvantages__
- _Very Expensive_
- _Need technical skill_ for maintaining  and difficult to management
- _Policies and other related things are to be framed carefully_ to make sure that the data is safe

#### Hybrid
- This deployment is a _mix of both private and public cloud deployment_.
- The resources offered and managed are both in-house and third party based

__Advantages__
- _Less investment_ needed to setup the infrastructure
- _Less technical skill_ required to manage and maintain the cloud
- _Customer support_ team can be reached on demand
- _Easily scaled up or scaled down_ based on requirements

__Disadvantages__
- _Security and privacy_ issues are the major challenges
- _Less flexibility and controls_ compare to public cloud

---
### Types of Cloud service Providers
__Infrastructure as a Service__
- Provider supplies the _basic compute, storage and networking infrastructure along with the hypervisor_ - the virtualization layer.
- Users must then _create virtual instances such as VMs and containers, install OS, support applications and data, and handle all of the configuration and management associated with those tasks_.
- The _consumer does not manage or control the underlying cloud infrastructure_ but _has control over operating systems, storage, and deployed applications_.
- This service provides you with the _highest level of flexibility_.
- Some examples of IaaS services are DigitalOcean, AWS, Azure, Google

__Platform as a Service__
- It provides a _development environment to application developers_.
- Operating system, programming-language execution environment, database, web server, development tools, APIs, libraries, etc., will be provided by the cloud service provider.
- Users have to _build, manage and maintain the applications_.
- Application developers _develop and run their software on a cloud platform_ instead of directly buying and managing the essential hardware and software layers.
- PaaS products include Google App Engine, Heroku, Zoho

__Software as a Service__
- Complete _software application as a service is provided_ to the user that is run and managed by the service provider.
- Typically, SaaS applications are completely accessible via internet web browser.
- SaaS providers _manage the application workload and all underlying IT resources_; users only control the data created by the SaaS application.
- Examples of SaaS include Salesforce, Dropbox and Google Workspace, Netflix, Zoom.

---
### Selection of Cloud Service Provider for IoT Applications
__Parameters to consider when choosing a cloud service provider__
- Certification and Standards Compliance
	- 
- Financial Health of the Service Provider
- Business and Technology Strength
- Compliance Audit
- Service Level Agreements
- Reporting/Tracking
- Costing and Billing
- Maintenance Monitoring and Upgrade
- Support
- Security

---
### Introduction to Fog Computing
- IoT is all about the data. The factors that affect data are the four Vs - _variety, velocity, veracity and volume_.
- All IoT applications require _instant analysis and action_.
- In case the _data volume is high_ and it reaches the cloud after _some delay_.
- Or sometimes we want to _distribute the data to other IoT devices_.
- In such cases, fog computing serves the solution
- The most _sensitive data should be analyzed in the area closer_ to the place where it is generated.
- Using fog computing we can _process the data locally_ and to avoid the trouble by not sending the data to the cloud.
- _Respond much faster because of data is moving locally_ so data travel is reduced considerably.
- Only the _required data will be sent to the cloud for further processing or storage or distribution to other nodes of the network_.
- This will be based on _storage requirements and guidelines_.
- _Predictive analytics can also be carried out with the data stored in the cloud_.
- The _fog is below cloud_, which means it is _closer to the elements that generate data_.
- _After analysis, the data stored is pushed on to the cloud_.
- Results in _increased efficiency and safety both physical and asset safety_.
- Some __examples__ where faster response time is extremely important are _factory or manufacturing line, oil and gas tube lines fault analysis, on-flight diagnosis, and healthcare_.
![[Pasted image 20220607092631.png | 400]]
![[sensors-17-01695-g001.webp | 400]]


__Advantages of Fog Computing__
- _Minimal amount of data sent to the cloud_.
- _Reduced bandwidth_ consumption.
- _Reduced data latency_.
- _Improved data security_. When limited data goes to cloud, it is easier to protect it.
- _Immediate processing of data in real time_ (this is very much needed in industrial applications).

![[Pasted image 20220607092144.png | 400]]

#### Working of Fog Computing
- Sensors/devices generate data  to _transmit it to the middle layer_ (Fog), which is very close the data source.
- These nodes in the _middle layer are capable of handling the data_.
- This requires _minimum power and lesser resources_.
- _All the data need not go to the cloud_ at the instant.
- Also, _sensitive data gets processed very fast, which results in an instant response_.
- _Fog is not meant for hefty storage_. It is still the cloud that does the task of storing big data.
- Fog is just an _intermediary layer for faster data processing_, and the _faster response_. 

#### Fog Computing v/s Edge Computing
| Fog Computing | Edge Computing |
| - | - |
|Data processing is moved to the processors that are connected to the local area network (LAN), making it a little farther from the sensors and actuators. | Edge computing is the computing carried out at the device itself, where all the sensors are-connected.|

_Thus, the main difference between edge and fog computing is the distance._

---
### Cloud Computing: Security aspects
- The security of any computing platform including cloud computing depends on:
	- __Software security__
		- Software is the core component and plays a vital role in presenting and ensuring a secure environment.
		- If there are _defects_ created/generated during the development phase, it is a _software security threat_.
		- Defects such as simple software implementation defects, _memory allocation, design issues, and exception handling_ all contribute to _security issues_.
		- This can be ensured by complete and _comprehensive testing_ carried out at all-stages.
	- __Infrastructure security__
		- Making sure that the infrastructure provided by the CSP is safe.
		- _Third party could also contribute to the infrastructure._
		- It is extremely important to _check the security vulnerabilities_ with the infrastructure.
		- All infrastructure related _guidelines should be mentioned clearly in the agreements and should be made transparent to the customer_.
		- If data is damaged, everything is damaged and lost.
		- Hence, care should be taken to protect the infrastructure.
	- __Storage security__
		- It is important to be informed of _who owns the data and the location where it is stored_.
		- _Data leak, snooping, malware attacks, etc. are all threats to the stored data_ and can be listed under storage security.
		- Appropriate _antivirus software and periodic monitoring_, should help protect the data.
	- __Network security__
		- Data is stored in the cloud via the Internet, and hence _all network threats become a possibility_.
- If any of these is compromised, it would result in security violation and could cause damages.