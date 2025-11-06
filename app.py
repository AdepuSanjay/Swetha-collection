# app.py
from ecomproj.wsgi import application

# Vercel expects the callable to be named `app`
app = application