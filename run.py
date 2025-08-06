from flask import Flask, render_template, request, redirect
# from flask_socketio import SocketIO

app = Flask(__name__)
# socketio = SocketIO(app)

@app.route('/')
def index():
   return render_template('index.html')

#---------------------------------------------------------------

@app.route('/comojogar')
def comojogar():
   return render_template('comojogar.html')

#----------------------------------------------------------------

@app.route('/cartas')
def cartas():
   return render_template('cartas.html')

#----------------------------------------------------------------

@app.route('/jogar')
def jogar():
   return render_template('jogar.html')

# if __name__ == '__main__':
   # socketio.run(app, host='192.168.0.100', port=80, debug=True)
app.run(host='10.144.227.179', port=80, debug=True)