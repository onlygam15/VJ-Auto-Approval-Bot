# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "29527236"))
    API_HASH = getenv("API_HASH", "528c2db679cf9f523ff64952fcdeffd4")
    BOT_TOKEN = getenv("BOT_TOKEN", "7969060800:AAFY3vawWS-M0nwxr1Am0Pc29kruqpdWvuo")
    # Your Force Subscribe Channel Id Below 
    CHID = int(getenv("CHID", "2453716466")) # Make Bot Admin In This Channel
    # Admin Or Owner Id Below
    SUDO = list(map(int, getenv("SUDO", "711821282").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://onlygam15:qzSZ2sfllQyZCUp5@cluster0.jku0t.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
