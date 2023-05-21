import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        for i in range(0,10):
            self.response.write("<h2>5 * {}  =  {}</h2>".format(i+1,5 * (i+1)))

app = webapp2.WSGIApplication([("/",MainPage)],debug=True)