from flask import Flask, render_template, session, request, redirect, url_for
from flask_flatpages import FlatPages, pygments_style_defs
import data
import os
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['FLATPAGES_EXTENSION'] = '.md'
app.config['FLATPAGES_ROOT'] = 'blog'
pages = FlatPages(app)

@app.route('/')
def home():
    return render_template('index.html', data=data, pages=pages)

@app.route('/blog/')
def blog():
    posts = [p for p in pages if 'published' in p.meta and p.meta['published']]
    posts.sort(key=lambda p: p.meta.get('date', ''), reverse=True)
    return render_template('blog.html', posts=posts, data=data)

@app.route('/blog/<path:path>/')
def blog_post(path):
    post = pages.get_or_404(path)
    return render_template('blog_post.html', post=post, data=data)

@app.route('/toggle-dark-mode')
def toggle_dark_mode():
    dark = session.get('dark_mode', False)
    session['dark_mode'] = not dark
    return redirect(request.referrer or url_for('home'))

@app.context_processor
def inject_current_year():
    return {'current_year': datetime.now().year}

if __name__ == '__main__':
    app.run(debug=True) 