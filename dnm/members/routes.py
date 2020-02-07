from flask import Blueprint
from flask import request
# Blueprint for members
members = Blueprint("members", __name__)

@members.route("/members/create")
def create_member():
    data = request.get_json()
    member = Member(member_name=data["member_name"], member_image=data["member_image"], member_description=data["member_description"])
    db.session.add(member)
    db.session.commit()
    return {{"Status" : "Created"}}

@members.route("/members/fetch_members")
def fetch_members():
