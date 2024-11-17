# BMI Calculator that automatically detects
# measurement system (Imperial or Metric)
import re
import collections

KILOS_PER_POUND = 0.453592
METERS_PER_INCH = 0.0254
HEIGHT_PROMPT = "Enter your height: "
WEIGHT_PROMPT = "Enter your weight: "

metric_weight_pattern = re.compile(r"^(\d+(\.\d+)?\s*kgs?)$")
imperial_weight_pattern = re.compile(r"^(\d+\s*lbs?)$")

metric_height_pattern = re.compile(r"^(\d+(\.\d+)?\s*m)$")
imperial_height_pattern = re.compile(r"^(\d+\s*ft(\s+\d+\s*in)?)$")

weight_patterns = [metric_weight_pattern, imperial_weight_pattern]
height_patterns = [metric_height_pattern, imperial_height_pattern]

prompts = {WEIGHT_PROMPT: weight_patterns,
           HEIGHT_PROMPT: height_patterns}

UserMeasurements = collections.namedtuple("UserMeasurements", ["weight", "height"])


def get_user_input():
    user_data = []
    for prompt, patterns in prompts.items():
        response = input(prompt).lower()
        if not response:
            print("No input. Application terminated.")
            break
        for pattern in patterns:
            match = pattern.match(response)
            if match:
                # print(match.groups())
                user_data.append(match.groups())
                break
        if not match:
            return
    return user_data

def get_metric_values(user_data):
    # Each element of user_data is a tuple. Except for imperial height, first
    # element of tuple contains the measurement needed.
    # For imperial height, first element will be either Xft or Xft Yin (feet and inches)
    # user_data[0] will contain the weight either in metric or imperial units
    # user_data[1] will contain the height either in metric or imperial units
    # Convert to metric if "ft" or "lb(s)" detected in a measurement
    
    non_numerics_pattern = r"[ a-z]"

    weight = user_data[0][0]
    # Get numeric equivalent of string representations of measurement
    # Same process regardless of measurement system. Later on any conversion
    # between systems will be determined
    numeric_weight = float(re.sub(non_numerics_pattern,"", weight))

    height = user_data[1][0]
    if "ft" in height and "in" in height:
        # Split on spaces. ft value will be in first element
        # in value will be in last element
        height_values = height.split(" ")
        feet = height_values[0]
        inches = height_values[-1]
        # Get numeric equivalents of string representations of measurements
        feet = float(re.sub(non_numerics_pattern, "", feet))
        inches = float(re.sub(non_numerics_pattern, "", inches))
        numeric_height = feet * 12 + inches
    elif "ft" in height:
        feet = float(re.sub(non_numerics_pattern, "", height))
        numeric_height = feet * 12
    elif "m" in height:
        # Measurement already in metric
        numeric_height = float(re.sub(non_numerics_pattern, "", height)) 
    
    
    # Convert Imperial to Metric if necessary
    weight = numeric_weight * KILOS_PER_POUND \
             if "lb" in weight else numeric_weight

    height = numeric_height * METERS_PER_INCH \
             if "ft" in height else numeric_height
    
    return UserMeasurements(weight = weight, height = height)
    
    
def calc_bmi():
    print("Welcome to the BMI Calculator Application!")
    user_data = get_user_input()
    if not user_data:
        print("Invalid input(s). Application terminated.")
        return
    
    metric_values = get_metric_values(user_data)
    bmi = metric_values.weight / metric_values.height ** 2
    print(f"metric_values.weight: {metric_values.weight}, metric_values.height: {metric_values.height}")
    bmi = int(round(bmi, 0))
    print(f"Your BMI is {bmi}")
    
    
    
    
calc_bmi()    
    
