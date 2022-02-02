from biothings.web.handlers import FrontPageHandler
from biothings.web.handlers import QueryHandler

class FrontPageHandler(FrontPageHandler):

    def get(self):
        self.write("\n RDP API HOMEPAGE")

class CD2HQueryHandler(QueryHandler):
    name = 'cd2h'

    def post(self, src=None):
        self.event['action'] = 'cd2h_post'

    def get(self, src=None):
    
        self.event['action'] = 'cd2h_get'
        self.write(self.event["action"])




EXTRA_HANDLERS = [
    (r"/", FrontPageHandler),
    (r"/es_query_test/(.+)", CD2HQueryHandler),
]