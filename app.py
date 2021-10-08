from flask import Flask, render_template, request
from admin.admin import admin

app = Flask(__name__)
app.register_blueprint(admin, url_prefix="/admin")


@app.route('/')
def index():
    return "Testing Succesful"

if __name__ == '__main__':
	app.run(debug=True)     