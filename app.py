from flask import Flask, render_template, request
import xmlrpclib

app = Flask(__name__)

# Enter your server URL below
server_url = 'http://192.168.0.106:8000/';
server = xmlrpclib.Server(server_url);

# Main logic tree for controller
@app.route("/secreturl", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        if request.form['submit'] == 'Left':
            result = server.set_motores(1, "Mant")
        elif request.form['submit'] == 'Right':
            result = server.set_motores(3, "Mant")
        elif request.form['submit'] == 'Down':
            result = server.set_motores(12, "Mant")
        elif request.form['submit'] == 'Up':
            result = server.set_motores(4, "Mant")
        elif request.form['submit'] == 'Stop':
            result = server.set_motores(0, "Mant")
        elif request.form['submit'] == 'MANUAL':
            result = server.set_motores(16,"Mant")
        elif request.form['submit'] == 'AUTOMATICO':
            result = server.set_motores(16,"Mant")
        elif request.form['submit'] == 'Zorrino_ON':
            result = server.set_motores(64,"Mant")
        elif request.form['submit'] == 'Laser_ON':
            result = server.set_motores(128,"Mant")
        elif request.form['submit'] == 'Limpiador_ON':
            result = server.set_motores(32,"Mant")
        elif request.form['submit'] == 'Salidas_OFF':
            result = server.set_motores(0,"Mant")
    return render_template('control-interface.html')  

# Run the web app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8001)
