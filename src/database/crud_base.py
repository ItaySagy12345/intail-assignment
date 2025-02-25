from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import DeclarativeMeta
from pydantic import BaseModel
from typing import Union
from src.generics.api_interfaces import APIFilter


class CrudBase:
    """
    Abstract class for database models
    """

    @classmethod
    def count(cls, db: Session, **kwargs: dict) -> int:
        """
        Count method for database models
        Param: db [Session]: The database session
        Param: kwargs [Dict]: Filters for the count operation
        Return [Integer]: The number of records
        """

        query = db.query(cls)

        for key, value in kwargs.items():
            query = query.filter(getattr(cls, key) == value)

        return query.count()

    @classmethod
    def list(cls: DeclarativeMeta, db: Session, filter: APIFilter) -> Union[list[DeclarativeMeta], None]:
        """
        List method for database models
        Param: db [Session]: The database session
        Param filter [APIFilter]: Filter for pagination
        Return [Union[list[DeclarativeMeta], None]]: A list of the records
        """

        query = db.query(cls)

        if filter:
            query = query.offset(filter.offset).limit(filter.size)

        return query.all()


    @classmethod
    def find(cls: DeclarativeMeta, db: Session, slug: str) -> Union[DeclarativeMeta, None]:
        """
        Find method for database models
        Param: db [Session]: The database session
        Param: slug [String]: The record's slug
        Return [Union[DeclarativeMeta, None]]: The found record if there was one
        """

        return db.query(cls).filter(cls.slug == slug).first() 

    @classmethod
    def create(cls: DeclarativeMeta, db: Session, data: BaseModel) -> DeclarativeMeta:
        """
        Create method for database models
        Param: db [Session]: The database session
        Param: data [BaseModel]: The data to insert
        Return [DeclarativeMeta]: The created record
        """

        model_data = cls(**data.model_dump())
        db.add(model_data)
        db.commit()
        db.refresh(model_data)
        return model_data