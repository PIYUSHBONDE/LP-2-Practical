import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write("<h1> Fibonaci Series </h1>")
        fibo_series = fibo_calculator(10)
        for i in fibo_series:
            self.response.write("<h2> {} </h2>".format(i))

def fibo_calculator(n):
    num = []
    a = 0
    b = 1
    num.append(a)
    num.append(b)
    for i in range(0,n-2):
        c = a+b
        num.append(c)
        a = b
        b = c
    return num



app = webapp2.WSGIApplication({("/",MainPage)},debug=True)
