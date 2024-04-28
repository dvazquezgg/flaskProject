from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Tenant(db.Model):
    # Model definition goes here
    id = db.Column(db.Integer, primary_key=True)
    apartment_number = db.Column(db.Integer, unique=True, nullable=False)
    primary_tenant_name = db.Column(db.String(100), nullable=False)
    primary_tenant_email = db.Column(db.String(120), unique=True, nullable=False)
    secondary_tenant_name = db.Column(db.String(100))
    secondary_tenant_email = db.Column(db.String(120), unique=True)
    monthly_quote = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Tenant(apartment_number='{self.apartment_number}', primary_tenant_name='{self.primary_tenant_name}', primary_tenant_email='{self.primary_tenant_email}')"


