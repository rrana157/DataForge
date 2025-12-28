import pandas as pd
from src.attributes import load_files
from src.common_functions.fake_dates import *


class RetailSalesGenerator:
    def __init__(self, people, retail_store, retail_product, product_promotion, num: int = 10000):
        """

        :type num: int
        """
        self.num = num
        self.people = people
        self.retail_store = retail_store
        self.retail_product = retail_product
        self.product_promotion = product_promotion

    @property
    def retailsales(self):

        qty_generator = lambda: random.randint(*random.choice([
            (1, 20),
            (2, 15),
            (3, 10),
            (1, 8),
            (1, 12)
        ]))

        retail_stores = []
        for item in self.retail_store:
            for _, store in item.items():
                retail_stores.append(store)

        retail_sales = []
        for i in range(self.num):
            retail_id = abs((self.num - random.randint(4792, 5847)) + i)
            order_date, ship_date = generate_employment_dates(min_years_ago=10, max_years_ago=1)
            dob = date_between('-59y', '-19y')
            dob_str = dob.strftime('%Y-%m-%d') if dob else None
            person: object = random.choice(self.people)
            store_details = random.choice(retail_stores)
            product_details = random.choice(self.retail_product)
            quantity = qty_generator()
            sales_amount = quantity * product_details['UnitPrice']
            cost_amount = quantity * product_details['UnitCost']

            retail_sales.append(
                {'retail_id': retail_id, 'first_name': person['First Name'], 'last_name': person['Last Name'],
                 'date_of_birth': dob_str, 'order_date': order_date.strftime('%Y-%m-%d') if order_date else None,
                 'ship_date': ship_date.strftime('%Y-%m-%d') if ship_date else None, 'gender': random.choices(
                    ["Male", "Female", "Other"], weights=random.choice([
                        [0.45, 0.40, 0.15],
                        [0.55, 0.35, 0.1],
                        [0.6, 0.3, 0.1],
                        [0.65, 0.3, 0.05]]), k=self.num),
                 'email': f"{person['First Name'].lower()}.{person['Last Name'].lower()}@{random.choices(['gmail', 'outlook', 'yahoo'])}.com",
                 'quantity': quantity, 'unit_price': product_details['UnitPrice'],
                 'unit_cost': product_details['UnitCost'], 'sales_amount': sales_amount, 'cost_amount': cost_amount,
                 'phone': person['Phone'], 'address': person['Address'], 'city': person['City'],
                 'state': person['State'], 'country': person['Country'],
                 'store_name': store_details['StoreDescription'], 'store_country': store_details['RegionCountryName'],
                 'store_type': store_details['StoreType'], 'store_manager': store_details['StoreManagerName'],
                 'store_phone': store_details['StorePhone'], 'store_fax': store_details['StoreFax'],
                 'store_status': store_details['StoreStatus'],
                 'product_category': product_details['ProductCategoryName'],
                 'product_subcategory': product_details['ProductSubcategoryName'],
                 'product': product_details['ProductName'], 'product_desc': product_details['ProductDescription'],
                 'product_manufacturer': product_details['Manufacturer'], 'product_brand': product_details['BrandName'],
                 'product_class': product_details['ClassName'], 'product_color': product_details['ColorName'],
                 'product_size': product_details['Size'], 'product_weight': product_details['Weight'],
                 'product_UOM': product_details['UnitOfMeasureName'],
                 'product_stock_type': product_details['StockTypeName'], 'product_status': product_details['Status']})

        return pd.DataFrame(retail_sales)


def generate_retailsales(num: int):
    people = load_files.load_files_data('fake_person_profiles.json')
    retail_store = load_files.load_files_data('retail_store.json')
    retail_product = load_files.load_files_data('retail_product.json')
    product_promotion = load_files.load_files_data('promotion.json')

    generator = RetailSalesGenerator(people=people,
                                     retail_store=retail_store,
                                     retail_product=retail_product,
                                     product_promotion=product_promotion,
                                     num=num)

    return generator.retailsales
