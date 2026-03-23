# 🌐 Personal Portfolio Website

A personal portfolio website built with **Python Django** showcasing my skills, projects, and contact information.

---

## 📸 Screenshots

### 🏠 Home Page
![Home Page](Screenshots/home.png)

### 👤 About Page
![About Page](Screenshots/about.png)

### 🛠️ Skills Page
![Skills Page](Screenshots/skills.png)

### 💼 Projects Page
![Projects Page](Screenshots/projects.png)

### 📬 Contact Page
![Contact Page](Screenshots/contact.png)

---

## 🚀 Tech Stack

- **Backend:** Python 3.11, Django 5.2
- **Database:** SQLite3
- **Frontend:** HTML5, CSS3
- **Templating:** Django Template Language (DTL)

---

## ✨ Features

- Responsive multi-page portfolio website
- Home, About, Skills, Projects, and Contact pages
- Contact form with server-side validation
- Contact form submissions saved to database
- Custom CSS styling
- Django Admin panel to view contact submissions

---

## 📁 Project Structure

```
portfolio/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── portfolio/               # Main Django config
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── website/                 # Main Django app
│   ├── views.py
│   ├── models.py
│   ├── admin.py
│   └── migrations/
├── templates/               # HTML templates
│   ├── home.html
│   ├── about.html
│   ├── skills.html
│   ├── Projects.html
│   └── contacts.html
├── static/
│   └── css/
│       └── base.css
└── screenshots/             # Project screenshots
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/portfolio.git
cd portfolio
```

### 2. Create and activate a virtual environment

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Run the development server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

---

## 📄 Pages

| URL | Page |
|-----|------|
| `/` | Home |
| `/about/` | About |
| `/skills/` | Skills |
| `/projects/` | Projects |
| `/contacts/` | Contact Form |
| `/admin/` | Django Admin |

---

## 📬 Contact Form

The contact form at `/contacts/` accepts submissions with:

- First Name *(required)*
- Last Name
- Email *(required)*
- Company
- Project Type
- Budget
- Message *(required)*

All submissions are saved to the database and can be viewed in the Django Admin panel.

---

## 🛠️ Admin Panel

Create a superuser to manage contact submissions:

```bash
python manage.py createsuperuser
```

Then visit `http://127.0.0.1:8000/admin/`

---

## 📦 Requirements

Full list in `requirements.txt`. Main dependency:

```
django==5.2.12
```

---

## 🔧 Environment Notes

> For local development only. Before deploying to production:

- Set `DEBUG = False` in `settings.py`
- Replace `SECRET_KEY` with a secure environment variable
- Add your domain to `ALLOWED_HOSTS`

---

## 👨‍💻 Author

**Your Name**
- GitHub: [@your-username](https://github.com/your-username)
- LinkedIn: [your-linkedin](https://linkedin.com/in/your-linkedin)

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).
