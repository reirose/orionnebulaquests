from telegram.ext import Updater

import logging

debug = 0  # TODO: сделать командой бота
TOKEN = "5240399182:AAFXRenIB9Sv9EisZBXlGIJEkbV9VxgajJc"
DEBUG_TOKEN = "1050588160:AAHyzSPWCGn1Lw7OCRf9DeVCNuBp4hj5NQM"

console = logging.StreamHandler()
console.setLevel(logging.INFO)

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    handlers=[console])
logger = logging.getLogger(__name__)

updater = Updater(TOKEN if not debug else DEBUG_TOKEN)
dp = updater.dispatcher
job = dp.job_queue
