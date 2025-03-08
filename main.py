from models import Base, engine
from sqlalchemy.orm import sessionmaker

# Create the database schema
Base.metadata.create_all(engine)

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()

# Alembic migrations
from alembic import command, config
alembic_cfg = config.Config("alembic.ini")
command.upgrade(alembic_cfg, "head")

print("Database setup complete.")
    