from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    layout = '''
    <html>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol>
                <li><a href="/read/1">html</a></li>
                <li><a href="/read/2">css</a></li>
            </ol>
            <h2>Welcome</h2>
            Hello, WEB
        </body>
    </html>
    '''
    return layout
