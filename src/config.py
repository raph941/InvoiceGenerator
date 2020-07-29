import os
import secrets
from dotenv import load_dotenv

#environment variable
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

#configuration
class DevelopmentConfig(object):
    DEBUG = False
    SECRET_KEY = secrets.token_hex(16)
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///" +  os.path.join(basedir, "invoice.db") 
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class ProductionConfig(DevelopmentConfig):
    DEBUG = False

class TestingConfig(DevelopmentConfig):
    DEVELOPMENT = True
    DEBUG = True

    
app_config = {
    "development": DevelopmentConfig,
    "testing" : TestingConfig
}    
    
