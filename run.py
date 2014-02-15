#!/usr/bin/env python
# -*- coding: utf-8 -*-
from memcache_cloud import app

if __name__ == "__main__":
    app.run(host=app.config['HOST'], port=app.config['PORT'])

