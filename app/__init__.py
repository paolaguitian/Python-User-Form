from flask import Flask, render_template, redirect
import psycopg2
from app.forms import UserForm
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
app._static_folder = '../../static'


conn = psycopg2.connect(
    dbname='mypythonsqlform',
    user='aexrymzsrdvfog',
    password='14620d5976258515291254cc72b196565f137bbd6ac75fd21f6bac4fe15db3a1',
    host='ec2-34-235-108-68.compute-1.amazonaws.com',
    port=5432
)
cursor = conn.cursor()
cursor.execute("CREATE TABLE user(id serial PRIMARY KEY, firstNname varchar, lastName varchar, email varchar, age integer )")


@app.route('/', methods=['GET', 'POST'])
def main():
    form = UserForm()
    if form.validate_on_submit():
        cursor.execute("INSERT INTO user")
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/allUsers')
    return render_template('main.html', form=form)


@app.route('/allUsers')
def getall():
    cursor.execute("SELECT * FROM user")
    items = cursor.fetchAll()
    print(items)


if __name__ == '__main__':
    app.run()
