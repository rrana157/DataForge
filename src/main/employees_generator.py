import pandas as pd
from resources.config import *
from src.common_functions.fake_dates import *
from src.attributes import load_files


class EmployeesGenerator:
    def __init__(self, people_data, job_data, num: int = 10000):
        """
        :type people_data: common data
        :type num: number of records (maximum number of records is set to 10000)
        """
        self.num = num
        self.people_data = people_data
        self.job_data = job_data

    @property
    def employees(self) -> object:
        employees = []
        for i in range(self.num):
            employee_id = abs((self.num - random.randint(4792, 5847)) + i)
            start_date, exit_date = generate_employment_dates(min_years_ago=10, max_years_ago=1)
            person = random.choice(self.people_data)
            job_data = random.choice(self.job_data)
            dob = date_between('-59y', '-19y')
            dob_str = dob.strftime('%Y-%m-%d') if dob else None

            employees.append(
                {'employee_id': employee_id, 'first_name': person['First Name'], 'last_name': person['Last Name'],
                 'start_date': start_date.strftime('%Y-%m-%d') if start_date else None,
                 'exit_date': exit_date.strftime('%Y-%m-%d') if exit_date else None, 'date_of_birth': dob_str,
                 'gender': random.choice(genders), 'employment_type': random.choice(employment_type),
                 'salary': f"${random.randint(55, 65)}K-${random.randint(80, 130)}K",
                 'email': f"{person['First Name'].lower()}.{person['Last Name'].lower()}@company.com",
                 'phone': person['Phone'], 'department': random.choice(departments), 'job_title': job_data['Job Title'],
                 'qualifications': random.choice(qualifications), 'vacancy_type': random.choice(vacancy_type),
                 'benefits_list': random.choice(benefits_list), 'address': person['Address'], 'city': person['City'],
                 'state': person['State'], 'country': person['Country'], 'source': random.choice(joining_source)})

        return pd.DataFrame(employees)


def generate_employee(num: int):
    people = load_files.load_files_data('fake_person_profiles.json')
    job_data = load_files.load_files_data('job_title.json')
    generator = EmployeesGenerator(people_data=people, job_data=job_data, num=num)
    return generator.employees

