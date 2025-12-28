# Static data pools


genders = ["Male", "Female", "Others"]

vacancy_type = ["New", "Replacement"]

employment_type = ["Full-Time", "Part-Time", "Temporary", "Contract", "Intern", "Intern(Paid)"]

qualifications = ["B.Tech", "M.Tech", "MCA", "BCA", "PhD", "BA", "MBA", "BBA", "B.Com", "M.Com"]

joining_source = [
    'Indeed', 'LinkedIn', 'Glassdoor', 'Monster', 'CareerBuilder', 'SimplyHired', 'ZipRecruiter', 'Dice', 'Idealist',
    'USAJOBS', 'Snagajob', 'The Muse', 'FlexJobs', 'Internships.com', 'Jobs2Careers', 'Stack Overflow Jobs',
    'SimplyHired', 'Idealist', 'USAJOBS', 'Snagajob', 'The Muse', 'FlexJobs', 'Internships.com', 'Jobs2Careers',
    'Stack Overflow Jobs'
]

departments = [
    "Engineering", "Human Resources (HR)", "Marketing", "Finance", "Sales", "Customer Service", "Operations",
    "Research & Development (R&D)", "Information Technology (IT)", "Legal", "Product Management",
    "Quality Assurance (QA)", "Procurement / Purchasing", "Supply Chain / Logistics", "Administration",
    "Business Development", "Compliance", "Training and Development", "Public Relations (PR)",
    "Health and Safety", "Facilities Management"
]


benefits_list = [
    ["Health Insurance, Retirement Plans, Paid Time Off (PTO), Flexible Work Arrangements, Employee Assistance Programs (EAP)"],
    ["Tuition Reimbursement, Stock Options or Equity Grants, Parental Leave, Wellness Programs, Childcare Assistance"],
    ["Transportation Benefits, Professional Development, Bonuses and Incentive Programs, Profit-Sharing, Employee Discounts"],
    ["Flexible Spending Accounts (FSAs), Relocation Assistance, Legal Assistance, Employee Recognition Programs, Financial Counseling"],
    ["Casual Dress Code, Social and Recreational Activities, Employee Referral Programs, Health and Wellness Facilities, Life and Disability Insurance"],
    ["Employee Assistance Programs (EAP), Tuition Reimbursement, Profit-Sharing, Transportation Benefits, Parental Leave"],
    ["Legal Assistance, Bonuses and Incentive Programs, Wellness Programs, Employee Discounts, Retirement Plans"],
    ["Employee Referral Programs, Financial Counseling, Health and Wellness Facilities, Casual Dress Code, Flexible Spending Accounts (FSAs)"],
    ["Childcare Assistance, Paid Time Off (PTO), Relocation Assistance, Flexible Work Arrangements, Professional Development"],
    ["Life and Disability Insurance, Stock Options or Equity Grants, Employee Recognition Programs, Health Insurance, Social and Recreational Activities"],
    ["Health Insurance, Retirement Plans, Flexible Work Arrangements, Employee Assistance Programs (EAP), Bonuses and Incentive Programs"],
    ["Tuition Reimbursement, Stock Options or Equity Grants, Parental Leave, Wellness Programs, Childcare Assistance"],
    ["Transportation Benefits, Professional Development, Bonuses and Incentive Programs, Profit-Sharing, Employee Discounts"],
    ["Flexible Spending Accounts (FSAs), Relocation Assistance, Legal Assistance, Employee Recognition Programs, Financial Counseling"],
    ["Casual Dress Code, Social and Recreational Activities, Employee Referral Programs, Health and Wellness Facilities, Life and Disability Insurance"],
    ["Employee Assistance Programs (EAP), Tuition Reimbursement, Profit-Sharing, Transportation Benefits, Parental Leave"],
    ["Legal Assistance, Bonuses and Incentive Programs, Wellness Programs, Employee Discounts, Retirement Plans"],
    ["Employee Referral Programs, Financial Counseling, Health and Wellness Facilities, Casual Dress Code, Flexible Spending Accounts (FSAs)"],
    ["Childcare Assistance, Paid Time Off (PTO), Relocation Assistance, Flexible Work Arrangements, Professional Development"],
    ["Life and Disability Insurance, Stock Options or Equity Grants, Employee Recognition Programs, Health Insurance, Social and Recreational Activities"]
]


# Constants
risk_surcharge = ['Owner', 'Carrier']

mode = ['Surface', 'Air Cargo', 'Express']

nature_of_consignment = ['Dox', 'Non-Dox']

mode_of_payment = ['Cash', 'Card', 'Wallet']

value_added_weights = {
    'Insurance': 0.1,
    'COD': 0.6,
    'Express': 0.1,
    'None': 0.2
}

city_state_pairs = [
    ("Mumbai", "Maharashtra"), ("Delhi", "Delhi"), ("Bangalore", "Karnataka"),
    ("Chennai", "Tamil Nadu"), ("Hyderabad", "Telangana"), ("Kolkata", "West Bengal"),
    ("Ahmedabad", "Gujarat"), ("Pune", "Maharashtra"), ("Jaipur", "Rajasthan"),
    ("Lucknow", "Uttar Pradesh"), ("Surat", "Gujarat"), ("Nagpur", "Maharashtra"),
    ("Bhopal", "Madhya Pradesh"), ("Indore", "Madhya Pradesh"), ("Patna", "Bihar"),
    ("Ranchi", "Jharkhand"), ("Guwahati", "Assam"), ("Chandigarh", "Chandigarh"),
    ("Coimbatore", "Tamil Nadu"), ("Thiruvananthapuram", "Kerala"), ("Kochi", "Kerala"),
    ("Vizag", "Andhra Pradesh"), ("Vijayawada", "Andhra Pradesh"), ("Amritsar", "Punjab"),
    ("Ludhiana", "Punjab"), ("Agra", "Uttar Pradesh"), ("Meerut", "Uttar Pradesh"),
    ("Varanasi", "Uttar Pradesh"), ("Nashik", "Maharashtra"), ("Aurangabad", "Maharashtra"),
    ("Raipur", "Chhattisgarh"), ("Bhubaneswar", "Odisha"), ("Jamshedpur", "Jharkhand"),
    ("Dehradun", "Uttarakhand"), ("Shimla", "Himachal Pradesh"), ("Srinagar", "Jammu & Kashmir")
]

couries_columns = [
    "Origin", "Destination", "Pouch No", "Date", "Sender's Name", "Sender Phone",
    "Sender Address", "Sender City", "Sender State", "Sender Pincode", "Sender GSTIN",
    "Total Pieces", "Actual Wt", "Volumetric Wt", "Chargeable Wt", "Paperwork",
    "Sender Signature", "Sender Date", "Recipient Name", "Recipient Phone",
    "Recipient Address", "Recipient City", "Receiver State", "Receiver Pincode",
    "Description", "Value Added Services", "Consignment No", "Expiry Date",
    "Booking Code", "Recipient GSTIN", "Receiver Name", "Relationship",
    "Company Stamp", "Receiver Signature", "Receive Date", "Tariff",
    "VAS Charges", "Total Amount", "Mode", "Risk Surcharge", "Mode of Payment",
    "Nature of Consignment"
]
