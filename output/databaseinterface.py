
from typing import List, Any, Union, Dict, Optional, Tuple
from output._types import *
        
class DatabaseInterface(object):
    """DatabaseInterface is 
    This is the interface to the database of the wiz_app system (the resourcemanager). 

To get started import the database and the valid modes of the database from the business rules.

```python
from wiz_app_connector.infrastructure.db.wiz_app_db import DatabaseInterface
from wiz_app_connector.domain.business_rules import ValidDatabaseMode
# setup a database with a development mode
db = DatabaseInterface("v1",ValidDatabaseMode.DEV)

# send a post request
db.use_url(endpoint="sensor").create(body={})
    
    
    Example
    -------
    
    ```python
    databaseinterface = DatabaseInterface()
    
    databaseinterface.create(body)
                
    databaseinterface.read(name)
                
    databaseinterface.update(name)
                
    databaseinterface.delete(name)
                
    ```        
        
    """
    
    def __init__(self, version : str, mode : int) -> None:
        # This will set what version of the database routes to send the request to, i.e v1 will set /v1/endpoint 
        self.version = version
        # This can be DEV which is for running the database locally (on development mode) this will send the requests to localhost:8000
        self.mode = mode
    
    def create(self, body : dict) -> dict:
        """create sends a post request
        
        Parameters
        ----------
            
        body : dict
            the body of the requests
        
        Returns
        -------
        dict
            returns a dictionary with the response of the request
        """
        ...
                          
    
    def read(self, name : str) -> dict:
        """read sends a get requests.
        
        Parameters
        ----------
            
        name : str
            the 
        
        Returns
        -------
        dict
            a dictionary containing the response of the request
        """
        ...
                          
    
    def update(self, name : str) -> dict:
        """update send a put request.
        
        Parameters
        ----------
            
        name : str
            parameter comment
        
        Returns
        -------
        dict
            a dictionary containing the response of the request
        """
        ...
                          
    
    def delete(self, name : str) -> dict:
        """delete sends a delete request.
        
        Parameters
        ----------
            
        name : str
            parameter comment
        
        Returns
        -------
        dict
            a dictionary containing the response of the request
        """
        ...
                          