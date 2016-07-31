# -*- coding: utf-8 -*-

import webapp2
from webapp2 import RedirectHandler


class Testing(webapp2.RequestHandler):
    """
    /test: test handler
    """
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'

        self.response.out.write('Done')

application = webapp2.WSGIApplication([
    webapp2.Route('/test', Testing),
], debug=_DEBUG)

