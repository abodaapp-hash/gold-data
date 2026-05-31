import requests
import os
import time
import json

URL = "https://dahabmasr.com/PriceAuth/data.json"
os.makedirs("data", exist_ok=True)

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json,text/plain,*/*"
}

def fetch_data():
    url = f"{URL}?t={int(time.time())}"

    try:
        r = requests.get(url, headers=headers, timeout=20)
        print("Status:", r.status_code)

        if r.status_code != 200:
            print("❌ HTTP Error")
            return None

        # تأكد أنه JSON
        try:
            return r.json()
        except Exception:
            print("❌ الرد ليس JSON")
            print(r.text[:300])
            return None

    except Exception as e:
        print("❌ Request Error:", str(e))
        return None


data = fetch_data()

# 🔴 Fallback (لو فشل المصدر)
if not data:
    print("⚠️ استخدام بيانات احتياطية")
    data = {
        "gold": "N/A",
        "status": "fallback",
        "note": "source unavailable",
        "last_update_timestamp": time.ctime()
    }

else:
    data["last_update_timestamp"] = time.ctime()

# حفظ الملف دائمًا بدون فشل
with open("data/latest.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("✅ Done successfully")