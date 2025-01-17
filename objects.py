import os

class ensure_env:
    def __init__(self,*args,**kwargs):
        assert hasattr(self,'ENV'), 'self.ENV [] needs to be populated in order to ensure.'
        super(ensure_env,self).__init__(*args,**kwargs)

class objectizer:
    def __init__(self,result:dict,*args,**kwargs):
        self.__object_name__ = type(self).__name__
        assert type(result) == dict, 'Dict is required for {}ized results'.format(self.__object_name__)
        assert hasattr(self,'REQUIRED_KEYS'),'REQUIRED_KEYS [] is required for subclasses'      

        for key in self.REQUIRED_KEYS:
            assert key in result, 'Required key missing from result == {}'.format(key)
        for attr in result:
            if not hasattr(self,attr):
                setattr(self,attr,result[attr])
        super(objectizer,self).__init__(*args,**kwargs)