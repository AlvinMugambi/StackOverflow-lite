from app import db

class Users(db.Model):
    # this class represents the users table

    __tablename__= 'users'

    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(255))
    email=db.Column(db.String(255))
    password=db.Column(db.String(255))
    date_registered= db.Column(db.DateTime, default=db.func.current_timestamp())

    def __init__(self,name):
        self.name = name

    def save(self):
        db.session,add(self)
        db.session.commit()

    def det_all():
        return users.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Users:{}>".format(self.name)
