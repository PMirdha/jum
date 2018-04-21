from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "hello - brooo1"

@app.route("/hey")
def hey_func():
    return "HEYYYYY - brooo"

@app.route("/upload",methods = ['POST','GET'])
def upload():
	return "upload"

@app.route("/edit_upload",methods = ['PUT','GET'])
def edit_upload():
	return "edit_upload - HAHAHAAH"

@app.route("/delete")
def delete():
	return "delete"

@app.route("/get")
def get_method():
	return "get_method"

if __name__ == "__main__":
	# app.run(debug=True)
    # app.run(host='0.0.0.0', debug=True)
    # app.run(host='0.0.0.0')
    app.run(host='127.0.0.1')


