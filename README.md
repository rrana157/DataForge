# 🔧 DataForge

**DataForge** is a Python library that provides realistic, ready-to-use fake datasets for a variety of industries — perfect for prototyping, testing, data analysis, teaching, and more.

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

| Dataset Type      | Description                         |
|-------------------|-------------------------------------|
| `ecommerce`       | Orders, customers, prices, dates    |
| `healthcare`      | Patients, diagnoses, visits         |
| `banking`         | Transactions, accounts, balances    |
| `logistics`       | Shipments, delivery, tracking       |
| `education`       | Students, courses, grades           |
| `real_estate`     | Listings, prices, locations         |
| `retail`          | Sales, products, inventory          |
| `insurance`       | Policies, claims, customers         |
| `human_resources` | Employees, roles, salaries          |
| `travel`          | Bookings, destinations, dates       |

> 💡 More datasets will be added regularly. Our goal: **1,000+ industry-specific datasets**.

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

## 🧩 Extending with Custom Datasets

Want to create your own dataset module?

```python
# DataForge/datasets/mydataset.py

def generate(count: int):
    # Return a pandas DataFrame with your custom logic
```

Then register it in `generator.py`. Full contribution guide: [CONTRIBUTING.md](CONTRIBUTING.md)

---

## 🤝 Contributing

We welcome contributions! If you have a new dataset idea or feature, check out:

📄 [CONTRIBUTING.md](CONTRIBUTING.md)

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🧠 Future Plans

- [x] 10+ starter datasets
- [ ] 1,000+ total industry-specific datasets
- [ ] Custom schema generation (YAML/JSON)
- [ ] Web app and Streamlit UI
- [ ] API access for integrations

---

## 🌐 Links

- 📦 PyPI: [https://pypi.org/project/DataForge](https://pypi.org/project/DataForge)
- 🧑‍💻 GitHub: [https://github.com/your-org/DataForge](https://github.com/your-org/DataForge)
- 📘 Docs: Coming soon

---

> Created with ❤️ by [Ravender Singh Rana / BI Learner]
