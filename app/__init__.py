from flask import Flask, render_template

from app.forms import UserForm
from config import Config


app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def main():
    form = UserForm()
    return render_template('main.html', form=form)


if __name__ == '__main__':
    app.run()
