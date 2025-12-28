# 🔧 DataForge

**DataForge** is a flexible synthetic data generation library for Python, built to support realistic, industry-specific datasets. Whether you're developing analytics dashboards, validating data pipelines, or training ML models, DataForge provides a quick and safe way to get high-quality sample data.

---

## 🚀 Why DataForge?

Generating clean, structured, and realistic sample data is often time-consuming. DataForge helps you:

✅ Prototype faster  
✅ Avoid messy real data  
✅ Simulate business scenarios  
✅ Teach analytics & machine learning  
✅ Benchmark tools and systems

---

## 📦 Installation

```bash
pip install DataForge
```

Requires Python 3.7+

---

## ⚙️ How It Works

DataForge comes with a library of **pre-built dataset generators**. Just specify the dataset type and how many records you want:

```python
from DataForge import DataForge

forge = DataForge()

# List all available dataset types
print(forge.available_datasets())

# Generate 1,000 fake ecommerce records
df = forge.generate('ecommerce', 1000)
print(df.head())
```

You’ll get a clean `pandas.DataFrame` ready for export or visualization.

---

## 📊 Available Datasets

DataForge provides industry-specific synthetic datasets with clean structure and realistic business attributes.

| Dataset Type | About the Dataset | Key Columns Included |
|-------------|------------------|---------------------|
| **Retail Sales** | Simulates ecommerce and retail transactions for pricing, customer segmentation, and profitability analysis. | `retail_id`, `first_name`,`last_name`, `date_of_birth`, `order_date`, `ship_date`, `gender`, `email`, `quantity`, `unit_price`, `unit_cost`, `sales_amount`, `cost_amount`, `phone`, `address`, `city`, `state`, `country`, `store_name`, `store_country`, `store_type`, `store_manager`, `store_phone`, `store_fax`, `store_status`, `product_category`, `product_subcategory`, `product`, `product_desc`, `product_manufacturer`, `product_brand`, `product_class`, `product_color`, `product_size`, `product_weight`, `product_UOM`, `product_stock_type`, `product_status`|
| **Employee Dataset** | HR dataset for payroll analysis, workforce planning, and attrition analytics. | `employee_id`, `first_name`, `last_name`, `start_date`, `exit_date`, `date_of_birth`, `gender`, `employment_type`, `salary`, `email`, `phone`, `department`, `job_title`, `qualifications`, `vacancy_type`, `benefits_list`, `address`, `city`, `state`, `country`, `source` |
| **Job Market Dataset** | Job posting + salary dataset for talent analytics, skill gap analysis & job recommendation engines. | `job_id`, `experience`, `qualifications`, `salary_range`, `location`, `country`, `region`, `latitude`, `longitude`, `work_type`, `job_posting_date`, `preference`, `contact_person`, `contact`, `job_title`, `role`, `job_portal`, `job_description`, `benefits`, `skills`, `responsibilities`, `company_name`, `company_profile` |
| **Courier Logistics** | Shipment journey data for last-mile routing, SLA tracking & delivery analytics. | `Origin`, `Destination`, `Pouch No`, `Date`, `Sender's Name`, `Sender Phone`, `Sender Address`, `Sender City`, `Sender State`, `Sender Pincode`, `Sender GSTIN`, `Total Pieces`, `Actual Wt`, `Volumetric Wt`, `Chargeable Wt`, `Paperwork`, `Sender Signature`, `Sender Date`, `Recipient Name`, `Recipient Phone`, `Recipient Address`, `Recipient City`, `Receiver State`, `Receiver Pincode`, `Description`, `Value Added Services`, `Consignment No`, `Expiry Date`, `Booking Code`, `Recipient GSTIN`, `Receiver Name`, `Relationship`, `Company Stamp`, `Receiver Signature`, `Receive Date`, `Tariff`, `VAS Charges`, `Total Amount`, `Mode`, `Risk Surcharge`, `Mode of Payment`, `Nature of Consignment`|
| **Healthcare Visits** | Clinical visit events for patient journey analytics & hospital operations simulation. | `patient_id`, `visit_id`, `doctor_id`, `visit_date`, `department`, `diagnosis`, `treatment`, `billing_amount`, `insurance_provider`, `visit_status` |




> ℹ️ All datasets are returned as `pandas.DataFrame` objects with valid data types and referential consistency wherever applicable.


> 💡 More datasets will be added. Our goal: **100+ industry-specific datasets**.

---

## 💾 Exporting Data

```python
df.to_csv('sample.csv', index=False)
df.to_excel('sample.xlsx', index=False)
df.to_json('sample.json', orient='records')
```

---

## 📚 Use Cases

- 🎓 Teaching data science and BI
- 🧪 Testing data pipelines and ETL jobs
- 📈 Building dashboards with Power BI / Tableau
- 🤖 Simulating ML training data
- 🧰 Creating product demos

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🧠 Future Plans

- [x] 5+ starter datasets
- [ ] 100+ total industry-specific datasets

---

## 🌐 Links

- 📦 PyPI: [https://pypi.org/project/DataForge](https://pypi.org/project/DataForge)
- 🧑‍💻 GitHub: [https://github.com/your-org/DataForge](https://github.com/your-org/DataForge)
- 📘 Docs: Coming soon

---

> Created with ❤️ by [Ravender Singh Rana](https://github.com/rrana157/) / [BI Learner](https://github.com/rrana157/)
