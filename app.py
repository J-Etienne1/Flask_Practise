
## https://www.youtube.com/watch?v=ZVGwqnjOKjk&list=PL6gx4Cwl9DGDi9F_slcQK7knjtO8TUvUs
"""
from flask import Flask, request

app = Flask(__name__)


#@app.route('/')
#def index():
#   return 'This is the Home Page!'


@app.route('/Stuff')
def Stuff():
    return '<h2>This is the Stuff page with a h2 Header'



@app.route('/profile/<username>')
def profile(username):
    return '<h3>Hey there %s<h3>' % username


@app.route('/post/<int:post_id>')
def post(post_id):
    return '<h3>Post ID is %s<h3>' % post_id



## Tutorial - 3 - HTTP Methods - GET & POST
# need to import request

@app.route('/')
def index():
    return 'Method used: %s' % request.method


@app.route('/things', methods=['GET', 'POST'])
def things():
    if request.method == 'POST':
        return 'You are using POST'
    else:
        return 'You are probably using GET'

# to test POST use Postman



if __name__ == '__main__':
    app.run(debug=True)
"""


## Tutorial - 4 - HTML Templates
## &
## Tutorial - 5 - Static Files
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/Profile/<name>')
def Profile(name):
   return render_template('profile.html', name=name)

if __name__ == '__main__':
    app.run()

"""


## Tutorial - 6 -  Mapping Multiple URLs

"""
from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
@app.route('/<user>')
def index(user=None):
    return render_template('user.html', user=user)


if __name__ == '__main__':
    app.run()
"""



## Tutorial - 7 -  Mapping Multiple URLs




































