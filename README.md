# Flask Portfolio Website

A personal portfolio website built with Flask, featuring projects, achievements, GitHub contributions, a blog (Markdown), and more.

## Features
- Home, About, Projects, Achievements, Blog, Contact sections
- Responsive design with animated gradient and glassmorphism
- GitHub contributions heatmap
- Blog with Markdown support (Flask-FlatPages)
- Dark mode toggle (remembers preference)
- Project carousel/slider for easy navigation

## Setup

1. **Clone the repo**
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Add your profile picture**
   - Place your image in `static/images/profile.jpg`
4. **Run the app**
   ```bash
   python app.py
   ```
5. **Visit** [http://localhost:5000](http://localhost:5000)

## How to Add or Edit Content (Step-by-Step for Beginners)

### 1. Add a New Project
- Open the file called `data.py` in your project folder.
- Find the section that looks like this:
  ```python
  PROJECTS = [
      {
          'title': 'Project One',
          'description': 'Description for project one.',
          'tech': ['Python', 'Flask', 'Bootstrap'],
          'github': 'https://github.com/yourusername/project-one',
          'demo': 'https://demo1.com'
      },
      # ... more projects ...
  ]
  ```
- To add a new project, copy one of the `{ ... }` blocks, paste it below, and change the details (title, description, tech, github, demo).
- Save the file. Your new project will appear in the Projects section!

### 2. Add an Achievement
- In `data.py`, find the `ACHIEVEMENTS` list:
  ```python
  ACHIEVEMENTS = [
      "Winner of XYZ Hackathon 2023",
      "Top 10 in ABC Coding Challenge",
      # ...
  ]
  ```
- Add your new achievement as a new line in the list, inside quotes.
- Save the file.

### 3. Change Contact Info
- In `data.py`, find the `CONTACT` dictionary:
  ```python
  CONTACT = {
      'email': 'your@email.com',
      'phone': '1234567890',
      'linkedin': 'https://linkedin.com/in/yourprofile',
      'instagram': 'https://instagram.com/yourprofile'
  }
  ```
- Change the values to your own info and save the file.

### 4. Add a Blog Post
- Go to the `blog/` folder in your project.
- Create a new file with a name like `my-first-post.md`.
- At the top, add this (change the title and date):
  ```markdown
  title: "My First Blog Post"
  date: 2024-06-20
  published: true
  ```
- Write your post below that in Markdown.
- Save the file. Your post will show up in the Blog section!

### 5. Change Your Name, Role, Tagline, or Bio
- In `data.py`, find these lines:
  ```python
  NAME = "Your Name"
  ROLE = "Your Role"
  TAGLINE = "Your tagline."
  BIO = "A short bio about you."
  PLACE_OF_STUDY = "Your School or College"
  ```
- Change the text to your own info and save the file.

## Customization
- All main colors and styles are in `static/css/style.css`.
- You can change the background, accent colors, or card styles there.
- The main layout is in `templates/index.html`.

## Troubleshooting
- If you add a project or achievement and don't see it, make sure you saved `data.py` and refresh your browser.
- If you get an error, check the terminal for messages.

## License
MIT 