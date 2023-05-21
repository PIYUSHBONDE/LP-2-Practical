import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        i = 10
        while i>0 :
            self.response.write("<h1>Name: Piyush Ramesh Bonde </h1><br><h2> Seat Number: T190058533 </h2><br><h3> Department: IT </h3><br><br>")
            i = i-1

        for i in range(0,5):
            self.response.write("<h1>Name: Piyush Ramesh Bonde </h1><br><h2> Seat Number: T190058533 </h2><br><h3> Department: IT </h3><br><br>")

app = webapp2.WSGIApplication([("/",MainPage)],debug=True)