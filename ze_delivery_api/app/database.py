from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# Carrega as variáveis do .env
load_dotenv()

# Pega os dados do banco do .env
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Monta a URL de conexão com o MySQL
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Cria o engine de conexão
engine = create_engine(DATABASE_URL)

# Cria uma sessão para o banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Cria o base para os modelos
Base = declarative_base()
