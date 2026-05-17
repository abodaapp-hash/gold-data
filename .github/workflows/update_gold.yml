import requests
import os
import time
import json

URL = "https://dahabmasr.com/PriceAuth/data.json"
os.makedirs("data", exist_ok=True)

# كسر الكاش بالطريقة الصحيحة باستخدام علامة الاستفهام ?
url_with_time = f"{URL}?t={int(time.time())}"

response = requests.get(url_with_time)

if response.status_code == 200:
    # قراءة البيانات كـ JSON
    data = response.json()
    
    # إضافة وقت التحديث داخل البيانات نفسها لضمان حدوث تغيير للـ Commit
    data["last_update_timestamp"] = time.ctime()
    
    # حفظ الملف بصيغة JSON
    with open("data/latest.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        
    print("✅ Updated latest.json")
else:
    print(f"❌ Failed to fetch data. Status code: {response.status_code}")
