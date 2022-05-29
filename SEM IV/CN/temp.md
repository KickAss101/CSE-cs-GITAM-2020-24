##### DNS Records
- __["A" Record](https://dnsmadeeasy.com/post/what-is-an-a-record) and AAAA__
	- An A record stores IPv4 address for a domain name
	- The AAAA record stores IPv6 address for a domain name
- __Canonical Name (CNAME)__
	- Canonical name is an alternative record or alias that maps one domain name to another.
	- Oftentimes, when sites have subdomains such as blog.example.com or shop.example.com, those subdomains will have CNAME records that point to a root domain (example.com). This way if the IP address of the host changes, only the DNS "A" record for the root domain needs to be updated and all the CNAME records will follow along with whatever changes are made to the root.

![300](627d639cbbc41b8058488033_A_RECORD_DNS_EXAMPLE.png)
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