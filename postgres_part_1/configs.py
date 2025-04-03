"""
    Все конфиги проекта.
"""

from postgres_part_1.db_connectors import Connector

# ======================================================================================================================
CONFIG_LOCAL_DB: str = 'sqlite:///local_base.db'
LOCDB_SESSION = Connector(CONFIG_LOCAL_DB).get_session
