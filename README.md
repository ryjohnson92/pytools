# PyTools
```
                                          __      _
                                        o'')}____//
                                        `_/      )
                                        (_(_/-(_/
```
Useful tools for python 

## Objects

#### ensure_env (class)
Ensures required environment variables are defined.
```
from PyTools.objects import ensure_env

class my_class(ensure_env):
  ENV = [
    "my_required_variable"
  ]

  def __init__(self,*args,**kwargs):
    super(my_class,self).__init__(*args,**kwargs)
```

#### objectizer (class)
assigns attributes of a passed dict object to the instance. 
```
from PyTools.objects import objectizer

class my_class(objectizer):
  REQUIRED_KEYS = [
    "required_attribute1"
  ]

  def __init__(self,*args,**kwargs):
    super(my_class,self).__init__(*args,**kwargs)
    
  
my_instance = my_class({"required_attribute1":"A required value"})
```