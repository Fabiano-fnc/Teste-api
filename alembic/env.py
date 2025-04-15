import os
import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importações dos modelos e da Base
from app.database import Base
import app.models.filme  # noqa: F401
import app.models.review  # noqa: F401
import app.models.usuario  # noqa: F401

# Carregar config do alembic.ini
config = context.config
config.set_main_option("sqlalchemy.url", os.getenv("DATABASE_URL"))

# Configuração de log
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Referência aos metadados dos modelos
target_metadata = Base.metadata
