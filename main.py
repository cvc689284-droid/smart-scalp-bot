from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class TradeRequest(BaseModel):
    login: int
    password: str
    server: str
    symbol: str
    action: str  # 'BUY' or 'SELL'
    lot: float

@app.post("/execute")
def execute_trade(data: TradeRequest):
    # هنا سيتم استقبال بيانات الحساب وأمر التداول من تابلت الأندرويد
    # وبما أننا على السحابة، سنقوم بربطه لاحقاً بواجهة البروكر أو تمريره
    print(f"Received trade request: {data.action} {data.lot} for account {data.login}")
    
    # محاكاة الاستجابة الناجحة للتنفيذ الحقيقي عبر السيرفر
    return {
        "status": "success",
        "message": f"تم إرسال أمر الـ {data.action} بنجاح إلى سيرفر {data.server}",
        "ticket": 12345678,  # رقم الصفقة الوهمي/الحقيقي الذي يرجع من البروكر
        "lot": data.lot
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)
  
