'''
Created on Feb 8, 2015

@author: songm
'''
from endpoints_proto_datastore.ndb.model import EndpointsModel
from google.appengine.ext import ndb

class DbEvent(EndpointsModel):
    _message_fields_schema = ("entityKey", "title", "address", "from_date_time", "to_date_time", "category", "description", "comments", "comment_size", "last_touch_date_time")
    title = ndb.StringProperty()
    address = ndb.StringProperty()
    from_date_time = ndb.DateTimeProperty()
    to_date_time = ndb.DateTimeProperty()
    category = ndb.StringProperty()
    description = ndb.StringProperty()
    comments = ndb.StringProperty(repeated=True)
    comment_size = ndb.IntegerProperty()
    last_touch_date_time = ndb.DateTimeProperty(auto_now=True)
    
    def get_comments(self):
        if not self.comments:
            return []
        return self.comments
    
# class DbComment(EndpointsModel):
#     _message_fields_schema = ("entityKey" , "event_id", "comment", "last_touch_date_time")
#     event_id = ndb.StringProperty()
#     comment = ndb.StringProperty()
#     last_touch_date_time = ndb.DateTimeProperty(auto_now=True)
