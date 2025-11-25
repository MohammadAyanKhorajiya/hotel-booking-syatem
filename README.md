folder structure 

hotel_project/
├── hotel_project/          # Main project folder
│   ├── settings.py         
│   ├── urls.py            
│   ├── wsgi.py            
│   └── __init__.py
│
├── hotel/                  # Hotel app
│   ├── migrations/         # Database changes
│   ├── models.py          # Database models
│   ├── views.py           # Business logic
│   ├── urls.py            # App URLs
│   ├── admin.py           # Admin panel
│   ├── apps.py            # App config
│   └── __init__.py
│
├── templates/             # HTML templates
│   ├── base.html          # Base template
│   └── hotel/
│       ├── home.html      
│       ├── rooms.html   
│       └── room_detail.html 
│
├── static/                # CSS, JS, images
├── media/                 # User uploaded files
├── manage.py              # Django command utility
└── requirements.txt       # Python packages


