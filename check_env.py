from dotenv import load_dotenv
import os

load_dotenv()

print("MENTOR_EMAIL =", os.getenv("MENTOR_EMAIL"))
print("MENTOR_WHITELIST_EMAILS =", os.getenv("MENTOR_WHITELIST_EMAILS"))