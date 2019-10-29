from flask_login import login_manager, UserMixin
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields, validate

db = SQLAlchemy()  # 마시멜로 보다 먼저 생성하는것이 중요!
ma = Marshmallow()


class AddUpdateDelete:
    def add(self, resource):
        db.session.add(resource)
        return db.session.commit()

    def update(self):
        return db.session.commit()

    def delete(self, resource):
        db.session.delete(resource)
        return db.session.commit()

#
# # 회의실 예약 현황
# class Booking:
#     __tablename__ = 'bookings'
#     id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
#     created = db.Column(db.DateTime, default=db.func.now())
#     updated = db.Columm(db.DateTime, default=db.func.now(), onupdate=db.func.now())
#     booking_start = db.Column(db.DateTime, nullable=False),
#     booking_end = db.Column(db.DateTime, nullable=False),
#     description = db.Column(db.String(255), nullable=True)


# 회의실
class MeetingRoom(db.Model, AddUpdateDelete):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    create_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    modify_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity


# 회의실 스키마 (마시멜로)
class MeetingRoomSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True, validate=validate.Length(1))
    capacity = fields.Integer()

# # 유저
# class User(db.model, UserMixin):
#     __tablename__ = 'users'
#
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#
#     active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')
#
#     # user authentication information
#     email = db.Column(db.String(100, collation='NOCASE'),  unique=True, nullable=False)
#     password = db.Column(db.String(255), nullable=False, server_default='')
#     email_confirmed_at = db.Column(db.DateTime())
#
#     # user information
#     image_file = db.Column(db.String(255), nullable=False, default='default.jpg')
#     name = db.Column(db.String(20, collation='NOCASE'), nullable=False, server_default='')
#
#     # Define the relationship to Role via UserRoles
#     roles = db.relationship('Role', secondary='user_roles')
#
#
# # 권한
# class Role(db.model):
#
#     __tablename__ = 'roles'
#
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String(50), unique=True)
#
#
# # Define the UserRoles association table
# class UserRoles(db.model):
#     __tablename__ = 'user_roles'
#
#     id = db.Column(db.Interval, primary_key=True, autoincrement=True)
#     user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
#     role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))
#
#
