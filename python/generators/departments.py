import pandas as pd

from config import RAW_DATA
from utils.constants import (
    DEPARTMENTS,
    DEPARTMENT_CODES,
    BUILDINGS
)

def generate_departments():

    departments = []

    for i in range(len(DEPARTMENTS)):
        departments.append({
            "department_id": i + 1,
            "department_name": DEPARTMENTS[i],
            "department_code": DEPARTMENT_CODES[i],
            "building": BUILDINGS[i]
        })

    df = pd.DataFrame(departments)

    output_file = RAW_DATA / "departments.csv"

    df.to_csv(output_file, index=False)

    print("Departments Generated Successfully")

    return df