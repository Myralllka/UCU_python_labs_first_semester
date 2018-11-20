from http.server import SimpleHTTPRequestHandler, HTTPServer
from json import dumps
from threading import Timer
from webbrowser import open
from icalevents.icalevents import events

FILE = 'main.html'
PORT = 8000


# noinspection PyPep8Naming
class TestHandler(http.server.SimpleHTTPRequestHandler):
    """
    The test example handler.
    """

    def do_POST(self):
        """
        Handle a post request by returning the square of the number.
        """
        print(self.headers)
        print(self.headers.get_all('content-length'))
        print(self.rfile.read(int(self.headers.get_all('content-length')[0])))
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.flush_headers()
        self.wfile.write(build_event_list_json())


def build_event_list_json():
    gc_events = events("https://calendar.google.com/calendar/ical/ucu.edu.ua_gl1e5udah0l84"
                       "uekquhjeqkgm0%40group.calendar.google.com/public/basic.ics")
    event_list = [{'summary': gc_event.__dict__['summary'], 'start': (str(gc_event.__dict__['start']))[:19],
                   'end': (str(gc_event.__dict__['end']))[:19], 'description': gc_event.__dict__['description']} for
                  gc_event in gc_events]
    return dumps(event_list)


def open_browser():
    """
    Start a browser after waiting for half a second.
    """

    def _open():
        open('http://localhost:%s/%s' % (PORT, FILE))

    Timer(0.5, _open).start()


def start_server():
    """
    Start the server.
    """
    HTTPServer(("", PORT), TestHandler).serve_forever()


if __name__ == "__main__":
    open_browser()
    start_server()
