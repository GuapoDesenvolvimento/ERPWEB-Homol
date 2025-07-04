@echo off
cd "C:\Users\redeg\OneDrive\Área de Trabalho\ERPWEB"
set FLASK_APP=main.py
set FLASK_ENV=development
python -m flask run --host=0.0.0.0
pause