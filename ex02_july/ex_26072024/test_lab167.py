from dotenv import load_dotenv
import os
def test_update_req():
    load_dotenv()
    url=os.getenv("URL")
    print(url)
    username=os.getenv("username")
    password=os.getenv("password")
    print(username)
    print(password)