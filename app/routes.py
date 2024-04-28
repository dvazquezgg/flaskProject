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