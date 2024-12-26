from flask import request, jsonify, make_response
from app import app, db
from models import App


## function to add app
@app.route('/add-app', methods=['OPTIONS', 'POST'])

def add_app():
    
    # Get JSON data from the request body
    data = request.get_json()

    # Extract app and system details
    app_name = data.get('app_name')
    version = data.get('version')
    description = data.get('description', "")
    system_info = data.get('system_info', {})
    
    os_version = system_info.get('os_version', "")
    device_model = system_info.get('device_model', "")
    available_memory = system_info.get('available_memory', "")

    # Validate required fields
    if not app_name or not version or not os_version or not device_model or not available_memory:
        return jsonify({'error': 'Missing required fields!'}), 400

    # Create a new app instance
    new_app = App(
        app_name=app_name,
        version=version,
        description=description,
        os_version=os_version,
        device_model=device_model,
        available_memory=available_memory
    )

    # Add and commit the new app to the database
    db.session.add(new_app)
    db.session.commit()

    return jsonify({'message': 'App added successfully!'}), 201

## function to fetch entry

@app.route('/get-app/<int:id>', methods=['GET'])
def get_app(id):
    # Retrieve the app by ID
    app_data = App.query.get(id)
    if not app_data:
        return jsonify({'error': 'App not found!'}), 404

    # Return the app details in JSON format
    return jsonify({
        'id': app_data.id,
        'app_name': app_data.app_name,
        'version': app_data.version,
        'description': app_data.description,
        'os_version': app_data.os_version,
        'device_model': app_data.device_model,
        'available_memory': app_data.available_memory
    }), 200

## function to delete entry

@app.route('/delete-app/<int:id>', methods=['DELETE'])
def delete_app(id):
    # Retrieve the app by ID
    app_data = App.query.get(id)
    if not app_data:
        return jsonify({'error': 'App not found!'}), 404

    # Delete the app
    db.session.delete(app_data)
    db.session.commit()

    return jsonify({'message': 'App deleted successfully!'}), 200
