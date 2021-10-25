# Software Engineering Paradigms and Best Practices

Interpreted Programming Language (usually undergirded by C)  
1. Imperative (structured, procedural (object oriented, event driven, modular))  
2. Declarative (functional, first-oder logic, higher-order logic)  

Compiled Programming Language (usually undergirded by Assembly)
1. Imperative (structured, procedural (object oriented, event driven, modular))
2. Declarative (functional, first-oder logic, higher-order logic)

Statically typed: types known at COMPILE time  
Dynamically typed: types are known at RUN time  
Strongly typed: types are clearly ENFORCED in operations    
Weakly typed: types are language specifically/pragmatically USED in operations  

SOLID  
1. Single-Responsibility: There should never be more than one reason for a class to change
2. Open-Closed: Open for extension but closed for modification
3. Liskov substitution: Functions that use pointers or references to base classes must be able to use objects of derived classes without knowing it  
4. Interfgace-Segregation: Many client-specific interfaces are better than one general-purpose interface  
5. Dependency-Inversion: Depend upon abstractions, do not depend on concretions

ACID  
1. Atomicity: Fail entirely or do not fail
2. Consistency: Roll back if not consistent according to preset rules
3. Isolation: Atoms connot conflict with each other
4. Durability: No log is ever lost and can be used to reinstate everything

12 FACTOR
1. One codebase tracked in revision control, many deploys
2. Explicitly declare and isolate dependencies
3. Store config in the environment
4. Treat backing services as attached resources
5. Strictly separate build and run stages
6. Execute the app as one or more stateless processes
7. Export services via port binding
8. Scale out via the process model
9. Maximize robustness with fast startup and graceful shutdown
10. Keep development, staging, and production as similar as possible
11. Treat logs as event streams
12. Run admin/management tasks as one-off processes

WEB APP SPEED
1. Point domain only, and only to load balancer  
2. Cache all slow, frequent and stable queries  
3. Static files HTTP caching for css, js, jpeg, png -> put on AWS S3/ Google Cloud  
4. Solve bottlenecks: Memory, CPU, Network I/O, Disk I/O  
5. Compute heavy logic offline/ Static web app HTML file  
6. Maintain database indexes  
7. CDN over subdomain/ CNAME, zip via gzip/minify  
8. Session data into cookies/ redis, memcached  

WEB APP SECURITY
1. Keep only HTTP (80) SSL (443) ports open  
2. Disable ssh root and passauth (/etc/ssh/sshd_config/, PermitRootLogin no, PasswordAuthentication no)  
3. Manage access via ssh public keys (~/.ssh/authorized_keys)  
4. Never serve off nginx root/ Apache DocumentRoot  
5. Serve user content on entirely different domain  
6. Always use Object Relational Mapper (ORM)  
7. Always use HTML template library (ORM)  
8. Always use CSRF Tokens  
9. Never open redirects  
10. Use crypto library to add unique salt to all user data  
11. Demand strong password input by design
12. Backcheck password input against huge rainbow table  
13. Never identify a user through cookies  

FILES
```console
#!/usr/bin/env setshebang
#
# <set synopsis>
#
# separate methods
# separate classes
# separate exception handling
# separate main

export PATH=$PATH:set_clean_paths
.bash_profile
.bashrc
.profile

chmod +777 permission handling

//self explanatory code
//comment only to improve readability
```
