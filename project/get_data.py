from urllib.request import urlopen
import json

def get_data():
    dataset = {}

    url = "https://www.govtrack.us/api/v2/bill?order_by=-current_status_date"
    response = urlopen(url)
    data_json = json.loads(response.read())

    introduced_count = 0
    pass_over_house_count = 0
    passed_bill_count = 0
    passed_concurrentres_count = 0
    passed_simpleres_count = 0
    reported_count = 0
    enacted_signed_count = 0

    for bill in data_json["objects"]:
        if (bill["current_status"] == "introduced"):
            introduced_count += 1
        elif (bill["current_status"] == "pass_over_house"):
            pass_over_house_count += 1
        elif (bill["current_status"] == "passed_bill"):
            passed_bill_count += 1
        elif (bill["current_status"] == "passed_concurrentres"):
            passed_concurrentres_count += 1
        elif (bill["current_status"] == "passed_simpleres"):
            passed_simpleres_count += 1
        elif (bill["current_status"] == "reported"):
            reported_count += 1
        elif (bill["current_status"] == "enacted_signed"):
            enacted_signed_count += 1

    dataset["data"] = {
        'Introduced': introduced_count,
        'Passed House': pass_over_house_count,
        'Passed House & Senate': passed_bill_count,
        'Concurrent Resolution': passed_concurrentres_count,
        'Simple Resolution': passed_simpleres_count,
        'Ordered Reported': reported_count,
        'Enacted': enacted_signed_count,
    }
    dataset["title"] = "Analyzing the last 100 bills introduced in the US congress"

    data = dataset["data"]
    dataset["description"] = "\n".join([f"{x}: {list(data.values())[ind]}" for ind, x in enumerate(list(data.keys()))])

    return dataset
