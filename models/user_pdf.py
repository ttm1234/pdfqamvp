import datetime
import json
import enum
from sqlalchemy import Column
import sqlalchemy as db
from extensions import Base, db_session, ModelMixin


class UserPdf(Base, ModelMixin):
    __tablename__ = 'user_pdf'

    id = Column(db.Integer, autoincrement=True, primary_key=True, comment='primary_key')
    filename = Column(db.String(length=128), nullable=False, comment='filename')
    file_md5 = Column(db.String(length=32), nullable=False, comment='md5')
    full_filename = Column(db.String(length=256), nullable=False, comment='full_filename')
    processed = Column(db.Boolean, comment='是否处理完成，include 摘要计算 等')
    summary = Column(db.Text, nullable=False, comment='摘要')
    # create_time todo
    # update_time todo

    __table_args__ = (
        db.Index('idx_md5', 'file_md5'),
        {
            'comment': 'UserPdf表',
        },
    )

    def to_dict(self):
        r = {
            'user_pdf_id': self.id,
            'filename': self.filename,
            'file_md5': self.file_md5,
            'summary': self.summary,
            'processed': self.processed,
        }
        return r

    @classmethod
    def create(cls, filename, file_md5, full_filename):
        m = cls()
        # m.id =
        m.filename = filename
        m.file_md5 = file_md5
        m.full_filename = full_filename
        m.processed = False
        m.summary = ''

        m.save()
        return m

    @classmethod
    def get_one(cls, _id):
        r = cls.query.filter(cls.id == _id).first()
        return r

    @classmethod
    def one_from_md5(cls, file_md5):
        r = cls.query.filter(cls.file_md5 == file_md5).first()
        return r

    def update_status(self, summary):
        self.summary = summary
        self.processed = True
        self.save()
