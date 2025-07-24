import os
import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

# Add app/ to Python path to import models
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))


# Import your SQLAlchemy Base and DB URL
from app.models import Base
from app.database import SQLALCHEMY_DATABASE_URL


# Alembic config setup
config = context.config
config.set_main_option("sqlalchemy.url", SQLALCHEMY_DATABASE_URL)

# Set up logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Metadata for auto-generating migrations
target_metadata = Base.metadata


# Offline migrations (no DB connection needed)
def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

# Online migrations (active DB connection)
def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()

# Run the correct migration mode
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
