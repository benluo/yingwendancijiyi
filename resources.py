from flask import request
from flask_restful import Resource
from models import db, Word, WordSchema
import urllib
from sqlalchemy.sql.expression import func, select

words_schema = WordSchema(many=True)
word_schema = WordSchema()


class WordListResource(Resource):
    def get(self):
        random = request.args.get('random')
        if random:
            words = Word.query.order_by(func.random()).all()
        else:
            words = Word.query.all()
        words = words_schema.dump(words).data
        return {'status': 'success', 'data': words}, 200


class WordResource(Resource):
    def get(self, id):
        word = Word.query.get_or_404(id)
        word = word_schema.dump(word).data
        return {'status': 'success', 'data': word}, 200


class WordByEnWordResource(Resource):
    def get(self, enWord):
        word = Word.query.filter_by(enword=enWord).first_or_404()
        word = word_schema.dump(word).data
        return {'status': 'success', 'data': word}, 200


class QueryResource(Resource):
    def get(self):
        qWord = request.args.get('word')
        if not qWord:
            return {'status': 'failed'}, 404

        qWord = "%" + str(urllib.parse.unquote(qWord)) + "%"
        enwords = Word.query.filter(Word.enword.like(qWord)).all()
        cnwords = Word.query.filter(Word.cnword.like(qWord)).all()
        if enwords:
            words = enwords
        elif cnwords:
            words = cnwords
        else:
            return {'status': 'failed'}, 404
        words = words_schema.dump(words).data
        return {'status': 'success', 'data': words}, 200
