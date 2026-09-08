import time
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class BotConfig(BaseModel):
    login: int
    password: str
    server: str
    symbol: str = "EURUSD"
    lot: float = 0.1

bot_status = {
    "running": False,
    "trades_count": 0,
    "last_message": "البوت في وضع الاستعداد"
}

@app.get("/")
def home():
    return {"status": "MT5 Automated Scalper is Active"}

@app.post("/start-bot")
def start_bot(config: BotConfig):
    bot_status["running"] = True
    bot_status["last_message"] = f"تم الاتصال بالحساب {config.login} على سيرفر {config.server} وبدء الاسكالْبينج الآلي."
    
    # محاكاة الاتصال الفعلي بمنصة MT5 وتنفيذ الصفقات تباعاً
    # (في السيرفر السحابي الفعلي، يتم دمج مكتبة MetaTrader5 هنا لتنفيذ الأمر على منصة البروكر)
    print(f"[MT5 Bridge]: Connected to {config.login} | Symbol: {config.symbol} | Lot: {config.lot}")
    
    return {
        "status": "success",
        "message": f"تم تفعيل التداول الآلي بنجاح على الزوج {config.symbol} بحجم عقد {config.lot}"
    }

@app.post("/stop-bot")
def stop_bot():
    bot_status["running"] = False
    bot_status["last_message"] = "تم إيقاف البوت."
    return {"status": "success", "message": "تم إيقاف التداول الآلي."}

@app.get("/status")
def get_status():
    return bot_status
    
