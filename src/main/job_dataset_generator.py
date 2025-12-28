import random
import pandas as pd
from resources.config import *
from src.attributes import load_files
from src.common_functions.fake_dates import *


class JobsDatasetGenerator:
    def __init__(self, people_data, job_data, cities_data, companies_data, num: int = 10000):
        self.num = num
        self.job_data = job_data
        self.companies_data = companies_data
        self.people_data = people_data
        self.cities_data = cities_data

    @staticmethod
    def generate_experience():
        return random.randint(*random.choice([
            (1, 3),
            (2, 5),
            (4, 8),
            (7, 12),
            (10, 20)
        ]))

    @staticmethod
    def generate_salary(experience):
        if experience <= 2:
            return f"${random.randint(30, 45)}K-${random.randint(45, 60)}K"
        elif experience <= 5:
            return f"${random.randint(45, 65)}K-${random.randint(65, 85)}K"
        elif experience <= 8:
            return f"${random.randint(65, 85)}K-${random.randint(85, 110)}K"
        elif experience <= 12:
            return f"${random.randint(85, 110)}K-${random.randint(110, 140)}K"
        else:
            return f"${random.randint(110, 140)}K-${random.randint(140, 180)}K"

    @property
    def jobs(self) -> object:
        jobs_dataset = []

        for i in range(self.num):
            job_id = abs((self.num - random.randint(4792, 5847)) + i)
            job_date, _ = generate_employment_dates(min_years_ago=2, max_years_ago=1)

            person = random.choice(self.people_data)
            company = random.choice(self.companies_data)
            job = random.choice(self.job_data)
            city = random.choice(self.cities_data)
            emp_type = random.choice(employment_type)

            experience = (
                self.generate_experience()
                if emp_type not in ('Intern', 'Intern(Paid)')
                else None
            )

            salary_range = (
                self.generate_salary(experience)
                if experience is not None
                else None
            )

            jobs_dataset.append(
                dict(job_id=job_id, experience=experience, qualifications=job['Degree'], salary_range=salary_range,
                     location=f"{city['City']}, {city['State']}", country=city['Country'], region=city['Region'],
                     latitude=city['Latitude'], longitude=city['Longitude'], work_type=emp_type,
                     job_posting_date=job_date.strftime('%Y-%m-%d') if job_date else None,
                     preference=random.choice(["Both", "Male", "Female"]),
                     contact_person=f"{person['Last Name']}, {person['First Name']}", contact=person['Phone'],
                     job_title=job['Job Title'], role=job['Role'], job_portal=random.choice(joining_source),
                     job_description=job['job_description'], benefits=random.choice(benefits_list),
                     skills=job['Skills'],
                     responsibilities=job['Responsibilities'], company_name=company['Company'],
                     company_profile=company['Company Profile']))

        return pd.DataFrame(jobs_dataset)


def generate_job_dataset(num: int):
    people = load_files.load_files_data('fake_person_profiles.json')
    job_data = load_files.load_files_data('job_title.json')
    companies_data = load_files.load_files_data('companies.json')
    cities_data = load_files.load_files_data('world_cities.json')

    generator = JobsDatasetGenerator(people_data=people,
                                     job_data=job_data,
                                     cities_data=cities_data,
                                     companies_data=companies_data,
                                     num=num)

    return generator.jobs
