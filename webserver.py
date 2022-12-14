import cgi
from http.server import HTTPServer, BaseHTTPRequestHandler
import Calc as calc

def createHTMLpage(value,result):
    if result is not None:
        htmlFile = '''<!DOCTYPE html>
<html>
<style>
    input[type="text"] {
        color: rgb(123, 123, 123);
        width: 90%;
        height: 30px;
        font-size: 18px;
    }
    input[type="submit"] {
        color: rgb(255, 0, 0);
        background-color: rgb(210, 210, 210);
        width: 20%;
        height: 20px;
    }
    input[type="submit"]:hover {
        color: rgb(223, 19, 19);
        background-color: rgb(174, 174, 174);
        width: 20%;
        height: 20px;
    }
</style>

<body>
    <h2>SWENG Calculator</h2>
    <form method="POST">
        <label for="calculation">Input to Calculate:</label><br><br>
        <input type="text" id="calculation" name="calculation"><br><br>
        <input type="submit" value="Calculate">
    </form>
    <p>Use log(x) to calculate the natual log and exp(x) to calculate e^x.</p><br>
    <h3>Previous Calculation:  '''+str(value)+'''</h3>
    <h3>Result:  '''+str(result)+'''</h3>
</body>

</html>'''
    else:
        htmlFile = '''<!DOCTYPE html>
<html>
<style>
    input[type="text"] {
        color: rgb(123, 123, 123);
        width: 90%;
        height: 30px;
        font-size: 18px;
    }
    input[type="submit"] {
        color: rgb(255, 0, 0);
        background-color: rgb(210, 210, 210);
        width: 20%;
        height: 20px;
    }
    input[type="submit"]:hover {
        color: rgb(223, 19, 19);
        background-color: rgb(174, 174, 174);
        width: 20%;
        height: 20px;
    }
</style>

<body>
    <h2>SWENG Calculator</h2>
    <form method="POST">
        <label for="calculation">Input to Calculate:</label><br><br>
        <input type="text" id="calculation" name="calculation"><br><br>
        <input type="submit" value="Calculate">
    </form>
    <p>Use log(x) to calculate the natual log and exp(x) to calculate e^x.</p>
</body>

</html>'''
    return htmlFile

# This class is used to handle the GET and POST requests to the webpage
class webserver(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        content = createHTMLpage(None,None)
        self.wfile.write(content.encode())

    def do_POST(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST'}
        )
        value = form.getvalue('calculation')
        result = calc.calculate(value)
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        content = createHTMLpage(value,result)
        self.wfile.write(content.encode())

def main():
    PORT = 8080
    server = HTTPServer(('', PORT), webserver)
    print("Server running on localhost:%s" % PORT)
    server.serve_forever()


if __name__ == '__main__':
    main()
