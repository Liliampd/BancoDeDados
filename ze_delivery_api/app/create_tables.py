from app.database import Base, engine
from app.models import Partner


# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)
