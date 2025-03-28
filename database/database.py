import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:0501726116@localhost:5432/marketplace_shop"
# SQLALCHEMY_DATABASE_URL = "postgresql://romanus:L3c4tDtn5ztwn20QTj28S4o0VPfgPCBY@dpg-csjqad9u0jms73b4ds9g-a:5432/marketplace_shop"
# SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://romanus:L3c4tDtn5ztwn20QTj28S4o0VPfgPCBY@dpg-csjqad9u0jms73b4ds9g-a.oregon-postgres.render.com/marketplace_shop"
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://sauron_marketplace_user:LfIVmnkTClxcKQLvOCHjXQNqS6t8P0BH@dpg-cvjed1adbo4c738scn2g-a.oregon-postgres.render.com/sauron_marketplace"
                                    # 'postgresql://romanus:L3c4tDtn5ztwn20QTj28S4o0VPfgPCBY@dpg-csjqad9u0jms73b4ds9g-a/marketplace_shop'
# SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://romanus:L3c4tDtn5ztwn20QTj28S4o0VPfgPCBY@dpg-csjqad9u0jms73b4ds9g-a/marketplace_shop"
# SQLALCHEMY_DATABASE_URL = os.getenv('SQLALCHEMY_DATABASE_URL')

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
