from environs import Env
from pathlib import Path

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("ip")
REST_API_ADDRESS = env.str("REST_API_ADDRESS")
# PAYMENT_PROVIDER_TOKEN = env.str('PAYMENT_PROVIDER_TOKEN')


I18N_DOMAIN = 'SWIPEbot'
BASE_DIR = Path(__file__).parent.parent
LOCALES_DIR = Path.joinpath(BASE_DIR, 'locales')
REDIS_HOST = 'localhost'
