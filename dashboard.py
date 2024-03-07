import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

st.set_option('deprecation.showPyplotGlobalUse', False)

def main():
    st.title('📊 Data Visualization Dashboard 📈')

    # Menampilkan pilihan menu
    menu = ["Top 10 Products 🛍️", "Top 10 Cities by Number of Customers 🌆", "Number of Customers by State 🏠", "Top 10 Sellers 💼"]
    choice = st.sidebar.selectbox("Select Visualization", menu)

    # Memanggil fungsi berdasarkan pilihan pengguna
    if choice == "Top 10 Products 🛍️":
        plot_top_10_products()
    elif choice == "Top 10 Cities by Number of Customers 🌆":
        plot_top_10_cities()
    elif choice == "Number of Customers by State 🏠":
        plot_customers_by_state()
    elif choice == "Top 10 Sellers 💼":
        plot_top_10_sellers()

def plot_top_10_products():
    # Data 1
    orders_df = pd.read_csv("https://raw.githubusercontent.com/lmaoyups/bright/main/orders_dataset.csv")
    order_items_df = pd.read_csv("https://raw.githubusercontent.com/lmaoyups/bright/main/order_items_dataset.csv")
    products_df = pd.read_csv("https://raw.githubusercontent.com/lmaoyups/bright/main/products_dataset.csv")

    product_orders = pd.merge(orders_df, order_items_df)
    product_orders = pd.merge(product_orders, products_df, on="product_id")

    # Visualisasi
    plt.figure(figsize=(10, 6))
    sns.countplot(x='product_category_name', data=product_orders, palette='husl', order=product_orders['product_category_name'].value_counts().head(10).index)

    plt.xlabel('Product Category', fontsize=12)
    plt.ylabel('Count', fontsize=12)
    plt.title('Top 10 Products', fontsize=14)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    st.pyplot()

def plot_top_10_cities():
    # Data 2
    customers_df = pd.read_csv("https://raw.githubusercontent.com/lmaoyups/bright/main/customers_dataset.csv")

    # Menghitung jumlah pelanggan per kota
    city_counts = customers_df['customer_city'].value_counts().nlargest(10)

    # Visualisasi
    plt.figure(figsize=(8, 6))
    sns.barplot(x=city_counts.values, y=city_counts.index, palette='muted')
    plt.xlabel('Number of Customers', fontsize=12)
    plt.ylabel('City', fontsize=12)
    plt.title('Top 10 Cities by Number of Customers', fontsize=14)
    plt.grid(axis='x', linestyle='--', alpha=0.5)
    plt.tight_layout()
    st.pyplot()

def plot_customers_by_state():
    # Data 3
    orders_df = pd.read_csv("https://raw.githubusercontent.com/lmaoyups/bright/main/orders_dataset.csv")
    customers_df = pd.read_csv("https://raw.githubusercontent.com/lmaoyups/bright/main/customers_dataset.csv")

    orders_customers_df = pd.merge(orders_df, customers_df, how="left", left_on="customer_id", right_on="customer_id")

    # Hitung jumlah pelanggan per negara bagian
    bystate_df = orders_customers_df['customer_state'].value_counts().reset_index()
    bystate_df.columns = ['customer_state', 'customer_count']

    # Visualisasi
    plt.figure(figsize=(10, 6))
    sns.barplot(x='customer_state', y='customer_count', data=bystate_df, palette='pastel')
    plt.xlabel('State', fontsize=12)
    plt.ylabel('Number of Customers', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.title('Number of Customers by State', fontsize=14)
    plt.tight_layout()
    st.pyplot()

def plot_top_10_sellers():
    # Data 4
    product_orders = pd.read_csv("https://raw.githubusercontent.com/lmaoyups/bright/main/order_items_dataset.csv")
    sellers_df = pd.read_csv("https://raw.githubusercontent.com/lmaoyups/bright/main/sellers_dataset.csv")

    
    # Pastikan kolom yang tepat digunakan untuk merge
    if 'seller_id' not in product_orders.columns or 'seller_id' not in sellers_df.columns:
        raise ValueError("Kolom 'seller_id' tidak ditemukan pada salah satu dataframe")
    
    # Melakukan merge berdasarkan kolom yang sesuai
    all_data = pd.merge(product_orders, sellers_df, how="left", on="seller_id")

    # Visualisasi
    plt.figure(figsize=(8, 8))
    all_data['seller_id'].value_counts()[:10].plot.pie(autopct='%1.1f%%', shadow=True, startangle=90, cmap='coolwarm', labels=None)
    plt.title("Top 10 Sellers", fontsize=16, weight='bold')
    plt.axis('equal')
    plt.legend(labels=all_data['seller_id'].value_counts()[:10].index, loc="best", fontsize=10)
    plt.tight_layout()
    st.pyplot()

    
if __name__ == '__main__':
    main()
