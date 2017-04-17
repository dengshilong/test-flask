from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from test_flask import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(10))
    addresses = relationship("Address", backref="user")

    def __repr__(self):
        return u'<user id={0}, name={1}>'.format(self.id, self.name).encode('utf-8')


class Address(db.Model):
    __tablename__ = 'addresses'
    id = db.Column(Integer, primary_key=True)
    email = db.Column(String(64))
    user_id = db.Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return '<address id={0}, email={1} user_id={2}>'.format(self.id, self.email, self.user_id)