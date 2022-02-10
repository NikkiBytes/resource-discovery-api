from telnetlib import EL
from biothings.web.handlers import FrontPageHandler, BaseQueryHandler, QueryHandler
from biothings.web.query import ESQueryBuilder, AsyncESQueryPipeline
#from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search


class FrontPageHandler(FrontPageHandler):

    def get(self):
        self.write("\n RDP API HOMEPAGE")

class CD2HQueryBuilder(ESQueryBuilder):
    def build(self, q, **options):
        return super().build(q, **options)

class CD2HQueryPipeline(AsyncESQueryPipeline):
    """
    Custom API Pipeline
    """

    async def fetch(self, id, **options):
        if id == "es_query":
            display = {"_testing": "ES pipeline"}
            display.update(await super(),fetch("?", **options))
            return display

        display = super().fetch(id, **options)
        return display

#class CD2HQueryHandler(QueryHandler):
 #   name = 'cd2h'

    #async def get(self, *args, **kwargs):
        #user_input=args[0]
        #search = Search.query("query_string", user_input)

        #return await super().get(search, options)

    #async def post(self, *args, **kwargs):

        
        # TESTING OUTPUT 
        #self.write({
         #   "USER INPUT" : user_input, 
          #  "FORMAT": self.args['format'],
           # "BIOTHING TYPE": self.args['biothing_type']
        #}
        #)



EXTRA_HANDLERS = [
    (r"/", FrontPageHandler),]
    #, {"biothing_type": "cd2h"}),]