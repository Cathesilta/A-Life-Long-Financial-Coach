import time
from datetime import datetime

birth_year = 2000

annual_inflation_rate = 2/100
number_of_year = 11
future_value = 5800


if __name__ == "__main__":
    
    current_year = datetime.now().year
    
    inflation_factor=(1+annual_inflation_rate)**number_of_year
    current_value = future_value//inflation_factor
    
    print(f"After {number_of_year} years, which is {number_of_year+current_year}. "
          f"Your age will be {number_of_year+current_year-birth_year}. \n"
          f"At that time, {future_value} was equivalent to {current_value} today. ")
    
    