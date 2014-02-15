# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

mod = Blueprint("help", __name__, url_prefix="/helps")

@mod.route('/')
def help():
    return render_template("memcache_cloud/help/index.html")
