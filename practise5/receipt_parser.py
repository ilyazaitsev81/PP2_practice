import re
import json

with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

price_pattern = r"\d{1,3}(?: \d{3})*,\d{2}"
prices = re.findall(price_pattern, text)

product_pattern = r"\d+\.\n(.+)"
products = re.findall(product_pattern, text)

def price_to_float(p):
    return float(p.replace(" ", "").replace(",", "."))

prices_float = [price_to_float(p) for p in prices]
total_calculated = sum(prices_float)
datetime_pattern = r"\d{2}\.\d{2}\.\d{4}\s\d{2}:\d{2}:\d{2}"
datetime_match = re.search(datetime_pattern, text)

datetime_value = datetime_match.group() if datetime_match else None
payment_method = None
if "Банковская карта" in text:
    payment_method = "Bank Card"
elif "Наличные" in text:
    payment_method = "Cash"
result = {
    "products": products,
    "prices": prices,
    "total_calculated": total_calculated,
    "datetime": datetime_value,
    "payment_method": payment_method
}

print(json.dumps(result, indent=4, ensure_ascii=False))