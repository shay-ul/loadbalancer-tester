from flask import Flask
import socket

app = Flask(__name__)
@app.route('/')
def hello_world():
    return ("<html><head><title>Loadbalancer Tester</title></head><body><h1> Hello from " + socket.gethostname()) + "</h1></body></html>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)