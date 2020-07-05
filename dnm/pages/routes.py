from dnm.models import Member, Resource
from flask import Blueprint, render_template

pages = Blueprint('pages', __name__)


@pages.route("/")
def create_member():
    members = Member.query.all()
    resources = Resource.query.all()
    print(members)
    print(resources)

    return render_template("home.html", members=members, resources=resources)
