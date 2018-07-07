from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
# from api import app

db = SQLAlchemy()
ma = Marshmallow()


class Word(db.Model):
    __tablename__ = 'words'
    id = db.Column(db.Integer, primary_key=True)
    enword = db.Column(db.String(250), nullable=False)
    phonetic = db.Column(db.String(250))
    wordclass = db.Column(db.String(250))
    cnword = db.Column(db.String(250))
    voice = db.Column(db.String(250))

    def __init__(self, enword, phonetic, wordclass, cnword, voice):
        self.enword = enword
        self.phonetic = phonetic
        self.wordclass = wordclass
        self.cnword = cnword
        self.voice = voice


class WordSchema(ma.ModelSchema):
    class Meta:
        model = Word
