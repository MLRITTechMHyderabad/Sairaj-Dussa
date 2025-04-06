customers = [
 {"name": "Emma", "age": 22, "total_purchase": 150.0},
 {"name": "John", "age": 30, "total_purchase": 200.0},
 {"name": "Grace", "age": 45, "total_purchase": 180.0}
]


new_customers = list(filter(lambda x: 18 <= x["age"] <= 25 and x["total_purchase"] % 10 == 0, customers))
print(new_customers)

new_customers1 = list(filter(lambda x: 26 <= x["age"] <= 40 and x["total_purchase"] % 5 == 0, customers))
print(new_customers1)
