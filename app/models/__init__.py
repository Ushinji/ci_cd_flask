from flask_sqlalchemy import Model, SQLAlchemy
from sqlalchemy import Column, Integer, BigInteger
from app.utils.time import epoch_msec, epoch_to_jst
from app import application


class RecordNotFoundError(Exception):
    pass


class BaseModel(Model):
    id = Column(Integer, primary_key=True)
    created_time = Column(BigInteger, default=epoch_msec, nullable=False)
    updated_time = Column(BigInteger, default=epoch_msec, nullable=False)

    @property
    def columns(self):
        return [c.name for c in self.__table__.columns]

    @property
    def created_at(self):
        return epoch_to_jst(self.created_time)

    @property
    def updated_at(self):
        return epoch_to_jst(self.updated_time)

    @classmethod
    def first(cls):
        return cls.query.first()

    @classmethod
    def find(cls, id):
        record = cls.query.get(id)
        if not record:
            raise RecordNotFoundError
        return record

    @classmethod
    def find_by(cls, **kwargs):
        return cls.query.filter_by(**kwargs).first()

    @classmethod
    def create(cls, **kwargs):
        return cls(**kwargs).save()

    @classmethod
    def bulk_insert(cls, records, commit=True):
        cls.query.session.bulk_insert_mappings(cls, records)
        if commit:
            cls.query.session.commit()

    def to_dict(self):
        return dict([(c, getattr(self, c)) for c in self.columns])

    def assign(self, **kwargs):
        for key in self.columns:
            if key in kwargs:
                setattr(self, key, kwargs[key])
        return self

    def update(self, **kwargs):
        return self.assign(**kwargs).save()

    def save(self, commit=True):
        self.query.session.add(self)
        if commit:
            self.query.session.commit()
        else:
            self.query.session.flush()
        return self

    def delete(self, commit=True):
        self.query.session.delete(self)
        if commit:
            self.query.session.commit()
        else:
            self.query.session.flush()
        return self


db = SQLAlchemy(application, model_class=BaseModel)

from .user import User
