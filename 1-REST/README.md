# gene_suggest REST-like web service


Provides a single endpoint `gene_suggest` and responds with a list of suggested gene names for the given query and target species.

![image alt >](https://d2.alternativeto.net/dist/icons/flask_27004.png?width=128&height=128&mode=crop&upscale=false)

# How to run?

**Easiest way:**
<img align="right" src="https://amazonwebservices.gallerycdn.vsassets.io/extensions/amazonwebservices/aws-vsts-tools/1.1.8/1541109517627/images/logo.png">

  - It is already running on an [AWS](https://aws.amazon.com/) EC2 machine.
  - Just hit the link http://18.218.244.207:5000/ *(Swagger documentation)*
  - Endpoint is http://18.218.244.207:5000/gene_operations/gene_suggest

&nbsp;

**You can also:**
  <img align="right" src="https://d.martinsefcik.sk/uploads/-/system/group/avatar/7/docker-logo.png">
  
  - Get the docker image `hossam26644/gene_suggest`  create & run your container (Expose port 5000).
  - Run from source code.
 
# Run from source code:
  - Start the virtual environment:
  ```sh
 $ source env/bin/activate
 ```
  - Download dependancies:
  ```sh
 $  pip3 install -r requirements.txt
 ```
   - Start service:
  ```sh
 $  python3 run.py
 ```
 > You may need to run: *apt-get install -y libmysqlclient-dev* , if libmysqlclient is not installed on the system:
 
   - Service starts at http://0.0.0.0:5000/gene_operations/gene_suggest
   - Swagger documentation at http://0.0.0.0:5000/
 # The endpoint accepts the following arguments:
  * **query** - the partial query typed by the user, e.g. `brc` 
    * Default value is an empty string, if the user sends no string.
  * **species** - the name of the target species, e.g. `homo_sapiens`
  * **limit** - the maximum number of suggestions to return, e.g. `10`

 # Technologies used:
 * *flask_restplus* as a microframework.
 * *SQLAlchemy* as an ORM.
 * *Marshmallow* for serialization.
 * *Swagger* for documentation.
 * python *unittest* (coupled with *flask* for api testing)
 * Docker to create a container.
 * Amazon EC2 to run the container.
 
 # Structure:

```
1-REST
│─── README.md
│─── run.py                            # run to start service    
│─── configurations.py                 # holds service configuration for Debugging, testing and deployment
│─── test_file.py                      # Automated testing file,
│─── Dockerfile                       
│─── requirements.txt                  # contains a pinned version of pip3 installations
│
└──────────── main
│             │─── application.py             # main file, initializes and configures application
│             │─── errorlogs.txt              # Error logs by server
│             └───  __init__.py
│
└──────────── apis
│             │───  api.py                # creates the flask api
│             └───  __init__.py
│            
└──────────── namespaces
│             │───  gene_operations.py    # gene_operations namespace (contains the gene_suggest end point)
│             │───  arguments.py          # arguments expected by endoints
│             └───  __init__.py
└──────────── models
│             │───  models.py             # holds the ORM model and Marshmallow model for serialization
│             └───  __init__.py
│
└──────────── env                         # virtual environment
              │
```

> Namespace gene_operations is created, to act as a root to the end point.

> Setting a max limit is proposed to avoid DoS attacks.


# Curl Command Examples 
some curl commands to try the service
  ```sh
 $ curl -X GET "http://18.218.244.207:5000/gene_operations/gene_suggest?query=brc&species=homo_sapiens&limit=10" -H  "accept: application/json"
 ```
  ```sh
 $ curl -X GET "http://18.218.244.207:5000/gene_operations/gene_suggest?query=hnf&species=ailuropoda_melanoleuca&limit=5" -H  "accept: application/json"
 ```
&nbsp;

# test_file.py:
  - Simple API testing file with 2 test cases driven from service specifications.
  - Checks that endpoint exists from status code.
  - Checks that results:
    - Are in order.
    - Have fewer number than limit.
    - Returned with status code 200 (OK)

To run test_file.py:
  - Start the virtual environment and install requirments as in the run step.
  - run the test file:
  
  ```sh
 $  python3 test_file.py
 ```



