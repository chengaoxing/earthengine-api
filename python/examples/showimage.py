# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# @Author: chengaoxing
# @Date:   2017-08-14 10:06:29
# @Last Modified by:   chengaoxing
# @Last Modified time: 2017-08-14 11:36:24
# Import the Earth Engine Python Packages
import ee

from oauth2client.service_account import ServiceAccountCredentials

client_email = 'account4gee@chen-pku-app.iam.gserviceaccount.com'
scopes = ['https://www.googleapis.com/auth/sqlservice.admin']

credentials = ServiceAccountCredentials.from_p12_keyfile(
    client_email, '/Users/chengaoxing/chen-pku-app-dbdcb868ef05.p12', scopes=scopes)

# import ee.mapclient

# Initialize the Earth Engine object, using the authentication credentials.
ee.Initialize()

# Print the information for an image asset.
image = ee.Image('srtm90_v4')
path = image.getDownloadURL()
# create the vizualization parameters
# viz = {'min':0.0, 'max':4000, 'palette':"000000,0000FF,FDFF92,FF2700,FF00E7"};

# # display the map
# ee.mapclient.addToMap(image,viz, "mymap")