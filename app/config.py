class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///museu_vivo.db'
    #'mssql+pyodbc://JEANVBA/MuseuVivo?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes&server=JEANVBA&database=MuseuVivo'
    #'mysql+mysqlconnector://developer:1234@localhost:3300/MuseuVivo'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
