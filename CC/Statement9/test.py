import os
import urllib
import json
import webapp2
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), "index.html")
        context = {}
        self.response.out.write(template.render(path, context))

    def post(self):
        uni_name = self.request.get("uni_name")
        uni_country = self.request.get("uni_country")

        url = "http://universities.hipolabs.com/search?name=" + uni_name + "&country=" + uni_country
        data = urllib.urlopen(url).read()
        universities = json.loads(data)

        template_values = {
            "universities": universities
        }

        path = os.path.join(os.path.dirname(__file__), "result.html")
        self.response.out.write(template.render(path, template_values))


app = webapp2.WSGIApplication([("/", MainPage)], debug=True)
