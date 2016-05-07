from django.db import models
from mongoengine import *
from mongoengine import connect
connect('website',host = '127.0.0.1',port = 27017)

# Create your models here.
class ArtiInfo(Document):
	des = StringField()
	title = StringField()
	scores = StringField()
	tags = ListField(StringField())

	meta = {
		'collection' : 'arti_info'
	}
