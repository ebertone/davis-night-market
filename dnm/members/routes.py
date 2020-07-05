from flask import Blueprint, request
from dnm import db
from dnm.models import Member

# Blueprint for members
members = Blueprint("members", __name__)


@members.route("/members/create", methods=["POST"])
def create_member():
    data = request.get_json()
    image = "https://davis-night-market-cms.herokuapp.com" + data["entry"]["image"]["url"]
    member = Member(name=data["entry"]["name"], 
                    image=image, 
                    content_id=data["entry"]["id"])
    db.session.add(member)
    db.session.commit()

    return {"Message": "Member Created"}, 200


@members.route("/members/update", methods=["POST"])
def update_members():
    data = request.get_json()
    member = Member.query.filter_by(content_id=data["entry"]["id"]).first()
    member.name = data["entry"]["name"]
    image = "https://davis-night-market-cms.herokuapp.com" + data["entry"]["image"]["url"]
    member.image = image
    db.session.commit()

    return {"Message": "Member Updated"}, 200


@members.route("/members/delete", methods=["POST"])
def delete_member():
    data = request.get_json()
    member = Member.query.filter_by(content_id=data["entry"]["id"]).first()
    db.session.delete(member)
    db.session.commit()

    return {"Message": "Member Deleted"}, 200