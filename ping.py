#!/usr/bin/env python

"""
Schedule this script in a cron job or something similar to keep the App Engine
instance warm.

The 3 things that needs to be kept warm are

1) the static file server (I actually never noticed a delay in this tbh)
2) the blobstore storage.  Can be a long delay of 5-10s to warm up
3) the cloud sql instance. Is usually a 5-10s delay to warm up.
"""

from urllib2 import urlopen

# Warm up normal Appengine static file server (is this necessary?)
urlopen('http://kien-on.appspot.com')
# Warm up the Cloud SQL instance
urlopen('http://kien-on.appspot.com/api/v1/page/1/')
# Warm up the Blobstore server
urlopen('http://kien-on.appspot.com/media/blobserve/AMIfv957UOBG3N_QEAwwJ6UqLQEBi4Qf5Rv6BkTSHzdnaWAYbo6QDHRjuaoY-BgV24sFLRotRgs0ZW705PGraasFwnDgd_f_25LEhIUqi1AxHVlyvUkU-PChC8BgHVkt7fMvF1I_CkUyezD-hSTML6nQkpWANHFl4Q/blobs/dummy.png')
