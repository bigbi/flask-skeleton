from datetime import datetime, timedelta
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Boolean, Integer, String, DateTime

from ..database import db
from ..mixins import CRUDModel

class Karty(CRUDModel):
    __tablename__ = 'karty'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True )
    cislo_karty = Column(String, nullable=False, index=False)
    datum_insertu= Column(DateTime)



    # Use custom constructor
    # pylint: disable=W0231
    def __init__(self, **kwargs):
        self.datum_insertu = datetime.utcnow()
        for k, v in kwargs.iteritems():
            setattr(self, k, v)
    @staticmethod
    def find_by_karty(karty):
        return db.session.query(Karty).filter_by(Karty.cislo_karty = Karty.cislo_karty).all()

