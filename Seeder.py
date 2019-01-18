import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import User, Base, Catalog,Item

engine = create_engine('sqlite:///events.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


cat1 = Catalog(name="Riyadh")
session.add(cat1)
session.commit()

cat2 = Catalog(name="Jeddah")
session.add(cat2)
session.commit()

cat3 = Catalog(name="Khobar")
session.add(cat3)
session.commit()


item1 = Item(
  name="X JED",
  description="A family waterfront festival featuring live performance, a theater for entertaining shows",
  catalog=cat2
  )
session.add(item1)
session.commit()

item2 = Item(
  name="Fall Festival",
  description="A Kuwaiti restaurant will be opened for the first time in the Kingdom",
  catalog=cat1
  )
session.add(item2)
session.commit()

item3 = Item(
	name="Khzam Festival",
  description="Near the sand dunes and an area with 350 thousand meters",
  catalog=cat1
)
session.add(item3)
session.commit()


print "events added to DB :D!"