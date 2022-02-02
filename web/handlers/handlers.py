from biothings.web.handlers.query import BaseAPIHandler

class EchoHandler(BaseAPIHandler):

    def get(self, text):
        self.write({
            "status": "ok",
            "result": text
        })