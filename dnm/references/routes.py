from flask import Blueprint, request
from dnm import db
from dnm.models import Reference

# Blueprint for references
references = Blueprint("references", __name__)


@references.route("/references/create", methods=['POST'])
def create_reference():
    data = request.get_json()
    # Ask Bryan about how to get the reference link from JSON object
    reference = Reference(name=data["entry"]["name"], link=data[""], content_id=data["entry"]["id"])
    db.session.add(reference)
    db.session.commit()

    return {"Status": "Reference Created"}, 200


@references.route("/references/update", methods=['PUT'])
def update_reference():
    data = request.get_json()
    reference = Reference.query.filter_by(content_id=data["id"]).first()
    reference.name = data["name"]
    reference.link = data["link"]
    db.session.commit()

    return {"Message": "Reference Updated"}, 200


@references.route("/references/delete", methods=['DELETE'])
def delete_reference():
    data = request.get_json()
    reference = Reference.query.filter_by(content_id=data["id"]).first()
    db.delete(reference)
    db.session.commit()

    return {"Status": "Reference Deleted"}, 200
