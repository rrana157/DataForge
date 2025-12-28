import pandas as pd
from resources.config import *
from src.attributes import load_files
from src.common_functions.fake_dates import *


class HealthcareGenerator:
    def __init__(self, people_data, cities_data, companies_data, num: int = 10000):
        self.num = num
        self.companies_data = companies_data
        self.people_data = people_data
        self.cities_data = cities_data

    def healthcare(self) -> object:

        healthcare_dataset = []

        for i in range(self.num):
            patient_id = abs((self.num - random.randint(4792, 5847)) + i)
            appointment_date, _ = generate_employment_dates(min_years_ago=2, max_years_ago=1)

            person = random.choice(self.people_data)
            company = random.choice(self.companies_data)
            city = random.choice(self.cities_data)

            healthcare_dataset.append(
                dict(patient_id=patient_id, first_name=person['First Name'], last_name=person['Last Name'], blood_type=None,
                     medical_condition=None,doctor=None,hospital=None,insurance=None,billing_amount=None,admission_type=None,
                     discharge_date=None,medication=None,test_results=None,
                     location=f"{city['City']}, {city['State']}", country=city['Country'], region=city['Region'],
                     latitude=city['Latitude'], longitude=city['Longitude'], work_type=emp_type,
                     job_posting_date=appointment_date.strftime('%Y-%m-%d') if appointment_date else None,
                     patient_gender=random.choice(["Both", "Male", "Female"])))

        return pd.DataFrame(healthcare_dataset)


def generate_healthcare(num: int):
    people = load_files.load_files_data('fake_person_profiles.json')
    companies_data = load_files.load_files_data('companies.json')
    cities_data = load_files.load_files_data('world_cities.json')

    generator = HealthcareGenerator(people_data=people,
                                    cities_data=cities_data,
                                    companies_data=companies_data,
                                    num=num)

    return generator.healthcare
