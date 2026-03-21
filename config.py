import os
from dotenv import load_dotenv

load_dotenv()

USER = os.getenv("UAGRM_USER")
PASSWORD = os.getenv("UAGRM_PASS")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# Other configs
LINK_PAGE= "https://inscripcion.uagrm.edu.bo/idxLogin.aspx"