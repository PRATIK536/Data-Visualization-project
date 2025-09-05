import requests
from datetime import datetime

# Replace with your desired PIN code and date
PIN_CODE = '411057'  # Example: Pune
DATE = datetime.today().strftime('31-08-2025')  # Format: DD-MM-YYYY

URL = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={PIN_CODE}&date={DATE}"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def fetch_slots():
    try:
        response = requests.get(URL, headers=HEADERS)
        response.raise_for_status()
        data = response.json()

        centers = data.get('centers', [])
        if not centers:
            print(f"No slots available for PIN {PIN_CODE} on {DATE}")
            return

        print(f"\n✅ Vaccine Slots for {PIN_CODE} on {DATE}:\n")
        for center in centers:
            print(f"🏥 {center['name']} - {center['address']}")
            for session in center['sessions']:
                print(f"  📅 Date: {session['date']}")
                print(f"  💉 Vaccine: {session['vaccine']}")
                print(f"  🧑 Age Limit: {session['min_age_limit']}+")
                print(f"  🪑 Available Capacity: {session['available_capacity']}")
                print(f"  💠 Slots: {', '.join(session['slots'])}")
                print("-" * 40)

    except requests.exceptions.RequestException as e:
        print("⚠️ Error fetching data:", e)

if __name__ == "__main__":
    fetch_slots()
    