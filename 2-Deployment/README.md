 <img align="right" src="https://raw.githubusercontent.com/hossam26644/ebi-technical-test/master/2-Deployment/images/scalable.png">

# How scalability is ensured:
 
## 1. containerization:
  <img align="right" src="https://d.martinsefcik.sk/uploads/-/system/group/avatar/7/docker-logo.png">

 - Ensures the apility to run identical copies of the service accross multible servers (horizontal scalability)
 - Makes deployment on servers easier.
## 2. Stick to the  RESTful system architectural constraints, including:
<img align="right" src="https://raw.githubusercontent.com/hossam26644/ebi-technical-test/master/2-Deployment/images/REST.png">

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

<img align="right" src="https://raw.githubusercontent.com/hossam26644/ebi-technical-test/master/2-Deployment/images/Automation.png">

## 4. Automate the whole process, including deployment

 - Automating the devOps removes the pain of managment a large number of services, and stops manual errors.
 - *Jenkins* can be used to automate application building, testing and containerization. 
 - *Ansible* can be used to automate application deployment, this includes deployment across multible different servers.
 - Automated scaling ensures on the run scaling of services.
 - *Kubernetes* for automated scaling and managment of the services.
 &nbsp;
# So how gene_suggest service would be deployed (a suggested workflow):

 - Code uploaded to a repository (Bitbucket, Github, .. )
 - *Jenkins* run testing.
 - *Jenkins* containerize application, then calls *Ansible* plugin.
 - *Ansible* configures the server and deploy application.
 - Servers cluster may be managed by *Kubernetes* to ensure automated services managment and scalability.

<img align="center" src="https://github.com/hossam26644/ebi-technical-test/blob/master/2-Deployment/images/workflow.png">



