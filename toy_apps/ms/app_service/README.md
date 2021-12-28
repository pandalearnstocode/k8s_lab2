# Application Service

This is responsible for the following things,

* New project creation
* Delete project
* Any new role creation
* Apply role to a user
* User authentication
* User authorization
* Other project management related stuff

It will have access to:

* project db
* client service
* data service
* ml service
* utils service


```
# Data Lib
python -m pip install -e . && python -c 'import datalib as datalib; print(datalib.datalib.core.useful_function())'
```

## REQUIRED ENV VARIABLES:

* `PROJECT_DATABASE_URL`