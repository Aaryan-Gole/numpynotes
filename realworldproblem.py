import numpy as np
import matplotlib.pyplot as plt

# Data structure: [restaurant_id, 2021, 2022, 2023, 2024]
sales_data = np.array([
    [1, 150000, 180000, 220000, 250000],  # Paradise Biryani
    [2, 120000, 140000, 160000, 190000],  # Beijing Bites
    [3, 200000, 230000, 260000, 300000],  # Pizza Hub
    [4, 180000, 210000, 240000, 270000],  # Burger Point
    [5, 160000, 185000, 205000, 230000]   # Chai Point
])

print("==== zomato sales analysis ====")
print("\n sales data shape: ",sales_data.shape)
print("\n sample data for 1st 3 restaurant: ",sales_data[0:3])

# total sales per year
print("\nsales per year: ",np.sum(sales_data, axis=0))
yearly_total = np.sum(sales_data[:, 1:], axis = 0)
print(yearly_total)

# minimum sales per restaurant
min_sales = np.min(sales_data[:, 1:],axis = 1)
print("\nminumum sale per restaurant: ", min_sales)

# maximum sales per year
max_Sales = np.max(sales_data[:, 1:],axis = 0)
print("\nmaximum sale per year: ",max_Sales)

# average sales per year
avg_Sale = np.mean(sales_data[:, 1:], axis = 1)
print("\naverage sale per restaurant: ",avg_Sale)

# cummulative sales
cumsum = np.cumsum(sales_data[:, 1:],axis = 1)
print("\ncummulative sum : ",cumsum)

plt.figure(figsize=(10,6))
plt.plot(np.mean(cumsum, axis = 0))
plt.title("average cumulative sales across all restaurent: ")
plt.xlabel("years")
plt.ylabel("sales")
plt.grid(True)
plt.show()

# vector
vector1 = np.array([1,2,3,4,5])
vector2 = np.array([6,7,8,9,10])
print("\nvector addition: ", vector1+vector2)
print("\nvector multiplication: ", vector1 * vector2)
print("\n dot product: ",np.dot(vector1,vector2))

angle = np.arccos(np.dot(vector1,vector2) / np.linalg.norm(vector1) * np.linalg.norm(vector2))
print(angle)

restaurent_types = np.array(['biryani','chinese','pizza','burger'])
vectorized_upper = np.vectorize(str.upper)
print("vectorized upper: ",vectorized_upper(restaurent_types))

monthly_avg = sales_data[:, 1:]
print("monthly average: ",monthly_avg)