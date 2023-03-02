from flask import  Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login_app', methods=['POST'])
def login_app():
    id = request.form['id']
    pwd = request.form['pwd']
    return id+':'+pwd

@app.route('/address')
def address():
    return render_template('address.html')

@app.route('/address_app', methods=['POST'])
def address_app():
    address = request.form['address']
    return address

@app.route('/select')
def select():
    return render_template('/select.html')

@app.route('/select_app', methods=['POST'])
def select_app():
    favorite = request.form['favorite']
    return favorite

if __name__=='__main__':
    app.run(debug=True)

