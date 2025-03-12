import xml.etree.ElementTree as ET
import csv
import random

folder_path = 'S:/A0005184/AAD/_archiv/2025_03/'

# Parse the old and new XML files
tree_old = ET.parse(f'{folder_path}vystup_202502_01_v0_doplneno.xml')
root_old = tree_old.getroot()

tree_new = ET.parse(f'{folder_path}vystup_202502_01_v0_doplneno_upraveno.xml')
root_new = tree_new.getroot()

# Load CSV intervals
intervals = []
with open('R:/!Pricing/RihaAdam/_AllianzProjects/FixMall/fixmall/intervaly/intervaly.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        lower = float(row[0].replace(',', '.'))
        upper = float(row[1].replace(',', '.'))
        intervals.append((lower, upper))

# Create a dictionary to hold (VehicleID, Year) -> Value mappings from the old XML
old_price_dict = {}
for price_record in root_old.findall(".//PriceRecord"):
    vehicle_id = price_record.find('VehicleID').text
    year = price_record.find('Year').text
    value = float(price_record.find('Value').text)
    old_price_dict[(vehicle_id, year)] = value

number_of_prices = 0
number_of_changed_prices = 0
errors = 0

# Iterate over the new price records and modify values based on the conditions
for price_record in root_new.findall(".//PriceRecord"):
    number_of_prices += 1

    vehicle_id = price_record.find('VehicleID').text
    year = price_record.find('Year').text
    new_value = float(price_record.find('Value').text)

    # Find the old value for the same VehicleID and Year
    if (vehicle_id, year) in old_price_dict:
        old_value = old_price_dict[(vehicle_id, year)]
        
        # Check if the new value falls within any of the intervals
        for lower, upper in intervals:
            if lower <= new_value <= upper and old_value <= lower:
                number_of_changed_prices += 1

                # Calculate the bounds
                min_bound = max(old_value, lower - 500)
                max_bound = lower

                # Round the number to the nearest hundred
                rounded_number = round(int(random.uniform(min_bound, max_bound)), -2)

                # Change the value to the lower bound of the interval
                price_record.find('Value').text = str(int(rounded_number))
                print(f"Updated VehicleID {vehicle_id}, Year {year}: New Value changed from {new_value} to {rounded_number} based on old value {old_value}")
                if old_value > rounded_number:
                    errors += 1
                break

# Save the modified new XML file
tree_new.write(f'{folder_path}vystup_202502_01_v0_doplneno_upraveno_intervaly.xml', encoding='utf-8', xml_declaration=True)

print(f"number_of_prices: {number_of_prices}")
print(f"number_of_changed_prices: {number_of_changed_prices}")
print(f"errors: {errors}")