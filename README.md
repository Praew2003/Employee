# Employee

* สร้างโปรเจค

```
django-admin startproject employee
```

- เข้าไปยัง directory ของโปรเจค

```
cd employee
```

- สร้างโฟลเดอร์สำหรับจัดเก็บ static file และ templates

```
mkdir static

mkdir templates
```

- สร้าง env

```
python -m venv env
```

- เปิด vscode ด้วย

```
code .
```

- เปิด terminal

```
pip install django
pip install psycopg2
```

## สร้างแอพแรก

- เปิด terminal ใน vscode
- ใช้คำสั่งเพื่อสร้างแอพ

```
python manage.py startapp  employies
```

## ตั้งค่าโปรเจค

- เขาไปที่ settings.py
- ตั้งค่า ALLOW_HOSTS

```python
ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app']
```

- ตั้งค่า INSTALLED_APPS ให้เพิ่มชื่อแอพที่เราสร้างขึ้นใหม่

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
  
    'employies',
]
```

- ตั้งค่า templates

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [Path.joinpath(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

- ตั้งค่าฐานข้อมูล

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '123456789praewpan',
        'HOST': 'db.efjbiiyxnemzyxgdinty.supabase.co',
        'PORT': '5432',    }
}
```

- ตั้งค่า static

```python
STATIC_URL = 'static/'
STATICFILES_DIRS = [Path.joinpath(BASE_DIR, 'static')]
STATIC_ROOT = Path.joinpath(BASE_DIR, 'staticfiles_build', 'static')
```

## สร้างฐานข้อมูล

- เข้าไปยังแอพที่สร้างขึ้น
- สร้าง ฐานข้อมูล ที่ไฟล์ models.py

```python
from django.db import models

# Create your models here.
class Department(models.Model):
  
    department = models.CharField(max_length=255)
  
    def __str__(self):
        return self.department
  
class Information(models.Model):

    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    gender = models.CharField(max_length=255,choices=(
        ("ชาย", "ชาย"),
        ("หญิง", "หญิง"),
    ))
    age = models.IntegerField()
    elevel = models.CharField(max_length=255,choices=(
        ("ปวช.", "ปวช."),
        ("ปวส.", "ปวส."),
        ("ปริญญาตรี", "ปริญญาตรี"),
        ("สูงกว่าปริญญาตรี", "สูงกว่าปริญญาตรี")
    ))
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
  
  
    def __str__(self):
        return self.fname  
```

- register models ที่ admin.py

```python
from django.contrib import admin

# Register your models here.

from .models import Department, Information

@admin.register(Department)
class Admin(admin.ModelAdmin):
    list_display = ("department",)
    search_fields = ("department",)
  
@admin.register(Information)
class MajorAdmin(admin.ModelAdmin):
    list_display = (
        'fname', 
        'lname', 
        'gender',
        'age',
        'elevel',
        'department',
)
  
```

*การทำ admin register เพื่อที่เราจะสามารถเพิ่มข้อมูลเองได้*

หลังจากนั้นใช้คำสั่ง

```
python manage.py makemigrations

python manage.py migrate
```

## templates หน้าเว็บ

- ให้หา Booststrap 5 template มาใช้
- เลือก `file.html` และย้ายไปที่ `templates/`
- เลือก `css/, js/ assets/` ย้ายไปยัง `static/`
- เข้าไปที่ `templates/` แล้วเลือกไฟล์ที่จะใช้เป็น `base.html`
- แล้วลบ tags ที่ไม่ใช้ออก
- เพิ่ม `{% load static %}` บนสุดของบรรทัด

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
    .
    .
    .

```

- เปลี่ยนการเชื่อมต่อ JavaScript และ CSS จากแบบเดิมเป็นแบบ Django Tempate

*จาก*

```html
 <link rel="stylesheet" href="assets/css/demo.css" />
 <script src="../assets/js/config.js"></script>
```

*เป็น*

```html
 <link href="{% static 'css/styles.css' %}" rel="stylesheet" />
        <script src="https://use.fontawesome.com/releases/v6.3.0/js/all.js" crossorigin="anonymous"></script>
```

*ให้เปลี่ยนทุกตัว*

## การใช้หน้าเว็บร่มกัน (extends)

เป็การใช้องค์ประกอบหน้าเว็บจากหน้า `base.html` ร่วมกัน โดยจาเกปลี่ยนเพี่ยงแค่เนื้อหา
โดยใช้ Django Template Tags ที่ชื่อว่า

```html
{% block name %}{% endblock name %}
```

โดยหน้าที่ต้องการสืบทอดก็ใช้ Django Template Tags ที่ชื่อว่า

```html
{% extends 'base.html' %}

{% block name %}{% endblock name %}
```

แล้วก็ตามด้วยชื่อ block
ตัวอย่าง

`base.html`

```html
<html>
    <head>
        .
        .
        .
    </head>
    <body>
        <header>
        header
        </header>
            {% block name %}{% endblock name %}
        <footer>
        footer
        </footer>
</html>
```

`index.html`

```html
{% extends 'base.html' %}

{% block name %}
<h1>Hello</h1>
{% endblock name %}

```

ผลลัพ

```html
<html>
    <head>
        .
        .
        .
    </head>
    <body>
        <header>
        header
        </header>
            <h1>Hello</h1>
        <footer>
        footer
        </footer>
</html>
```

## Views 

views.py เป็นส่วนที่ควบคุมการทำงานของหน้าเว็บ การ render หน้าเว้บ

- สร้างฟังก์ชันสำหรับ render หน้า index

```python
def home(request):
    context = {}
    information = models.Information.objects.all()
    context['informations'] = information
  
    return render(request,'index.html', context)
```

`context` คือ ค่าที่จะส่งออกไปยังหน้าเว็บ มีรูปแบบเป็น dictionary

` context['informations'] = information`

`models.Information.objects.all()` คือ การดึงค่าทั้งหมดจากตาราง `Information` ที่อยู่ใน ฐานข้อมูล

`return render(request, 'index.html', context)` คือ การรีเทิร์นค่าโดยสั่งให้ render หน้า `index.html` และยังส่ง `context` ออกไปยังหน้าเว็บ

- สร้างตารางใน [`index.html`](./templates/index.html)

```html
{% extends 'base.html' %}
<!---->
{% block title %} หน้าแรก {% endblock title %}
<!---->
{% block content %}
<!---->
<table class="table">
  <thead>
    <tr>
      <th scope="col">ชื่อ</th>
      <th scope="col">นามสกุล</th>
      <th scope="col">เพศ</th>
      <th scope="col">อายุ</th>
      <th scope="col">ระดับการศึกษา</th>
      <th scope="col">แผนกงานที่สังกัด</th>
    </tr>
  </thead>
  <tbody>
    {% for course in informations %}
    <tr>
      <td>{{ course.fname }}</td>
      <td>{{ course.lname }}</td>
      <td>{{ course.gender }}</td>
      <td>{{ course.age }}</td>
      <td>{{ course.elevel }}</td>
      <td>{{ course.department }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>
{% endblock content %}
```

## การสร้าง URL urls.py

เป็นการสร้าง url เพื่อเรียกใช้ฟังก์ชั่นใน views.py

- import แอพ เข้ามาทำงาน

```python
from django.contrib import admin
from django.urls import path

from employies import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='index'),
    path('about/', views.about, name='about'),
    path('purchasing/', views.purchasing, name='purchasing'),
    path('providing/', views.providing, name='providing'),
    path('aftersale/', views.aftersale, name='aftersale'),
]
```

- ใช้คำสั่ง runserver

```
python manage.py runserver
```

หากยังไม่มีข้อมูลก็จะไม่แสดงข้อมูล

## Deploy Vercel

- ตั้งค่า wsgi.py

```python
"""
WSGI config for resgis project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'resgis.settings')

application = get_wsgi_application()

app = get_wsgi_application()
```

เพิ่ม `app = get_wsgi_application()`

- สร้าง vercel.json

```json
{
    "version": 2,
    "builds": [
        {
            "src": "employee/wsgi.py",
            "use": "@vercel/python"
        },
        {
            "src": "build_files.sh",
            "use": "@vercel/static-build",
            "config": {
                "distDir": "staticfiles_build"
            }
        }
    ],
    "routes": [
        {
            "src": "/static/(.*)",
            "dest": "/static/$1"
        },
        {
            "src": "/(.*)",
            "dest": "employee/wsgi.py"
        }
    ]
  
}
```

- สร้าง build_files.sh

```sh
python -m pip install --upgrade pip
pip install -r requirements.txt


python3.9 manage.py collectstatic --noinput --clear
```

- สร้าง `requirements.txt`

```
asgiref==3.7.2
Django==4.2.5
django-dump-load-utf8==0.0.4
psycopg2-binary
sqlparse==0.4.4
tzdata==2023.3
```
