from flask import Flask, render_template, request
import xmlrpclib

app = Flask(__name__)

server_url = 'http://192.168.0.101:8000/';
server = xmlrpclib.Server(server_url);

@app.route('/secreturl', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['submit'] == 'Do Something':
            result = server.set_motores(4, "Busca")
            return render_template('control-interface.html')
            pass # do something
        elif request.form['submit'] == 'Do Something Else':
            result = server.set_motores(0, "Busca")
            return render_template('control-interface.html')
            pass # do something else
        else:
            pass # unknown
    elif request.method == 'GET':
    #result = server.set_motores(4, Busca)
        return render_template('control-interface.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
