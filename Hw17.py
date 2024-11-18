#start--- hw17
#1


israel = {"name": "Israel",
"birth": 1948,
"population_millions": 9.3,
"capital": "Jerusalem",
"language": "Hebrew",
"cities": ["Jerusalem", "Tel Aviv", "Haifa", "Rishon LeZion", "Petah Tikva", "Ashdod"],
"currency": "ILS",
"area_Kilometer": 22145,
"gdp_billion": 450}
print(israel)
print(israel["capital"])
print(israel.keys())
print(israel.values())
for item in israel:
    print(item, end= " ")
israel_newD = israel.copy()
gdp_bill = israel_newD.pop("gdp_billion")
print(israel_newD)
new_country = dict.fromkeys(israel.keys())
print(new_country)
new_country["cities"]= [input("enter city:") for i in range(3)]
print(new_country)

#2 ---leetcode
"""find the length of the last word"""
s = "lior is a master in python"
s_words = s.split(" ")

print(f"The last word is '{s_words[-1]}' with length {len(s_words[-1])}")






