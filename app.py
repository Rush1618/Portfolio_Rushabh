from flask import Flask, render_template, session, request, redirect, url_for, flash
from flask_flatpages import FlatPages
import os
from datetime import datetime
import sqlite3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
from werkzeug.utils import secure_filename
from flask_mail import Mail, Message
import uuid
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['FLATPAGES_EXTENSION'] = '.md'
app.config['FLATPAGES_ROOT'] = 'blog'
pages = FlatPages(app)

# --- SQLite setup for contact messages ---
DB_PATH = 'messages.db'
def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )''')
        conn.commit()
init_db()

TESTIMONIALS_PATH = 'testimonials.json'
UPLOAD_FOLDER = 'static/images/testimonials/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Email config (set these as environment variables in production)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'projectsmailsender0@gmail.com'
app.config['MAIL_PASSWORD'] = 'pilc rutc sqbm aaka'
app.config['MAIL_DEFAULT_SENDER'] = 'projectsmailsender0@gmail.com'
mail = Mail(app)

ADMIN_EMAIL = 'portfoliorushabh@gmail.com'  # CHANGE THIS

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def load_testimonials():
    if os.path.exists(TESTIMONIALS_PATH):
        with open(TESTIMONIALS_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_testimonials(testimonials):
    with open(TESTIMONIALS_PATH, 'w', encoding='utf-8') as f:
        json.dump(testimonials, f, ensure_ascii=False, indent=2)

# Utility functions for pending testimonials
PENDING_PATH = 'pending_testimonials.json'
def load_pending_testimonials():
    if os.path.exists(PENDING_PATH):
        with open(PENDING_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []
def save_pending_testimonials(pending):
    with open(PENDING_PATH, 'w', encoding='utf-8') as f:
        json.dump(pending, f, indent=2)

RENDER_BASE_URL = "https://portfolio-rushabh.onrender.com"

@app.route('/')
def home():
    testimonials = [t for t in load_testimonials() if not t.get('pending', False)]
    return render_template('index.html', data=data, pages=pages, testimonials=testimonials)

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

@app.route('/contact', methods=['POST'])
def contact_submit():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    if name and email and message:
        with sqlite3.connect(DB_PATH) as conn:
            c = conn.cursor()
            c.execute('INSERT INTO messages (name, email, message) VALUES (?, ?, ?)', (name, email, message))
            conn.commit()
        # Send email notification
        try:
            sender_email = "projectsmailsender0@gmail.com"
            sender_password = "fengveihgrbueuvm"  # App password, no spaces
            receiver_email = "portfoliorushabh@gmail.com"
            subject = f"New Portfolio Message from {name}"
            body = f"Name: {name}\nEmail: {email}\nMessage:\n{message}"
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, receiver_email, msg.as_string())
        except Exception as e:
            print(f"Message send failed: {e}")
        flash('Thank you! Your message has been received.', 'success')
    else:
        flash('Please fill in all fields.', 'danger')
    return redirect(url_for('home') + '#contact')

# When a testimonial is submitted, mark as pending and send approval email
@app.route('/testimonials/add', methods=['GET', 'POST'])
def add_testimonial():
    if request.method == 'POST':
        text = request.form.get('text')
        email = request.form.get('email')
        file = request.files.get('image')
        author = request.form.get('author')
        image_url = ''
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            image_url = filepath.replace('static/', '')
        testimonial = {
            'id': str(uuid.uuid4()),
            'text': text,
            'author': author,
            'email': email,
            'image': image_url,
            'pending': True
        }
        # Save to pending testimonials
        pending = load_pending_testimonials()
        pending.append(testimonial)
        save_pending_testimonials(pending)
        # Send approval email
        approve_url = f"{RENDER_BASE_URL}{url_for('approve_testimonial', id=testimonial['id'])}"
        reject_url = f"{RENDER_BASE_URL}{url_for('reject_testimonial', id=testimonial['id'])}"
        msg = Message('New Testimonial Pending Approval', recipients=[ADMIN_EMAIL])
        msg.body = f"""
New testimonial submitted:

Author: {testimonial['author']}
Email: {testimonial['email']}
Text: {testimonial['text']}

Approve: {approve_url}
Reject: {reject_url}
"""
        mail.send(msg)
        flash('Testimonial submitted and pending approval!', 'info')
        return redirect(url_for('home'))
    return render_template('add_testimonial.html', data=data)

# Admin approval routes
@app.route('/testimonials/approve/<id>')
def approve_testimonial(id):
    pending = load_pending_testimonials()
    approved = load_testimonials()
    for t in pending:
        if t['id'] == id:
            t['pending'] = False
            approved.append(t)
            save_testimonials(approved)
            pending = [x for x in pending if x['id'] != id]
            save_pending_testimonials(pending)
            flash('Testimonial approved!', 'success')
            break
    return redirect(url_for('home'))

@app.route('/testimonials/reject/<id>')
def reject_testimonial(id):
    pending = load_pending_testimonials()
    pending = [x for x in pending if x['id'] != id]
    save_pending_testimonials(pending)
    flash('Testimonial rejected.', 'warning')
    return redirect(url_for('home'))

@app.route('/testimonials')
def testimonials():
    testimonials = load_testimonials()
    return render_template('testimonials.html', testimonials=testimonials, data=data)

@app.context_processor
def inject_current_year():
    return {'current_year': datetime.now().year}

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True) 