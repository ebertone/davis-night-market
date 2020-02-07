from flask import Blueprint, request
from dnm import db

# Blueprint for members
members = Blueprint("members", __name__)

@members.route("/members/create")
def create_member():
    data = request.get_json()
    member = Member(name=data["member_name"], image=data["member_image"])
    db.session.add(member)
    db.session.commit()
    return {"Message" : "Member Created"}

@members.route("/members/edit")
def update_members():
    data = request.get_json()
    #might change
    member = Member.query.filter_by(content_id=data["id"]).first()
    member.name = data["name"]
    member.image = data["image"]
    db.commit()
    return {"Message" : "Member Updated"}

@members.route("/members/delete")
def delete_member():
    data = request.get_json()
    member = Member.query.filter_by(content_id=data["id"]).first()
    db.delete(member)
    db.commit()
    return {"Message" : "Member Deleted"}
