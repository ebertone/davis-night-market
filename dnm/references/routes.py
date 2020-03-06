from flask import Blueprint, request
from dnm import db
from dnm.models import Resource

# Blueprint for resources
resources = Blueprint("resources", __name__)


@resources.route("/resources/create", methods=['POST'])
def create_resource():
    data = request.get_json()
    # Ask Bryan about how to get the resource link from JSON object
    resource = Resource(name=data["entry"]["name"], link=data[""], content_id=data["entry"]["id"])
    db.session.add(resource)
    db.session.commit()

    return {"Status": "Resource Created"}, 200


@resources.route("/resources/update", methods=['PUT'])
def update_resource():
    data = request.get_json()
    resource = Resource.query.filter_by(content_id=data["id"]).first()
    resource.name = data["name"]
    resource.link = data["link"]
    db.session.commit()

    return {"Message": "Resource Updated"}, 200


@resources.route("/resources/delete", methods=['DELETE'])
def delete_resource():
    data = request.get_json()
    resource = Resource.query.filter_by(content_id=data["id"]).first()
    db.delete(resource)
    db.session.commit()

    return {"Status": "Resource Deleted"}, 200
