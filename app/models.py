from flask_login import login_manager, UserMixin
from flask_sqlalchemy import SQLAlchemy
from app.app import app

db = SQLAlchemy(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# 회의실 예약 현황
class Booking:
    __tablename__ = 'bookings'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created = db.Column(db.DateTime, default=db.func.now())
    updated = db.Columm(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    booking_start = db.Column(db.DateTime, nullable=False),
    booking_end = db.Column(db.DateTime, nullable=False),
    description = db.Column(db.String(255), nullable=True)


# 회의실
class MeetingRooms(db.Model):
    __tablename__ = 'meeting_rooms'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String())
    capacity = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<id {}>'.format(self.id)


# 유저
class User(db.model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')

    # user authentication information
    email = db.Column(db.String(100, collation='NOCASE'),  unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False, server_default='')
    email_confirmed_at = db.Column(db.DateTime())

    # user information
    image_file = db.Column(db.String(255), nullable=False, default='default.jpg')
    name = db.Column(db.String(20, collation='NOCASE'), nullable=False, server_default='')

    # Define the relationship to Role via UserRoles
    roles = db.relationship('Role', secondary='user_roles')


# 권한
class Role(db.model):

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True)


# Define the UserRoles association table
class UserRoles(db.model):
    __tablename__ = 'user_roles'

    id = db.Column(db.Interval, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))


