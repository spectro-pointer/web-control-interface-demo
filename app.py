from flask import Flask, render_template
import xmlrpclib

app = Flask(__name__)

server_url = 'http://192.168.0.101:8000/';
server = xmlrpclib.Server(server_url);

@app.route('/secreturl')
def index():
    #result = server.set_motores(4, Busca)
    return render_template('control-interface.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
