from flask import Flask, g, render_template, redirect, url_for
import yaml

app = Flask(__name__)

def calculate_statistics():
    return {'users': len(g.data),
            'interests': sum([len(g.data[user]['interests']) for user in g.data])}

@app.before_request
def load_data():
    with open('users.yaml', 'r') as file:
        g.data = yaml.safe_load(file)
    g.count = calculate_statistics()

@app.template_filter('others_lined')
def others_lined(others):
    links = [f'<a href="{url_for("user", name=other)}">{other.capitalize()}</a>'
             for other in others]
    return ' | '.join(links)

@app.route('/')
def home():
    return redirect(url_for('users'))

@app.route('/users')
def users():
    return render_template('users.html', names=g.data.keys(), count=g.count)

@app.route('/<name>')
def user(name):
    try:
        data = g.data[name]
        others = [user for user in g.data.keys() if user != name]
        return render_template('user.html',
                               name=name,
                               data=data,
                               others=others,
                               count=g.count)
    except:
        error_message = 'Sorry, there is no such user. ' \
                        'Try one of the links at the bottom.'
        return render_template('user.html',
                               error_message=error_message,
                               others = g.data.keys(),
                               count=g.count)

@app.errorhandler(404)
def page_not_found(error):
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True, port=5003)