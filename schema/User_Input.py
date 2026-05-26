
from pydantic import BaseModel,Field,computed_field
from typing import Optional,Literal,Annotated


class UserInput(BaseModel):
    age:Annotated[int,Field(...,description="Enter Age here ")]
    weight:Annotated[float,Field(...,gt=0,description='Weight in Kgs')]
    height:Annotated[float,Field(...,gt=0,description='Enter height in Meters')]
    occupation:Annotated[Literal
    [     'Factory Worker',         'Businessman',       'Sales Manager',
              'Banker',   'Marketing Manager',     'Insurance Agent',
          'HR Manager',          'Pharmacist',             'Teacher',
   'Software Engineer',          'Consultant',              'Driver',
          'Shop Owner',               'Nurse',          'Accountant',
 'Government Employee',           'Architect',            'Engineer',
   'Real Estate Agent',       'Civil Servant',             'Plumber',
      'Retail Manager',                'Chef',         'Electrician',
           'Carpenter',              'Doctor',      'Lab Technician',
        'Data Analyst',              'Lawyer',      'Content Writer'],Field(...,description="What is your Occupation",examples=['Businessman','Banker'])]
    income_lpa:Annotated[float,Field(...,description="What is your income in Lakhs per annum",examples=[12.5,3.2])]
    smoker:Annotated[bool,Field(...,description="Does the user Smoke True or False Only")]

    city:Annotated[str,Field(...,description='Enter the city of user')]
    
    @computed_field
    @property
    def bmi(self)->float:
        return self.weight/(self.height**2)
    
    @computed_field
    @property
    def lifestyle_risk(self)->str:
        if self.smoker and self.bmi > 30:
            return "High"
        elif self.smoker or self.bmi > 27:
            return "Medium"

        return "Low"
    
    @computed_field
    @property
    def age_group(self)->str:
        if self.age<25:
            return "Young"
        elif self.age<30:
            return "Adult"
        elif self.age<60:
            return "Middle_aged"
        return "Senior"
    
    @computed_field
    @property
    def city_tier(self)->int:
        if self.city in tier_1_cities:
            return 1 
        elif self.city in tier_2_cities:
            return 2 
        else:
            return 3