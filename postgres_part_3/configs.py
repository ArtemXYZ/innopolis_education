"""
    Все конфиги проекта.
"""

from postgres_part_1.db_connectors import Connector

# ======================================================================================================================
CONFIG_LOCAL_DB: str = 'sqlite:///local_base.db'
connector = Connector(CONFIG_LOCAL_DB)
ENGINE = connector.engine
LOCDB_SESSION = connector.get_session
