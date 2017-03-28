from app import db

class School(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    schoolname = db.Column(db.String(60), index=True, unique=True)
    entryscore = db.Column(db.Integer, index=True, unique=False)

    def __repr__(self):
        return '{} {}'.format(self.schoolname, self.entryscore)