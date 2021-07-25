import requests
VaccineInfo=""

r = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=150&date=22-07-2021',headers={'User-Agent': 'Mozilla/5.0'})
package_json = r.json()
all_centres = package_json['centers']
for price in all_centres:
    if price['fee_type'] == "Free":#change for "Paid" or "Free" Vaccine
        for date in price['sessions']:
            if date['vaccine'] == "COVISHIELD" and date['available_capacity_dose2'] != 0:
                FreeVaccineAddress="Free Vaccine available on " + date['date'] + " in " + price['name'] + price['address']+", "+ str(price['pincode'])+", "+ price['district_name']
                DoseQuantity = "\n" + "No.of Dose2 available=" + str(date['available_capacity_dose2']) + "\n"
                VaccineInfo += FreeVaccineAddress + DoseQuantity + "\n"

if len(VaccineInfo)==0:
    print("Free Vaccine is not available.")

print(VaccineInfo)