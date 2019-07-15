import os

from flask import Flask, render_template, request


app = Flask(__name__)

blogs = {
    'name': 'Todays blog',
    'posts': {
        1: {'id': 1,
            'title': 'my first blog',
            'content': 'yo this is a blog'
            },
        2: {'id': 2,
            'title': 'my second blog',
            'content': 'im getting good at this '
            },
        3: {'id': 3,
            'title': 'my thrid blog',
            'content': 'awesome i can count to three go me'
            },
    }
}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/blog/<int:post_id>')
def blog(post_id):
    post = blogs['posts'][post_id]

    return render_template('blogs.html', heading=post['title'], content=post['content'])


app.run(host=os.getenv('HOST'), port=os.getenv('PORT'), debug=True)
