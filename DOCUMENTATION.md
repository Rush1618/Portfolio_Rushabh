# Portfolio_Rushabh Documentation

Welcome! This documentation will help you understand every part of your portfolio website, how it works, and how you can edit it—even if you're new to coding.

---

## Table of Contents
1. [Project Structure](#project-structure)
2. [How the Website Works](#how-the-website-works)
3. [Editing Your Info](#editing-your-info)
4. [Projects & Achievements](#projects--achievements)
5. [Blog Posts](#blog-posts)
6. [Contact Form](#contact-form)
7. [Dark/Light Mode](#darklight-mode)
8. [Customizing Styles](#customizing-styles)
9. [Adding/Editing Content](#addingediting-content)
10. [How to Deploy](#how-to-deploy)
11. [File-by-File Explanation](#file-by-file-explanation)
12. [FAQ](#faq)

---

## 1. Project Structure

```
Portfolio_Rushabh/
├── app.py                # Main Flask app (runs the website)
├── data.py               # Your info, projects, achievements, contact
├── requirements.txt      # Python dependencies
├── Procfile              # For deployment (Render/Heroku)
├── README.md             # Project overview
├── DOCUMENTATION.md      # This file!
├── static/               # Images, CSS, JS, favicon
│   ├── css/style.css     # Main styles
│   └── images/           # Your profile pic, etc.
├── templates/            # HTML templates
│   ├── index.html        # Main page
│   ├── 404.html          # Custom 404 page
│   └── ...
├── blog/                 # Blog posts (Markdown files)
└── messages.db           # SQLite database for contact messages
```

---

## 2. How the Website Works
- **Flask** runs the website. When someone visits, Flask loads your info from `data.py` and blog posts from `blog/`.
- **HTML templates** (in `templates/`) control how the site looks.
- **CSS** (in `static/css/style.css`) controls colors, fonts, and layout.
- **JavaScript** adds interactivity (sliders, theme toggle, modals).

---

## 3. File & Directory Structure

Let's look at what's inside your project folder.  
Think of your project like a house: each file and folder is a room or tool that helps your website work!

### Top-Level Overview

```
Portfolio_Rushabh/
├── app.py
├── data.py
├── requirements.txt
├── Procfile
├── README.md
├── DOCUMENTATION.md
├── static/
├── templates/
├── blog/
└── messages.db
```

---

### What does each file/folder do?

#### 1. `app.py`  
**This is "the brain" of your website.**  
It's a Python file that tells Flask how to build your site, what to show on each page, and how to handle things like the contact form.

#### 2. `data.py`  
**This is your "profile and content" file.**  
It stores your name, role, tagline, bio, projects, achievements, and contact info.  
If you want to change what's on your site, you'll edit this file a lot!

#### 3. `requirements.txt`  
**This is your "shopping list" for Python.**  
It lists all the Python packages your website needs to run.  
When you run `pip install -r requirements.txt`, Python installs everything on this list.

#### 4. `Procfile`  
**This is a "recipe" for deployment.**  
It tells platforms like Render or Heroku how to start your website.  
Usually, it just says:  
```
web: gunicorn app:app
```
which means "run the app using gunicorn."

#### 5. `README.md`  
**This is your "welcome sign."**  
It explains what your project is, how to use it, and how to set it up.  
People see this first on GitHub.

#### 6. `DOCUMENTATION.md`  
**This is the "big instruction manual."**  
It's what you're reading now! It explains every part of your project in detail.

#### 7. `static/`  
**This is your "closet" for things like images, CSS, and JavaScript.**  
- `static/css/style.css`: All the styles for your website (colors, fonts, layout).
- `static/images/`: Your profile picture and any other images.
- `static/favicon.ico`: The little icon in the browser tab.

#### 8. `templates/`  
**This is your "blueprint folder."**  
It holds all the HTML templates (the structure of your web pages).
- `index.html`: The main page of your site.
- `404.html`: The custom "Page Not Found" error page.
- `blog.html`, `blog_post.html`: Templates for your blog section.

#### 9. `blog/`  
**This is your "blog post library."**  
Each file here is a blog post, written in Markdown (a simple way to format text).

#### 10. `messages.db`  
**This is your "mailbox."**  
It's a SQLite database file where contact form messages are stored.

---

### Visual Map

Here's a simple diagram to help you see how everything connects:

```
[User] --> [Flask (app.py)] --> [HTML Templates] --> [Browser]
         |                |
         |                +--> [data.py] (your info)
         |                +--> [blog/] (your posts)
         |                +--> [messages.db] (contact messages)
         +--> [static/] (CSS, images, JS)
```

---

### What happens when someone visits your site?

1. Flask (app.py) runs and loads your info from `data.py`.
2. It finds the right HTML template in `templates/`.
3. It fills in your info, projects, achievements, etc.
4. The browser loads the page, using styles from `static/css/style.css` and images from `static/images/`.
5. If someone submits the contact form, their message is saved in `messages.db`.

---

**Next up:**  
- Line-by-line code explanations for `app.py` and `data.py`  
- How to edit and customize every part

---

[Continue to Part 3 → Line-by-Line Code Explanations]

---

## 4. Projects & Achievements
- **Projects:**
  - In `data.py`, edit the `PROJECTS` list. Each project is a dictionary with `title`, `description`, `tech`, `github`, and `demo`.
- **Achievements:**
  - In `data.py`, edit the `ACHIEVEMENTS` list. Each achievement is a dictionary with `title` and `details`.
- To add more, copy an existing entry and change the details.

---

## 5. Blog Posts
- Go to the `blog/` folder.
- Create a new file like `my-first-post.md`.
- At the top, add:
  ```
  title: "My First Blog Post"
  date: 2024-06-20
  published: true
  summary: "A short summary of my post."
  featured_image: "images/myimage.jpg"  # (optional)
  ```
- Write your post in Markdown below the front matter.
- Save the file. It will appear in your blog section!

---

## 6. Contact Form
- The contact form is on the main page.
- When someone submits, their message is saved in `messages.db` (SQLite database).
- To view messages, open `messages.db` with a tool like [DB Browser for SQLite](https://sqlitebrowser.org/).

---

## 7. Dark/Light Mode
- The floating button on the right toggles between dark and light mode instantly.
- The theme is remembered in your browser.

---

## 8. Customizing Styles
- Open `static/css/style.css`.
- Change colors, fonts, spacing, or add your own styles.
- Use the `[data-theme='light']` and `[data-theme='dark']` selectors for theme-specific styles.

---

## 9. Adding/Editing Content
- **Profile Picture:** Place your image in `static/images/` and update `PROFILE_PIC` in `data.py`.
- **Projects/Achievements:** Edit `data.py`.
- **Blog Posts:** Add Markdown files to `blog/`.
- **Contact Info:** Edit the `CONTACT` dictionary in `data.py`.

---

## 10. How to Deploy
- Push your code to GitHub.
- Deploy on [Render](https://render.com/) or similar.
- Make sure `Procfile` and `gunicorn` are present.
- Set up environment variables if needed.

---

## 11. File-by-File Explanation
- **app.py:** Main Python file. Handles routes, contact form, error pages, and loads your data.
- **data.py:** All your personal info, projects, achievements, and contact info.
- **requirements.txt:** List of Python packages needed.
- **Procfile:** Tells Render/Heroku how to run your app.
- **static/css/style.css:** All the styles for your site.
- **templates/index.html:** Main HTML template for your site.
- **templates/404.html:** Custom 404 error page.
- **blog/:** Folder for your blog posts (Markdown files).
- **messages.db:** SQLite database for contact form messages.

---

## 12. FAQ

**Q: How do I add a new project?**
A: Edit `data.py`, copy a project in the `PROJECTS` list, and change the details.

**Q: How do I change my profile picture?**
A: Place your image in `static/images/` and update `PROFILE_PIC` in `data.py`.

**Q: How do I add a blog post?**
A: Add a Markdown file to `blog/` with the required front matter.

**Q: How do I change colors or fonts?**
A: Edit `static/css/style.css`.

**Q: How do I see contact form messages?**
A: Open `messages.db` with DB Browser for SQLite.

**Q: How do I deploy?**
A: Push to GitHub and connect to Render or your preferred host.

---

If you have any questions, open an issue or contact Rushabh Singh! 