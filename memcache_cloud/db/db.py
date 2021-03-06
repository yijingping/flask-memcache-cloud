# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.pool import NullPool
from memcache_cloud import app

engine = create_engine(app.config['DB_URI'], poolclass=NullPool, convert_unicode=True,
        **app.config['DB_CONNECT_OPTIONS'])

db_session = scoped_session(sessionmaker(autoflush=True, autocommit=True, bind=engine))

Model = declarative_base(name="Model")

def init_db():
    Model.metadata.create_all(bind=engine)
