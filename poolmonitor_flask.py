import poolprobe
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hi():
    return "<h2>The current pool temperature is: " + str("%.1f" % poolprobe.read_temp()) + " *F</h2><br><br><small>it has been 35 days since @edsw said 'im a bad friend and erik doesnt deserve aws'"

@app.route('/data')
def data():
    return "<pre>" + str(poolprobe.read_temp()) + "</pre>"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
