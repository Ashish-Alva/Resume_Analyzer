import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()


def create_database_if_not_exists():

    db_name = os.getenv("DB_NAME")

    connection_url = (
        f"postgresql://"
        f"{os.getenv('DB_USER')}:"
        f"{os.getenv('DB_PASSWORD')}@"
        f"{os.getenv('DB_HOST')}:"
        f"{os.getenv('DB_PORT')}/postgres"
    )

    engine = create_engine(
        connection_url,
        isolation_level="AUTOCOMMIT"
    )

    with engine.connect() as conn:

        result = conn.execute(
            text(
                f"SELECT 1 FROM pg_database "
                f"WHERE datname='{db_name}'"
            )
        )

        exists = result.scalar()

        if not exists:

            conn.execute(
                text(
                    f"CREATE DATABASE {db_name}"
                )
            )

            print(
                f"{db_name} created"
            )

        else:

            print(
                f"{db_name} already exists"
            )