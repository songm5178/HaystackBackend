'''
Created on Feb 8, 2015

@author: songm
'''
import endpoints
import protorpc
from models import DbEvent, DbComment

@endpoints.api(name="haystack", version="v1", description="Haystack Api")
class HaystackApi(protorpc.remote.Service):
    
    @DbEvent.method(name="dbevent.insert", path="haystack/dbevent/insert", http_method="POST")
    def dbevent_insert(self, request):
        if request.from_datastore:
            my_quote = request
        else:
            my_quote = DbEvent(title=request.title, address=request.address, from_date_time=request.from_date_time, to_date_time=request.to_date_time, category=request.category)
        my_quote.put()
        return my_quote
    
    @DbEvent.query_method(name="dbevent.list", path="haystack/dbevent/list", http_method="GET", query_fields=("limit", "order", "pageToken"))
    def dbevent_list(self, query):
        return query
    
    @DbEvent.method(name="dbevent.delete", path="haystack/dbevent/{entityKey}", http_method="DELETE",
                       request_fields=("entityKey",))
    def dbevent_delete(self, request):
        if not request.from_datastore:
            raise endpoints.NotFoundException("Key not in datastore")
        else:
            request.key.delete()
        return DbEvent(quote="deleted")
    
    @DbComment.method(name="dbcomment.insert", path="haystack/dbcomment/insert", http_method="POST")
    def dbcomment_insert(self, request):
        if request.from_datastore:
            my_quote = request
        else:
            my_quote = DbComment(event_id=request.event_id, comment=request.comment)
        my_quote.put()
        return my_quote

    @DbComment.query_method(query_fields=("order", "limit", "pageToken"), name="dbcomment.list", path="haystack/dbcomment/insert", http_method="GET")
    def dbcomment_list(self, query):
        return query
    
    @DbComment.method(name="dbcomment.delete", path="haystack/dbcomment/delete/{entityKey}", http_method="DELETE",
                       request_fields=("entityKey",))
    def dbcomment_delete(self, request):
        if not request.from_datastore:
            raise endpoints.NotFoundException("Key not in datastore")
        else:
            request.key.delete()
        return DbComment(quote="deleted")    
    
app = endpoints.api_server([HaystackApi], restricted=False)