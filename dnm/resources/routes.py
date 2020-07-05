from flask import Blueprint, request
from dnm import db
from dnm.models import Resource

# Blueprint for resources
resources = Blueprint("resources", __name__)


@resources.route("/resources/create", methods=['POST'])
def create_resource():
    data = request.get_json()
    image = "https://dnm-cms.herokuapp.com" + data["entry"]["image"]["url"]
    resource = Resource(name=data["entry"]["name"], 
                        link=data["entry"]["link"], 
                        content_id=data["entry"]["id"])
    db.session.add(resource)
    db.session.commit()

    return {"Message": "Resource Created"}, 200


@resources.route("/resources/update", methods=['POST'])
def update_resource():
    data = request.get_json()
    new_image = "https://dnm-cms.herokuapp.com" + data["entry"]["image"]["url"]
    resource = Resource.query.filter_by(content_id=data["entry"]["id"]).first()
    resource.name = data["entry"]["name"]
    resource.link = data["entry"]["link"]
    resource.image = new_image
    db.session.commit()

    return {"Message": "Resource Updated"}, 200


@resources.route("/resources/delete", methods=['POST'])
def delete_resource():
    data = request.get_json()
    resource = Resource.query.filter_by(content_id=data["entry"]["id"]).first()
    db.session.delete(resource)
    db.session.commit()

    return {"Message": "Resource Deleted"}, 200