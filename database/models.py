from sqlalchemy import Column, Integer, String, Boolean, func, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


note_m2m_tag = Table(
    "note_m2m_tag",
    Base.metadata,
    Column(
        "note_id",
        Integer,
        ForeignKey("notes.id", ondelete="CASCADE"),
        primary_key=True
    ),
    Column(
        "tag_id",
        Integer,
        ForeignKey("tags.id", ondelete="CASCADE"),
        primary_key=True
    ),
)


class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    created_at = Column('created_at', DateTime, default=func.now())
    description = Column(String(150), nullable=False)
    done = Column(Boolean, default=False)

    tags = relationship("Tag", secondary=note_m2m_tag, backref="notes")
    
    def __repr__(self):
        return f"Note({self.title}, {self.description}, {self.done})"


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(25), nullable=False, unique=True)

    def __repr__(self):
        return f"Tag({self.name})"
