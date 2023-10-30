#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

# Load the Excel file into a DataFrame
df = pd.read_excel('student_details_nm.xlsx')

# Print column names
print(df.columns)


# In[3]:


# Replace 'your_exact_column_name' with the actual column name from the printed output
register_column_name = 'Register_number'


# In[7]:


import pandas as pd

# Function to retrieve student details from Excel
def retrieve_student_details(register_number):
    # Load the Excel file into a DataFrame
    df = pd.read_excel('student_details_nm.xlsx')

    # Print column names
    print(df.columns)

    # Replace 'your_exact_column_name' with the actual column name from the printed output
    register_column_name = 'Register_number'

    # Search for the student with the provided register number (case-insensitive)
    student_details = df[df[register_column_name].astype(str).str.upper() == register_number.upper()]

    # Return the details as a dictionary (or None if not found)
    return student_details.to_dict(orient='records')[0] if not student_details.empty else None

# Example Usage:
if __name__ == "__main__":
    # User input: Register number
    Register_number = input("Enter student's register number: ")

    # Retrieve student details
    student_details = retrieve_student_details(Register_number)

    if student_details:
        print("\nStudent Details:")
        for key, value in student_details.items():
            print(f"{key}: {value}")
    else:
        print(f"\nStudent with register number {Register_number} not found.")


# In[ ]:




