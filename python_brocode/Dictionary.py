capitals = {
    "USA": "Washington, D.C.",
    "Canada": "Ottawa",
    "United Kingdom": "London",
    "Germany": "Berlin",
    "France": "Paris",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Australia": "Canberra",
    "Japan": "Tokyo"
}
# 1. Access value with get("key")
print(capitals.get("USA"))

# 2. update:
capitals.update({  "India": "New Delhi"}) # add new
capitals.update({  "India": "New Delhi1"}) # update existing one

# 3. remove a particular key:value: pop():
capitals.pop("India")

# 4. Remove last item in dict: popitem():
capitals.popitem()

# 5. clear Dict completely
# capitals.clear()
##################################################################################
                    # keys(), values(), items()
##################################################################################
print(capitals)