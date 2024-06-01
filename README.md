#Apagar ambiente virtual existente:
	##rmdir /s /q venv
#Criar ambiente virtual:
	##python -m venv venv (lembre-se de fazer na pasta do projeto)
#Ativar o ambiente virtual:
	##venv\Scripts\activate (windows)
	##source venv/bin/activate (Linux ou Mac)
#Instalar Flask e outros:
	##pip install flask flask_sqlalchemy flask_migrate pyodbc
#Rodar a aplicação primeira vez:
	##python.exe -m pip install --upgrade pip
#Ativar o servidor:
	##flask run
