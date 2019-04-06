# How scalability is ensured:
  <img align="right" src="https://drive.google.com/file/d/1YA9PbRDCdLvf_9UWw3RBzrA3Ui9Y71vm/view?usp=sharing">


## 1. containerization:
  <img align="right" src="https://d.martinsefcik.sk/uploads/-/system/group/avatar/7/docker-logo.png">

 - Ensures the apility to run identical copies of the service accross multible servers (horizontal scalability)
 - Makes deployment on servers easier.
## 2. Stick to the  RESTful system architectural constraints, especially:
<img align="right" src="https://jojozhuang.github.io/public/images/restfulapi.png">

 - ##### Ensure that the service is not the first layer user accesses:
   - Use **layers**, including a loadbalancer to distribute traffic amoung servers.
   - Layering also ensures the appility to smothely upgrade the system without stopping the service.

  - ##### A **shared cash** amoung servers running the same service may increase system effeciency.
  - ##### Separation of concerns (Client–server architecture): 
    - The service should be separated from UI concerns.
    
  - #### Statelessness:
    - Each request should include all data needed by the service.
    - This makes any server running the same service able to serve requests from any user.

## 3. Divide the large services to small microservices
 - Each service should be small and independent, allowing scalling individual services based on demand.
## 4. Automate the whole process, including deployment
 - Automating the devOps removes the pain of managment a large number of services, and stops manual errors.
 - Jenkins can be used to automate application building, testing and containerization. 
 - Ansible can be used to automate application deployment, this includes deployment across multible differenr servers.
 - Automated scaling ensures on the run scaling of services.
 - Kubernetes for automated scaling and managment of the services.
 &nbsp;
# So how gene_suggest service would be deployed (a suggested workflow):
 - Code uploaded to a repository (Jira, Github, .. )
 - Jenkins run testing.
 - Jesnkins containerize application, then calls ansible plugin.
 - Ansible configures the server and deploy application.
 - Server may be managed by Kubernetes to ensure automated managment and scalability.


