import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Function to generate random date within a range
def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + timedelta(seconds=random_second)

# Set the seed for reproducibility (optional)
np.random.seed(42)
random.seed(42)

# Define sample data with African focus
last_names = [
    # West African surnames
    'Adebayo', 'Okafor', 'Nkosi', 'Mensah', 'Osei', 'Ibrahim', 'Mohammed', 'Diallo', 'Keita', 'Toure',
    'Afolabi', 'Kofi', 'Ndongo', 'Kone', 'Sankara', 'Okonkwo', 'Nwosu', 'Oluwole', 'Adeyemi', 'Abara',
    # East African surnames
    'Wangai', 'Kimani', 'Odhiambo', 'Gebre', 'Mulatu', 'Kibet', 'Hassan', 'Ahmed', 'Abdi', 'Senghor',
    # North African surnames
    'El-Masri', 'Khalil', 'Bensouda', 'Amara', 'Youssef', 'Abbas', 'Ben Ali', 'Al-Fassi', 'Tadesse', 'Haile',
    # Southern African surnames
    'Mokoena', 'Ndlovu', 'Dlamini', 'Mandela', 'Moyo', 'Mutasa', 'Banda', 'Mwangi', 'Chirwa', 'Phiri',
    # Central African surnames
    'Bongo', 'Kabila', 'Mobutu', 'Bokassa', 'Nguesso', 'Touadéra', 'Biya', 'Bemba', 'Tshisekedi', 'Bemba'
]

first_initials = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

ethnic_groups = [
    # Major ethnic groups across different African regions
    'Yoruba', 'Igbo', 'Hausa', 'Akan', 'Fulani', 'Kikuyu', 'Amhara', 'Oromo', 'Zulu', 'Xhosa',
    'Berber', 'Arab', 'Tigray', 'Shona', 'Maasai', 'Luba', 'Lunda', 'Kongo', 'Mandinka', 'Wolof',
    'Somali', 'Swahili', 'Tswana', 'Sotho', 'Ndebele', 'Hutu', 'Tutsi', 'Afar', 'Mixed Heritage'
]

departments = [
    'General Medicine', 'General Surgery', 'Maternal Health', 'Child Health', 'Infectious Disease',
    'HIV/AIDS Treatment', 'Tuberculosis Clinic', 'Malaria Unit', 'Emergency', 'Outpatient Services',
    'Community Medicine', 'Mental Health', 'Nutrition', 'Tropical Disease', 'Immunization',
    'Radiology', 'Pharmacy', 'Laboratory', 'Public Health', 'Family Planning'
]

# Number of rows to generate
num_rows = 9217

# Define date range
start_date = datetime(2023, 1, 2)
end_date = datetime(2025, 4, 30)

# Create empty dataframe
df = pd.DataFrame()

# Generate Patient IDs
df['Patient ID'] = ['PT' + str(i).zfill(6) for i in range(1, num_rows + 1)]

# Generate random admission dates
admission_dates = []
for _ in range(num_rows):
    rand_date = random_date(start_date, end_date)
    admission_dates.append(rand_date.strftime('%d-%m-%Y %H:%M'))
df['Patient Admission Date'] = admission_dates

# Generate random first initials
df['Patient First Initial'] = np.random.choice(first_initials, num_rows)

# Generate random last names
df['Patient Last Name'] = np.random.choice(last_names, num_rows)

# Generate random genders
df['Patient Gender'] = np.random.choice(['M', 'F'], num_rows)

# Generate random ages
df['Patient Age'] = np.random.randint(1, 80, num_rows)

# Generate random races/ethnicities
df['Patient Race'] = np.random.choice(ethnic_groups, num_rows)

# Generate random departments
df['Department Referral'] = np.random.choice(departments, num_rows)

# Generate random admission flags
df['Patient Admission Flag'] = np.random.choice(['True', 'False'], num_rows, p=[0.7, 0.3])

# Generate random satisfaction scores
df['Patient Satisfaction Score'] = np.random.randint(1, 10, num_rows)

# Generate random wait times
df['Patient Wait Time'] = np.random.randint(10, 60, num_rows)

# Generate random CM values (0 or 1)
df['Patients CM'] = np.random.choice([0, 1], num_rows)

# Preview the first few rows
print(df.head())

# Save to CSV file
df.to_csv('african_patient_dataa.csv', index=False)

print(f"Dataset with {num_rows} rows successfully generated and saved as 'african_patient_dataa.csv'")