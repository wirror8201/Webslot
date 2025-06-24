import os

# Токен бота от @BotFather
BOT_TOKEN = os.getenv('BOT_TOKEN', 'YOUR_TELEGRAM_BOT_TOKEN')

# Базовый URL WebSlot API
API_BASE_URL = os.getenv('API_BASE_URL', 'https://api.webslot.uz')

# ID организации (берётся из настроек WebSlot)
ORG_ID = os.getenv('ORG_ID', 'YOUR_ORG_ID')
