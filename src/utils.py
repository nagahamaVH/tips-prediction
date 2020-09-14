import pandas as pd

def transform_day(input_day):
    if input_day == "Quinta-feira":
        return "Thur"
    if input_day == "Sexta-feira":
        return "Fri"
    if input_day == "Sábado":
        return "Sat"
    else:
        return "Sun"


def transform_input(input_day, input_time, input_sex, input_smoker):
    day = transform_day(input_day)
    time = "Lunch" if input_time == "Almoço" else "Dinner"
    sex = "Male" if input_sex == "Masculino" else "Female"
    smoker = "Yes" if input_smoker else "No"

    return day, time, sex, smoker


def struct_input(bill, sex, smoker, day, time, group):
    day, time, sex, smoker = transform_input(day, time, sex, smoker)

    data = pd.DataFrame({
        "total_bill": [bill],
        "size_of_group": [group],
        "sex_Male": [1 if sex == "Male" else 0],
        "smoker_Yes": [1 if smoker == "Yes" else 0],
        "day_Sat": [1 if day == "Sat" else 0],
        "day_Sun": [1 if day == "Sun" else 0],
        "day_Thur": [1 if day == "Thur" else 0],
        "time_Lunch": [1 if day == "Lunch" else 0]})

    return data