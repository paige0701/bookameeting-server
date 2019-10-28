from flask import Blueprint, make_response, jsonify
from flask_restful import Resource, Api
from sqlalchemy.exc import SQLAlchemyError

from app.models import MeetingRoomSchema, MeetingRoom, db
import status
api_bp = Blueprint('api', __name__)
meeting_room_schema = MeetingRoomSchema()
api = Api(api_bp)


class MeetingRoomResource(Resource):

    def get(self, id):
        room = MeetingRoom.query.get_or_404(id)
        result = meeting_room_schema.dump(room).data
        return result

    def delete(self, id):
        room = MeetingRoom.query.get_or_404(id)
        try:
            delete = room.delete(room)
            response = make_response()
            return response, status.HTTP_204_NO_CONTENT
        except SQLAlchemyError as e:
            db.session.rollback()
            resp = jsonify({"error": str(e)})
            return resp, status.HTTP_401_UNAUTHORIZED


api.add_resource(MeetingRoomResource, '/meetingroom/<int:id>')