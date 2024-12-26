from app import db

class App(db.Model):
    # Define columns for the table
    id = db.Column(db.Integer, primary_key=True)
    app_name = db.Column(db.String(100), nullable=False)
    version = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(500), nullable=True)

    # Represent the object when queried
    def __repr__(self):
        return f"<App {self.app_name}>"
