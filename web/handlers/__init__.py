from telnetlib import EL
from biothings.web.handlers import FrontPageHandler, BaseQueryHandler, QueryHandler
from biothings.web.query import ESQueryBackend
#from elasticsearch import Elasticsearch
#from elasticsearch_dsl import Search


class FrontPageHandler(FrontPageHandler):

    def get(self):
        self.write("\n RDP API HOMEPAGE")

class CD2HQueryHandler(QueryHandler):
    name = 'cd2h'
    async def get(self, *args, **kwargs):
        user_input=args[0]

        # TESTING OUTPUT 
        self.write({
            "USER INPUT" : user_input, 
            "FORMAT": self.args['format'],
            "BIOTHING TYPE": self.args['biothing_type']
        }
        )
    
    async def post(self, *args, **kwargs):
        self.write(args[0])


EXTRA_HANDLERS = [
    (r"/", FrontPageHandler),
    (r"/cd2h/es_query/(.+)", CD2HQueryHandler,{"biothing_type": "cd2h"}),]