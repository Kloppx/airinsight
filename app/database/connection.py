import os
import logging
from contextlib import contextmanager

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

load_dotenv()

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def get_database_url() -> str:
	url = os.getenv("DATABASE_URL")
	if not url:
		raise RuntimeError("DATABASE_URL não definido no ambiente")
	return url


def get_engine(echo: bool = False):
	"""Cria e retorna um SQLAlchemy Engine configurado.

	Não abre conexões ao importar o módulo; o caller controla o uso.
	"""
	db_url = get_database_url()
	return create_engine(db_url, future=True, echo=echo)


@contextmanager
def get_connection(engine=None):
	"""Context manager que fornece uma conexão e garante fechamento/dispose.

	Uso:
		with get_connection() as conn:
			conn.execute(...)
	"""
	own_engine = False
	if engine is None:
		engine = get_engine()
		own_engine = True
	conn = None
	try:
		conn = engine.connect()
		yield conn
	except OperationalError:
		logger.exception("Falha ao conectar ao banco de dados")
		raise
	finally:
		if conn is not None:
			conn.close()
		if own_engine:
			engine.dispose()


if __name__ == "__main__":
	try:
		with get_connection() as conn:
			logger.info("Connected successfully!")
	except Exception as e:
		logger.exception("Connection test failed: %s", e)