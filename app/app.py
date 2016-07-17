from flask import Flask, session, escape, request
from redis import Redis
from redis_session import RedisSessionInterface


redis = Redis(host='192.168.99.102', port=6379, db=0, password='abc123')


app = Flask(__name__)
app.session_interface = RedisSessionInterface(redis=redis)


@app.route("/", methods=['GET'])
def index():
    if 'username' in session:
        return 'Hello, my friend! '\
                'You\'re logged in as '\
                '<strong>{}</strong>.'.format(escape(session['username']))
    else:
        return 'You\'re not logged in. <a href="/login">Go Login</a>.'


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return 'Greetings, visitor! You are now logged in. '\
               '<a href="/">Go Home</a>.'
    else:
        return """
        <h3>Login</h3>
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>"""
