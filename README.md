# 🏨 होटल प्रबंधन प्रणाली - Django

यह एक basic Django project है जिसमें होटल के लिए home page और room page है।

## 📁 फोल्डर संरचना

```
hotel_project/
├── hotel_project/          # Main project folder
│   ├── settings.py         # सभी settings
│   ├── urls.py            # Main URLs
│   ├── wsgi.py            # Production के लिए
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
│       ├── home.html      # Home page
│       ├── rooms.html     # सभी कमरों की list
│       └── room_detail.html # एक कमरे की details
│
├── static/                # CSS, JS, images
├── media/                 # User uploaded files
├── manage.py              # Django command utility
└── requirements.txt       # Python packages
```

## 🚀 शुरुआत करना

### 1. Requirements install करें
```bash
pip install -r requirements.txt
```

### 2. Database migrate करें
```bash
python manage.py migrate
```

### 3. Superuser बनाएं (Admin के लिए)
```bash
python manage.py createsuperuser
```

### 4. Server चलाएं
```bash
python manage.py runserver
```

Server http://127.0.0.1:8000/ पर चलने लगेगा

## 🌐 URLs

- **होम पेज**: http://127.0.0.1:8000/
- **सभी कमरे**: http://127.0.0.1:8000/rooms/
- **कमरे की details**: http://127.0.0.1:8000/room/<id>/
- **Admin panel**: http://127.0.0.1:8000/admin/

## 📝 Admin में कमरे add करें

1. Admin panel में जाएं: http://127.0.0.1:8000/admin/
2. Username और password डालें (जो आपने createsuperuser में बनाया था)
3. "कमरे" पर click करें
4. "कमरा जोड़ें" button पर click करें
5. Details भरें और Save करें

## ✨ Features

- ✅ Responsive design (Mobile, Tablet, Desktop)
- ✅ कमरों की list page
- ✅ कमरे की detailed page
- ✅ Admin panel से कमरे manage करना
- ✅ Hindi comments और labels
- ✅ Simple और clean UI

## 🎨 Styling

- CSS: Base template में inline CSS है
- Responsive: Grid layout और media queries use हो रहे हैं
- Color scheme: Purple और pink का combination

## 📱 Responsive

सभी pages mobile, tablet और desktop पर अच्छे से दिखते हैं।

## 🔧 Project Structure समझना

### hotel/models.py
`Room` model में कमरे की सभी जानकारी है:
- नाम, description
- कमरे का प्रकार (Single, Double, Suite)
- रात भर की कीमत
- सुविधाएं (WiFi, AC, आदि)
- तस्वीर

### hotel/views.py
3 views हैं:
1. `home()` - होम पेज
2. `rooms_list()` - सभी कमरों की list
3. `room_detail()` - एक कमरे की जानकारी

### templates/
Base template से सभी pages inherit करते हैं।

## 🎯 भविष्य के लिए

- [ ] Booking system add करना
- [ ] User authentication
- [ ] Payment integration
- [ ] Email notification
- [ ] Reviews/Ratings

## 📧 Support

किसी भी समस्या के लिए संपर्क करें।

---
**Happy Coding! 🚀**
