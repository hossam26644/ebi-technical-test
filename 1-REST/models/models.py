''' defining the Gene model for the ORM and
	the schema for serialization
'''
from main.application import db, ma


class Gene(db.Model):
    ''' Gene model for ORM '''
    __tablename__ = 'gene_autocomplete'
    #attributes specification
    species = db.Column('species', db.Unicode, primary_key=True)
    stable_id = db.Column('stable_id', db.Unicode, nullable=False, primary_key=True)
    display_label = db.Column('display_label', db.Unicode, primary_key=True)
    location = db.Column('location', db.Unicode, primary_key=True)
    db = db.Column('db', db.Unicode, nullable=False, primary_key=True)

class GeneSchema(ma.ModelSchema):
    ''' schema for marshmallow serialization'''
    class Meta:
        model = Gene
