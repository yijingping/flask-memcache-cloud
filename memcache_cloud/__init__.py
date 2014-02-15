# -*- coding: utf-8 -*-

from flask import Flask, send_from_directory
import os
app = Flask(__name__)

app.config.update(
    DEBUG=True,
    ENV="Development",

    HOST='0.0.0.0',
    PORT=7701,
    DB_URI="mysql://root:123456@localhost/mc",
    DB_CONNECT_OPTIONS = {}
)

from memcache_cloud.views import index, host, memcached, group, help

app.register_blueprint(index.mod)
app.register_blueprint(host.mod)
app.register_blueprint(memcached.mod)
app.register_blueprint(group.mod)
app.register_blueprint(help.mod)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static' ), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
