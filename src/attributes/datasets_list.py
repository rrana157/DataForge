from src.main.airlines_generator import airlines_generator
from src.main.couriers_generator import CouriersGenerator
from src.main.industrial_pump_generator import industrial_pump_generator
from src.main.retailsales_generator import generate_retailsales
from src.main.healthcare_generator import generate_healthcare
from src.main.employees_generator import generate_employee
from src.main.job_dataset_generator import generate_job_dataset


def normalize_name(name: str) -> str:
    return name.replace(" ", "").replace("_", "").lower()


_RAW_DATASETS = {
    # "Airline": generate_airlines,
    "Courier": CouriersGenerator,
    "Healthcare": generate_healthcare,
    "Job Dataset": generate_job_dataset,
    "Employee Dataset": generate_employee,
    # "Petrol Pump": generate_industrialpump,
    "Retail Sales": generate_retailsales
}

# Normalized registry
DATASETS = {normalize_name(k): v for k, v in _RAW_DATASETS.items()}


def available_datasets():
    return list(_RAW_DATASETS.keys())
