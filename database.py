import databases
import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func

# Configuration de la base de données
DATABASE_URL = "sqlite:///./test.db"
database = databases.Database(DATABASE_URL)

# Configuration SQLAlchemy
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata = MetaData()

# Exemple de table pour des produits
products = Table(
    "products",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(100), nullable=False),
    Column("description", String(500)),
    Column("price", Float, nullable=False),
    Column("created_at", DateTime, server_default=func.now()),
)

# Création des tables
metadata.create_all(bind=engine)
