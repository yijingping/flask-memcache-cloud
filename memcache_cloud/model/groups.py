# -*- coding: utf-8 -*-
from memcache_cloud.db.db import Model
from sqlalchemy import Column, Integer, String

class Groups(Model):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Group %r>' % self.name

