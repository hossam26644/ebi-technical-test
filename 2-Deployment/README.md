 <img align="right" src="https://raw.githubusercontent.com/hossam26644/ebi-technical-test/master/2-Deployment/images/scalable.png">

# How scalability is ensured:
 
## 1. Containerization:
  <img align="right" src="https://d.martinsefcik.sk/uploads/-/system/group/avatar/7/docker-logo.png">

 - Ensures the ability to run identical copies of the service across multiple servers (horizontal scalability).
 - Deployment on servers requires no code change.
## 2. Stick to the  RESTful system architectural constraints, including:
<img align="right" src="https://raw.githubusercontent.com/hossam26644/ebi-technical-test/master/2-Deployment/images/REST.png">

 - ##### The service is better not to be the first layer user accesses:
   - Use **layers**, including a load-balancer to distribute traffic among servers.
   - Layering also ensures the ability to smoothly upgrade the system without stopping the service.

  - ##### A **shared cache** among servers running the same service may increase system efficiency.
  - ##### Separation of concerns (Client–server architecture):
    - The service should be separated from UI concerns.
    
  - #### Statelessness:
    - Each request should include all data needed by the service.
    - This makes any server running the same service able to serve requests from any user.

## 3. Divide the large services to small microservices
 - Each service should be small and independent, allowing scaling individual services based on demand.

<img align="right" src="https://raw.githubusercontent.com/hossam26644/ebi-technical-test/master/2-Deployment/images/Automation.png">

## 4. Automate the whole process, including deployment

 - Automating the devOps removes the pain of managing a large number of services, and stops manual errors.
 - Automation software can be used to automate application building, testing and containerization, as *Jenkins*.
 - Server configuration and management tools can be used to automate application deployment, this includes deployment across different servers, as *Ansible*
 - Automated scaling ensures on-the-run scaling of services containers.
 - *Kubernetes* can be used to automated scaling and management of the services (Container Orchestration).
 &nbsp;
# So how gene_suggest service would be deployed (a suggested workflow):

 - Code uploaded to a repository (Bitbucket, Github, .. )
 - *Jenkins* runs testing.
 - *Jenkins* containerizes application, then calls *Ansible* plugin.
 - *Ansible* configures the server and deploys application.
 - Servers cluster may be managed by *Kubernetes* to ensure automated services management and scalability.
 
> In this model, *Ansible* can do *Jenkins* role and vise versa (Plugins exist), but the common usage of each was the reference in creating this workflow

<img align="center" src="https://github.com/hossam26644/ebi-technical-test/blob/master/2-Deployment/images/workflow.png">









