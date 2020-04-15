import os
from flask import Flask, request
import othello.dispatch as dispatch

app = Flask(__name__)

#-----------------------------------
#  The following code is invoked when the path portion of the URL matches 
#         /othello
#
#  Parameters are passed as a URL query:
#        /othello?parm1=value1&parm2=value2
#
@app.route('/othello')
def server():
    try:
        parms = {}
        for key in request.args:
            parms[key] = str(request.args[key])
        result = dispatch._dispatch(parms)
        return str(result)
    except Exception as e:
        return str(e)
    
#-----------------------------------
port = os.getenv('PORT', '5000')
if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = int(port))

