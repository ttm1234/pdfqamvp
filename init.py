from extensions import Base, engine, db_session


def init_db_table():
    import models
    Base.metadata.create_all(bind=engine)
    # for _Model in []:
    #     Base.metadata.tables[_Model.__tablename__].create(bind=engine)


if __name__ == '__main__':
    init_db_table()
