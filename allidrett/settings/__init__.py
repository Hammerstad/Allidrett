try:
    from allidrett.settings.development import *
    print("Using development settings")
except ImportError:
    # Looks like we dont have a development file, 
    # since that is ignored by docker
    from allidrett.settings.production import *
    print("Using production settings")
