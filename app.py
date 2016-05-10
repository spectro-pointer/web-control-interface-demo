from flask import Flask, render_template, request
import xmlrpclib

app = Flask(__name__)

# Enter your server URL below
server_url = 'http://192.168.0.101:8000/';
server = xmlrpclib.Server(server_url);

# Main logic tree for controller
@app.route('/secreturl', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['submit'] == 'Left':
            result = server.set_motores(1, "Busca")
        elif request.form['submit'] == 'Right':
            result = server.set_motores(3, "Busca")
        elif request.form['submit'] == 'Down':
            result = server.set_motores(12, "Busca")
        elif request.form['submit'] == 'Up':
            result = server.set_motores(4, "Busca")
        elif request.form['submit'] == 'Stop':
            result = server.set_motores(0, "Busca")
    return render_template('control-interface.html')  

# Run the web app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
