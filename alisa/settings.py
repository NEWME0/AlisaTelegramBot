import os
import dotenv


dotenv.load_dotenv()


API_TOKEN = os.getenv('API_TOKEN')

BASE_ROOT = os.path.dirname(os.path.abspath(__file__))

STORAGE_ROOT = os.path.join(os.path.dirname(BASE_ROOT), 'storage')
