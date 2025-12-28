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
| **Retail Sales** | Simulates ecommerce and retail transactions for pricing, customer segmentation, and profitability analysis. | `order_id`, `order_item_id`, `customer_id`, `product_name`, `category`, `quantity`, `unit_price`, `discount`, `order_date`, `payment_method`, `region` |
| **Employee Dataset** | HR dataset for payroll analysis, workforce planning, and attrition analytics. | `employee_id`, `first_name`, `last_name`, `gender`, `department`, `role`, `salary`, `hire_date`, `location`, `manager_id`, `employment_status` |
| **Job Market Dataset** | Job posting + salary dataset for talent analytics, skill gap analysis & job recommendation engines. | `job_id`, `job_title`, `company`, `industry`, `experience_level`, `salary_range`, `skills_required`, `job_type`, `posted_date`, `city`, `country` |
| **Courier Logistics** | Shipment journey data for last-mile routing, SLA tracking & delivery analytics. | `shipment_id`, `tracking_number`, `sender_city`, `receiver_city`, `pickup_date`, `expected_delivery_date`, `current_status`, `courier_partner`, `delivery_priority`, `weight_kg` |
| **Healthcare Visits** | Clinical visit events for patient journey analytics & hospital operations simulation. | `patient_id`, `visit_id`, `doctor_id`, `visit_date`, `department`, `diagnosis`, `treatment`, `billing_amount`, `insurance_provider`, `visit_status` |

> ℹ️ All datasets are returned as `pandas.DataFrame` objects with valid data types and referential consistency wherever applicable.


> 💡 More datasets will be added regularly. Our goal: **1,00+ industry-specific datasets**.

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
- [ ] 1,00+ total industry-specific datasets

---

## 🌐 Links

- 📦 PyPI: [https://pypi.org/project/DataForge](https://pypi.org/project/DataForge)
- 🧑‍💻 GitHub: [https://github.com/your-org/DataForge](https://github.com/your-org/DataForge)
- 📘 Docs: Coming soon

---

> Created with ❤️ by [Ravender Singh Rana](https://github.com/rrana157/) / [BI Learner](https://github.com/rrana157/)
