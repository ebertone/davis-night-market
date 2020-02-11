from flask import Blueprint, request
from dnm import db
from dnm.models import Member

# Blueprint for members
members = Blueprint("members", __name__)

@members.route("/members/create", methods=["POST"])
def create_member():
    data = request.get_json()
    image = "https://include-dnm.herokuapp.com/" + data["entry"]["Image"][0]["url"]
    member = Member(name=data["entry"]["Name"], image=image, content_id=data["entry"]["id"])
    db.session.add(member)
    db.session.commit()
    print(data)
    return {"Message" : "Member Created"}

@members.route("/members/edit", methods=["PUT"])
def update_members():
    data = request.get_json()
    #might change
    member = Member.query.filter_by(content_id=data["id"]).first()
    member.name = data["name"]
    member.image = data["image"]
    db.commit()
    return {"Message" : "Member Updated"}

@members.route("/members/delete", methods=["DELETE"])
def delete_member():
    data = request.get_json()
    member = Member.query.filter_by(content_id=data["id"]).first()
    db.delete(member)
    db.commit()
    return {"Message" : "Member Deleted"}
