from flask import Flask, g, render_template, redirect, url_for
import yaml

app = Flask(__name__)

@app.before_request
def load_data():
    with open('users.yaml', 'r') as file:
        g.data = yaml.safe_load(file)
    g.count = count()

@app.template_filter('others_lined')
def others_lined(others):
    links = [f'<a href="{url_for("user", name=other)}">{other.capitalize()}</a>'
             for other in others]
    return ' | '.join(links)

@app.route('/users')
def users():
    names = [user for user in g.data.keys()]
    return render_template('users.html', names=names, count=g.count)

@app.route('/<name>')
def user(name):
    data = g.data[name]
    others = [user for user in g.data.keys()]
    others.remove(name)
    return render_template('user.html',
                           name=name,
                           data=data,
                           others=others,
                           count=g.count)

@app.errorhandler(404)
def page_not_found(error):
    return redirect('/users')

def count():
    return {'users': len(g.data),
            'interests': sum([len(g.data[user]['interests']) for user in g.data])}

if __name__ == "__main__":
    app.run(debug=True, port=5003)