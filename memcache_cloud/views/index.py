# -*- coding: utf-8 -*-

from flask import Blueprint, render_template
from memcache_cloud.model import Groups, Memcacheds
from memcache_cloud.db.db import db_session

mod = Blueprint("index", __name__)

@mod.route('/')
def index():
    return render_template("memcache_cloud/index.html", 
            group_count = db_session.query(Groups).count(),
            host_count = db_session.query(Memcacheds).group_by(Memcacheds.ip).count(),
            memcached_count = db_session.query(Memcacheds).count())
