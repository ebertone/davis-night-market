from flask import Blueprint, request

# Blueprint for references
references = Blueprint("references", __name__)

@references.route("/references/create", methods=['GET', 'POST'])
def create_reference():
    data=request.get_json()
    reference=Reference(name=data["name"], link=data["link"], image=data["image"])
    db.session.add(reference)
    db.session.commit()
    return {"Status" : "Reference created"}

@references.route("/references/update", methods=['GET', 'POST'])
def update_reference():
    data = request.get_json()
    reference = reference.query.filter_by().first()
    db.session.commit()
    return {"Message" : "Reference updated"}

@references.route("references/delete", methods=['GET', 'POST'])
def delete_reference():
    data = request.get_json()

    db.session.commit()
    return {"Status" : "Reference deleted"}
    pass
