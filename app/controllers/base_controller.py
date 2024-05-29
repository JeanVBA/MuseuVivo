from flask import request, jsonify

def base_controller(service):
    def get_all():
        items = service.fetch_all()
        return jsonify(items)

    def get_by_id(id):
        item = service.fetch_by_id(id)
        if isinstance(item, dict):
            return jsonify(item)
        return item

    def create():
        data = request.get_json()
        item = service.create(data)
        if isinstance(item, dict):
            return jsonify(item)
        return item

    def update(id):
        data = request.get_json()
        item = service.update(id, data)
        if isinstance(item, dict):
            return jsonify(item)
        return item

    def delete(id):
        item = service.delete(id)
        if item is None:
            return '', 204
        return item

    return {
        'get_all': get_all,
        'get_by_id': get_by_id,
        'create': create,
        'update': update,
        'delete': delete
    }