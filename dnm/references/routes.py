from flask import Blueprint, request

# Blueprint for references
references = Blueprint("references", __name__)

@references.route("references/create")
def create_reference():
    data = request.get_json()
    reference = Reference(name=data["name"], link=data["link"], image=data["image"])
    db.session.add(reference)
    db.session.commit()
    return {"Status" : "Reference created"}

# @references.route("references/update")
# def update_reference():
#     pass
#
# @references.route("references/delete")
# def delete_reference():
#     pass
