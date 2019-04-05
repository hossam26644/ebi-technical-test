# gene_suggest REST-like web service


Provides a single endpoint `gene_suggest` and responds with with a list of suggested gene names for the given query and target species


# How to run?

Easiest way:
  - It is already running on an AWS EC2 machine.  
  - Just hit the link http://18.218.244.207:5000/ *(documentation)*
  - Endpoint is http://18.218.244.207:5000/gene-operations/gene-suggest

You can also:
  - Get the docker image `hossam26644/gene_suggest`  and create & run your container.
  - Run from source code.
 
# Run from source code:
  - Start the virtual environment.
  ```sh
 $ source env/bin/activate
 ```
  - Download dependancies.
  ```sh
 $  pip install -r requirements.txt
 ```
   - Start service.
  ```sh
 $  python3 app.py
 ```
   - Service starts at http://0.0.0.0:5000/gene-operations/gene-suggest
   - Swagger documetnation at http://0.0.0.0:5000/
 # The endpoint accepts the following arguments:
  * query - the partial query typed by the user, e.g. `brc` 
  * species - the name of the target species, e.g. `homo_sapiens`
  * limit - the maximum number of suggestions to return, e.g. `10`

 # Project structure:

```
1-REST
│─── README.md
│─── app.py                            # main file, run to start service    
│─── configurations.py                 # holds service configuration for Debugging, testing and deployment
│───  test_file.py                     # Automated testing file,
│───  Dockerfile                        
│───  errorlogs.txt                    # Server writes error logs in this file
│───  requirements.txt                 # contains a pinned version of everything that was installed by pip3
│───  __init__.py
│
└────────────apis
│             │───  api.py             # creates the flask api
│             └───  __init__.py
│            
└────────────end _points
│       │─── gene_operations.py        #The name space gene_operation, holds the endpoint gene_suggest
│       │─── arguments.py
│       └───  __init__.py
│   
└───folder2
    │   file021.txt
    │   file022.txt
```
