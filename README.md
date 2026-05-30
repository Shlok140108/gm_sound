# SB PRO-AUDIO — Django Website

A full Django website for SB PRO-AUDIO, a professional sound system manufacturer, with a modern dark frontend and a fully functional admin panel.

---

## 📁 Project Structure

```
sbproaudio/
├── sbproaudio/         # Project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/               # Main app
│   ├── models.py       # All data models
│   ├── views.py        # Page views
│   ├── urls.py         # URL routing
│   ├── admin.py        # Admin panel config
│   ├── forms.py        # Contact form
│   ├── context_processors.py
│   ├── templates/core/ # All HTML templates
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── about.html
│   │   ├── services.html
│   │   ├── products.html
│   │   ├── testimonials.html
│   │   └── contact.html
│   └── management/commands/
│       └── seed_data.py
├── media/              # Uploaded images (auto-created)
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Prerequisites
- Python 3.10+
- PostgreSQL installed and running
- pip

### 2. Create & Activate Virtual Environment
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Create PostgreSQL Database
Open your PostgreSQL shell (psql) and run:
```sql
CREATE DATABASE sbproaudio;
CREATE USER postgres WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE sbproaudio TO postgres;
```
Or update `settings.py` with your own DB credentials (DB_NAME, DB_USER, DB_PASSWORD).

### 5. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Seed Demo Data
```bash
python manage.py seed_data
```
This creates: site settings, 6 services, 6 "why us" items, 6 product categories, 3 testimonials.

### 7. Create Admin Superuser
```bash
python manage.py createsuperuser
```

### 8. Collect Static Files (optional for dev)
```bash
python manage.py collectstatic
```

### 9. Run Development Server
```bash
python manage.py runserver
```

Visit:
- **Website:** http://127.0.0.1:8000/
- **Admin Panel:** http://127.0.0.1:8000/admin/

---

## 🎛️ Admin Panel Features

| Section | What you can manage |
|---|---|
| **Site Settings** | Logo, phone, email, address, social links, Google Map, SEO |
| **Hero Slides** | Carousel images, titles, subtitles, button links |
| **Products** | Product name, image, category, featured flag |
| **Product Categories** | Organize products into categories |
| **Services** | Service cards with image and description |
| **Why Choose Us** | Reason cards shown on Home & About pages |
| **Testimonials** | Client reviews with rating and photo |
| **Contact Submissions** | View all form submissions, mark as read |

---

## 🌐 Pages

| URL | Page |
|---|---|
| `/` | Home |
| `/about/` | About |
| `/services/` | Services |
| `/products/` | Products (with category filter) |
| `/testimonials/` | Testimonials |
| `/contact/` | Contact Form |
| `/admin/` | Admin Dashboard |

---

## 🎨 Tech Stack

- **Backend:** Django 4.2, Python
- **Database:** PostgreSQL (via psycopg2)
- **Frontend:** Tailwind CSS (CDN), Bebas Neue + DM Sans fonts
- **Media:** Django's built-in MEDIA handling (Pillow)

---

## 🚀 Deployment Tips (later)

When ready to deploy:
1. Set `DEBUG = False` in settings.py
2. Move `SECRET_KEY` to environment variable
3. Use `python-decouple` or `.env` file
4. Configure `ALLOWED_HOSTS` with your domain
5. Use WhiteNoise for static files: `pip install whitenoise`
6. For Railway/Render: add a `Procfile` → `web: gunicorn sbproaudio.wsgi`

---

## 📞 Support

Built for SB PRO-AUDIO, Pune, India.
