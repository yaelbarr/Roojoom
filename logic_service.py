from collections import Counter
def calculate_response(data : dict):
    try:
        problem_description = data["problem_description"]
        serial_number = data["serial_number"]
        light_indi1 = data["light_indicator1"]
        light_indi2 = data["light_indicator2"]
        light_indi3 = data["light_indicator3"]
    except KeyError:
        return "Input is invalid"
    
    if (len(data) > 5):
        return "Input is invalid"
    
    input_errors = []
    
    #check input requirments
    if len(problem_description) > 300:
        input_errors.append("Cannot accept problem description longer than 300 characters")
    if isinstance(serial_number, str):
        if len(serial_number) != 64:
            input_errors.append("Serial number should consist of 64 characters exactly, please check")
    
    #which lights' input is invalid
    invalid_lights = [f"light {i+1}" for i, status in enumerate([light_indi1, light_indi2, light_indi3]) if status not in {"on", "off", "blinking"}]

    if invalid_lights:
        if len(invalid_lights) == 1:
             input_errors.append(f"The status of {invalid_lights[0]} is invalid")
        else:
            st = " and ".join(invalid_lights)
            input_errors.append(f"The status of {st} is invalid")

    #returns all input errors.
    if input_errors:
        return " and ".join(input_errors)

    count_indications = Counter([light_indi1, light_indi2, light_indi3])

    if isinstance(serial_number, (int, float)):
        return "Bad serial number"
    if serial_number[:4] == "24-X":
        return "Please upgrade your device"
    if serial_number[:4] == "36-X":
        if count_indications["off"] == 3:
            return "Turn on the device"
        if count_indications["blinking"] == 2:
            return "Please wait"
        if count_indications["on"] == 3:
            return "ALL is ok"
        else:
            return "Cannot assist at this moment"
    if serial_number[:4] == "51-B":
        if count_indications["off"] == 3:
            return "Turn on the device"
        if count_indications["blinking"] >= 1:
            return "Please wait"
        if count_indications["on"] > 1:
            return "ALL is ok"
        else:
            return "Cannot assist at this moment"
    else:
        return "Unknown device"
        
 

