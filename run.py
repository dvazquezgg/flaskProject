from app import create_app, db

app = create_app() # Creates a Flask app

# Using the app context creates database tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    # Create the database tables
    app.run(debug=True)
