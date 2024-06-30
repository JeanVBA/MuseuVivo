class Config:
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://JEANVBA/MuseuVivo?driver=ODBC+Driver+18+for+SQL+Server&trusted_connection=yes&TrustServerCertificate=yes'
        #'mssql+pyodbc://JEANVBA/MuseuVivo?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes&server=JEANVBA&database=MuseuVivo'
    #'mysql+mysqlconnector://developer:1234@localhost:3300/MuseuVivo'
    #'sqlite:///museu_vivo.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
