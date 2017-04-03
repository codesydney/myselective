from app import db

class School(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	schoolname = db.Column(db.String(60), index=True, unique=True)
	entryscore = db.Column(db.Integer, index=True, unique=False)
	website = db.Column(db.String(60), index=True, unique=True)
	schooladdress = db.Column(db.String(60), index=True, unique=True)
	schoollat = db.Column(db.Float, index=True, unique=True)
	schoollng = db.Column(db.Float, index=True, unique=True)
	
	def __repr__(self):
		return '{} {} {} {} {} {}'.format(self.schoolname, self.entryscore, self.website, self.schooladdress, self.schoollat, self.schoollng)