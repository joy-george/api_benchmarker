class Config(object):
    """Parent configuration class."""
    DEBUG = False
    HOST = "0.0.0.0"
    PORT = 5005

class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True
    PORT = 5005

class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    PORT = 8080

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}