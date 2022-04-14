from telegram.ext import Updater

import logging

debug = 0
TOKEN = "5240399182:AAE5DtqbXbn4_7RGVjHfi_5Y8xvbfKPCVqM"
DEBUG_TOKEN = "1050588160:AAHLgjqZKBf2lrm20Z2mz69HgyEiel1U45E"

console = logging.StreamHandler()
console.setLevel(logging.INFO)

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    handlers=[console])
logger = logging.getLogger(__name__)

updater = Updater(TOKEN if not debug else DEBUG_TOKEN, use_context=True)
dp = updater.dispatcher
job = dp.job_queue
