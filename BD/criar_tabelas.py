from banco_de_dados import Base, session, engine

#Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
session.close()


