import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('ecommerce_dataset.csv')

# Revenue per product
df['Revenue'] = df['Quantity'] * df['Price']
plt.figure(figsize=(8,5))
plt.bar(df['Product'], df['Revenue'], color='orange')
plt.title('Revenue per Product')
plt.xlabel('Product')
plt.ylabel('Revenue ($)')
plt.show()

# Orders by Payment Method
payment_counts = df['PaymentMethod'].value_counts()
plt.figure(figsize=(6,4))
plt.pie(payment_counts, labels=payment_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Orders by Payment Method')
plt.show()
