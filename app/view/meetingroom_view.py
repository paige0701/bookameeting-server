from flask import Blueprint, request
from flask_restful import Resource, Api
from sqlalchemy.exc import SQLAlchemyError
from app.models import MeetingRoomSchema, MeetingRoom, db

api_bp = Blueprint('api', __name__)
meeting_room_schema = MeetingRoomSchema()
api = Api(api_bp)


class MeetingRoomListResource(Resource):

    # Meeting room list
    def get(self):
        meeting_rooms = MeetingRoom.query.all()
        result = meeting_room_schema.dump(meeting_rooms, many=True)
        return result, 200

    # create meeting room
    def post(self):
        request_dict = request.get_json()
        if not request_dict:
            resp = {'message': 'No input data provided'}
            return resp, 400
        try:
            meeting_room = MeetingRoom(request_dict['name'], request_dict['capacity'])
            db.session.add(meeting_room)
            db.session.commit()
            return {'message': 'Create success'}, 201
        except SQLAlchemyError as e:
            db.session.rollback()
            return str(e), 400


class MeetingRoomResource(Resource):

    def get(self, id):
        room = MeetingRoom.query.filter((getattr(MeetingRoom, 'id') == id)).first()
        if room is not None:
            return meeting_room_schema.dump(room)
        else:
            return 'No user', 400

    def delete(self, id):
        room = MeetingRoom.query.filter((getattr(MeetingRoom, 'id') == id)).first()
        try:
            room.delete(room)
            return "success", 204
        except SQLAlchemyError as e:
            db.session.rollback()
            return str(e), 401

    def patch(self, id):
        room = MeetingRoom.query.filter((getattr(MeetingRoom, 'id') == id)).first()
        request_dict = request.get_json()
        try:
            room.capacity = request_dict['capacity']
            meeting_room_schema.dump(room)
            room.update()
            return self.get(id), 200
        except SQLAlchemyError as e:
            db.session.rollback()
            return str(e), 401


api.add_resource(MeetingRoomResource, '/meetingrooms/<int:id>')
api.add_resource(MeetingRoomListResource, '/meetingrooms')