## Cloud for IoT:
- IoT with Cloud – Challenges
- Selection of Cloud Service Provider for IoT Applications
- Introduction to Fog Computing
- Cloud Computing: Security Aspects
- Case Study: How to use Adafruit Cloud?

---
### IoT with Cloud - Challenges
- __Privacy and Security__
	- 
- __Bandwidth Cost__
	- Bandwidth is one of the challenges because of _continuous data transferring from the IoT devices_.
	- IoT is all about data, and in most cases, this would be _big data_. 
	- Cloud computing is preferred for storage and processing in IoT.
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
	- However, when opting for cloud storage, the data is under the custody of the cloud service provider.
	- Then, it appears that the service provider owns the data.
	- When it comes to IoT, the data is generated at multiple points and ownership could lie with multiple participating parties.
	- Hence, in IoT the ownership-related challenges are multiplied.
- __Expertise__
	- 


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
- High level of security and privacy
- More control flexible in terms of deciding and managing the resources

__Disadvantages__
- Very Expensive
- Need technical skill for maintaining  and difficult to management
- Policies and other related things are to be framed carefully to make sure that the data is safe

#### Hybrid
- This deployment is a _mix of both private and public cloud deployment_.
- The resources offered and managed are both in-house and third party based

__Advantages__
- Less investment needed to setup the infrastructure
- Less technical skill required to manage and maintain the cloud
- Customer support team can be reached on demand
- Easily scaled up or scaled down based on requirements

__Disadvantages__
- Security and privacy issues are the major challenges
- Less flexibility and controls compare to public cloud

---
### Types of Cloud service Providers
__Infrastructure as a Service__
- Provider supplies the basic compute, storage and networking infrastructure along with the hypervisor - the virtualization layer.
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
### Introduction to Fog Computing
