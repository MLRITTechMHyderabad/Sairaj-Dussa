"""For each employee:
• If their rating is 4 or 5, increase their salary by 10%.
• If their rating is 3, increase their salary by 5%.
• If their rating is 1 or 2, decrease their salary by 3%"""

employees = [
    {"name": "Alice", "salary": 50000.0, "rating": 5},
    {"name": "Bob", "salary": 40000.0, "rating": 3},
    {"name": "Charlie", "salary": 35000.0, "rating": 2}
]

updated_employees = list(map(lambda x:
                             {**x, "salary":
                                round(x["salary"] * (1.10 if x["rating"] >= 4
                                    else 1.05 if x["rating"] == 3
                                    else 0.97), 2)
                            }, employees))
print(f"before Updation {employees}")
print(f"The Updated List{updated_employees}")
