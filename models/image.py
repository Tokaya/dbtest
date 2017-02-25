from . import *


class Image(db.Document, ModelMixin):
    name = db.StringField(requid=True)
    path = db.StringField(requid=True)
    created_time = db.DateTimeField(default=datetime.datetime.now())