#Apagar ambiente virtual existente:
	##rmdir /s /q venv (windows)
 	##rm -rf venv (Linux ou MAC)
#Criar ambiente virtual:
	##python -m venv venv (lembre-se de fazer na pasta do projeto)
#Ativar o ambiente virtual:
	##venv\Scripts\activate (windows)
	##source venv/bin/activate (Linux ou MAC)
#Instalar Flask e outros:
	##pip install flask flask_sqlalchemy flask_migrate pyodbc
	##pip install mysql-connector-python ou pip install psycopg2 - Bancos de dados
	##pip install python-dotenv
	##pip install pyside6 requests openpyxl - Interface
#Rodar funcionalidades:
	##flask run - API
	##cd app\interface - python main.py - Interface
