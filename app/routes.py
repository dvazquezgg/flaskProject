from flask import Blueprint, request, jsonify
from .models import db, Tenant

routes_blueprint = Blueprint('routes', __name__)

# Route definitions go here
# A decorator used to tell the application
# which URL is associated function
@routes_blueprint.route('/')
def hello():
    return 'HELLO'

# decorator to route URL
@routes_blueprint.route('/hello')
# binding to the function of route
def hello_world():
    return 'hello world'

# routing the decorator function hello_name
@routes_blueprint.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name


@routes_blueprint.route('/tenants', methods=['POST'])
def create_tenant():
    data = request.json  # Assuming JSON data is sent in the request body

    # Extracting data from the request
    apartment_number = data.get('apartment_number')
    primary_tenant_name = data.get('primary_tenant_name')
    primary_tenant_email = data.get('primary_tenant_email')
    secondary_tenant_name = data.get('secondary_tenant_name')
    secondary_tenant_email = data.get('secondary_tenant_email')
    monthly_quote = data.get('monthly_quote')

    # Create a new Tenant object
    new_tenant = Tenant(apartment_number=apartment_number,
                        primary_tenant_name=primary_tenant_name,
                        primary_tenant_email=primary_tenant_email,
                        secondary_tenant_name=secondary_tenant_name,
                        secondary_tenant_email=secondary_tenant_email,
                        monthly_quote=monthly_quote)

    # Add the new tenant to the database
    db.session.add(new_tenant)
    db.session.commit()

    # Return a JSON response indicating success
    return jsonify({'message': 'Tenant created successfully'}), 201

@routes_blueprint.route('/tenants', methods=['GET'])
def get_tenants():
    # Query all tenants from the database
    tenants = Tenant.query.all()

    # Convert the tenants to a list of dictionaries
    tenants_list = []
    for tenant in tenants:
        tenant_data = {
            'apartment_number': tenant.apartment_number,
            'primary_tenant_name': tenant.primary_tenant_name,
            'primary_tenant_email': tenant.primary_tenant_email,
            'secondary_tenant_name': tenant.secondary_tenant_name,
            'secondary_tenant_email': tenant.secondary_tenant_email,
            'monthly_quote': tenant.monthly_quote
        }
        tenants_list.append(tenant_data)

    # Return the list of tenants as a JSON response
    return jsonify(tenants_list), 200

@routes_blueprint.route('/tenants/<int:apartment_number>', methods=['GET'])
def get_tenant(apartment_number):
    # Query the tenant with the given apartment number
    tenant = Tenant.query.filter_by(apartment_number=apartment_number).first()

    # If the tenant does not exist, return a 404 error
    if tenant is None:
        return jsonify({'message': 'Tenant not found'}), 404

    # Convert the tenant to a dictionary
    tenant_data = {
        'apartment_number': tenant.apartment_number,
        'primary_tenant_name': tenant.primary_tenant_name,
        'primary_tenant_email': tenant.primary_tenant_email,
        'secondary_tenant_name': tenant.secondary_tenant_name,
        'secondary_tenant_email': tenant.secondary_tenant_email,
        'monthly_quote': tenant.monthly_quote
    }

    # Return the tenant as a JSON response
    return jsonify(tenant_data), 200

@routes_blueprint.route('/tenants/<int:apartment_number>', methods=['PUT'])
def update_tenant(apartment_number):
    # Query the tenant with the given apartment number
    tenant = Tenant.query.filter_by(apartment_number=apartment_number).first()

    # If the tenant does not exist, return a 404 error
    if tenant is None:
        return jsonify({'message': 'Tenant not found'}), 404

    data = request.json

    # Update the tenant data
    tenant.primary_tenant_name = data.get('primary_tenant_name', tenant.primary_tenant_name)
    tenant.primary_tenant_email = data.get('primary_tenant_email', tenant.primary_tenant_email)
    tenant.secondary_tenant_name = data.get('secondary_tenant_name', tenant.secondary_tenant_name)
    tenant.secondary_tenant_email = data.get('secondary_tenant_email', tenant.secondary_tenant_email)
    tenant.monthly_quote = data.get('monthly_quote', tenant.monthly_quote)

    # Commit the changes to the database
    db.session.commit()

    # Return a JSON response indicating success
    return jsonify({'message': 'Tenant updated successfully'}), 200

@routes_blueprint.route('/tenants/<int:apartment_number>', methods=['DELETE'])
def delete_tenant(apartment_number):
    # Query the tenant with the given apartment number
    tenant = Tenant.query.filter_by(apartment_number=apartment_number).first()

    # If the tenant does not exist, return a 404 error
    if tenant is None:
        return jsonify({'message': 'Tenant not found'}), 404

    # Delete the tenant from the database
    db.session.delete(tenant)
    db.session.commit()

    # Return a JSON response indicating success
    return jsonify({'message': 'Tenant deleted successfully'}), 200

# Path: app/models.py
