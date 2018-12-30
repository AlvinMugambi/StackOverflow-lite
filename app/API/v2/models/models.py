from app import db

class Question(db.Model):
    # this class represents the users table

    __tablename__= 'questions'

    id= db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(255))
    question= db.Column(db.String(1000))
    answer=db.Column(db.String(1000))
    date_registered= db.Column(db.DateTime, default=db.func.current_timestamp())


    def __init__(self,name):
        self.title = title

    def save(self):
        db.session,add(self)
        db.session.commit()

    def det_all():
        return users.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Questions:{}>".format(self.title)
