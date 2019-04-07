# Testing

## Model-based testing strategy is employed in testing the service as:
  - Specifications about expected user input and service response are availble.
  - Other information as the whole strategy of the system or the standards to follow are unavailbe.

### In model-based testing the system (gene_suggest service) is treated as a black box, where specific input is expect and a defined response from the system exists.
  - In this case the input to the model is the arguments expected by the service.
  - The specified response by the service is the model ouput.
  - Both criteria are used to design test cases in a Model-based testing strategy.

#### Different testing layers should be implemented during the development cycle, in this scenario unit testing and integrative testing are considered, other testing layers should be implemented regarding the system as a whole.

#### 1. Unit testing:
  - The nature of a REST-like service indicates that it should have one concern, preciese and small, unit testing should apply to the small building units of the application. 
    - The class that performs the database query is a good example of a unit to be tested in the gene_suggest case.
    - Python unittest can be used to perform the automated testing.
    - API response testing in a confiened environment can also be considered.

#### 2. Integration testing:
  - although unit testing verifies that application components behaves in the targeted way, it is insuffecient at predicting its behaviour when communticating with each other and with other system components outside the confined environment of unit testing.
  - Testing service responce header, body and status code is an example.
    - Testing response code (Implemented)
    - Body can be tested in this case by:
      - Testing that response suggested gene names are in order.
      - Testing that response suggested gene names includes the query.
      - Testing that response suggested gene names number is smaller than the limit.
      - Testing that response suggested gene names belong to the specified species.


### How testing would be automated.
  - API automated testing has many tool as: postman, REST Assured, and more, flask integrated with python unittest can provide automated API testing (Used in gene_suggest test file).
  - Automated testting should be an integrated part of the development workflow, in the propsed workflow in part 2 (Deployment), automated test scripts are run by Jenkings directly after code is commited.
  - Another testing layer should be application validation prior to deployment, this could be done by Ansible.
  
### Some points worth mentioning 
  - Testing automation does not eliminate manual testing.
  - Testing automation should be a continous process that does not stop by deployment.
  - Choosing a testing strategy as a bottom up, top down or big bang depends on the whole system and its surrounding environment:
    - ex: if major flaws are expected in the system a top down approach is a more effecient approach.
  




