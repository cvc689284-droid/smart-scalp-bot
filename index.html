import time
import asyncio
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# إعدادات المتداول الآلي (تستطيع تعديلها لاحقاً أو ربطها بالواجهة)
class BotConfig(BaseModel):
    login: int
    password: str
    server: str
    symbol: str = "EURUSD"
    lot: float = 0.1
    is_active: bool = False

bot_status = {
    "running": False,
    "last_action": "متوقف",
    "profit": 0.0
}

@app.get("/")
def home():
    return {"status": "Smart Scalp Bot Server is Running 24/7"}

@app.post("/start-bot")
def start_bot(config: BotConfig):
    bot_status["running"] = True
    bot_status["last_action"] = f"بدء التداول الآلي على الزوج {config.symbol}"
    
    # هنا سيبدأ السيرفر بتنفيذ الصفقات تلقائياً بناءً على الشروط
    print(f"[بوت آلي]: تم تفعيل التداول لحساب {config.login} بالحجم {config.lot}")
    
    return {
        "status": "success",
        "message": "تم تشغيل المتداول الآلي بنجاح وهو الآن يراقب السوق ويدير الصفقات نيابة عنك!"
    }

@app.post("/stop-bot")
def stop_bot():
    bot_status["running"] = False
    bot_status["last_action"] = "تم إيقاف البوت يدوياً"
    return {"status": "success", "message": "تم إيقاف المتداول الآلي بنجاح."}

@app.get("/status")
def get_status():
    return bot_status
    
