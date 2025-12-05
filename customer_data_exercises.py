import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta


def create_random_gen_df(rows):
    # column list : date, product_id, category, quantity, price, customer_id
    n_rows = rows
    
    #generate random dates + product ids
    start_date = datetime.now() - timedelta(days = 365*2)
    end_date = datetime.now()

    #product ids from 1000-1999
    product_id_list = np.random.randint(1000,2000, size = n_rows)

    categories = ["Clothing", "Food", "Electronics", "Accessories", "Toys"]
    category_data = [random.choice(categories) for _ in range(n_rows)]

    quantity = np.random.randint(1-100, size=n_rows)

    price = np.random.rand(1-1000, size=n_rows)


