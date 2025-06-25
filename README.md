# 🚀 Rushabh Singh Portfolio

![Portfolio Banner](static/images/profile.jpg)

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Build](https://img.shields.io/badge/build-passing-brightgreen)
![Visitors](https://visitor-badge.laobi.icu/badge?page_id=Rush1618.Portfolio_Rushabh)

---

## ✨ Features
- 🏠 Home, About, Projects, Achievements, Blog, Contact sections
- 📱 Responsive design with animated gradient and glassmorphism
- 🟩 GitHub contributions calendar and live commit stats (adaptive to theme)
- 📝 Blog with Markdown support (Flask-FlatPages)
- 🌗 Animated theme toggle switch (sun/moon, clouds/stars, fully responsive and accessible)
- 🎠 Project and achievement carousels with details modal
- 🚫 Custom 404 page
- 📬 Contact form (stores messages in SQLite)
- 🛠️ Easy customization via `data.py`

---

## 🛠️ Setup
1. **Clone the repo**
   ```bash
   git clone https://github.com/Rush1618/Portfolio_Rushabh.git
   cd Portfolio_Rushabh
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the app**
   ```bash
   python app.py
   ```
4. **Visit** [http://localhost:5000](http://localhost:5000)

---

## 🚀 Deployment
- Deploy to [Render](https://render.com/) or any Python host.
- Make sure to include `Procfile` and `gunicorn` in `requirements.txt`.

---

## 🖼️ Screenshots
| Home | Projects | Achievements | Blog | Theme Toggle |
|------|----------|--------------|------|-------------|
| ![Home](static/images/profile.jpg) | ![Projects](static/images/profile.jpg) | ![Achievements](static/images/profile.jpg) | ![Blog](static/images/profile.jpg) | ![Toggle](static/images/theme-toggle-demo.png) |

---

## 📝 Customization
- **Edit your info, projects, achievements:**
  - Open `data.py` and update the variables and lists.
- **Customize the theme toggle:**
  - The theme toggle switch is fully animated and adapts to light/dark mode.
  - To change its style, edit the `.theme-toggle-switch` section in `static/css/style.css`.
  - The toggle is always accessible: on desktop it appears at the right center, on mobile at the bottom right.
- **Add blog posts:**
  - Add Markdown files to the `blog/` folder. Use front matter for title, date, summary, and (optionally) featured_image.
- **Change styles:**
  - Edit `static/css/style.css` for colors, fonts, and layout.
- **Update contact info:**
  - Edit the `CONTACT` dictionary in `data.py`.

---

## 📚 Documentation
See [DOCUMENTATION.md](DOCUMENTATION.md) for a detailed, beginner-friendly explanation of the codebase, file structure, and how to edit every part of your website.

---

## 🌗 Theme & Responsiveness
- The site automatically adapts to light and dark mode, including all cards, text, and the GitHub contributions section.
- The animated theme toggle switch visually changes between sun/clouds and moon/stars.
- The toggle is always accessible and moves to the best position for your device.

---

## 🤝 Connect with Me
[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?logo=linkedin)](https://linkedin.com/in/rushabh-singh-22b23a2bb)
[![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/Rush1618)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?logo=instagram&logoColor=white)](https://instagram.com/rushabhsingh69)

---

## 📄 License
MIT 