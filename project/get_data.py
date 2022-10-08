import json
from urllib.request import urlopen

def get_data():
    url = "https://www.govtrack.us/api/v2/bill?order_by=-current_status_date" 
    response = urlopen(url) 
    data_json = json.loads(response.read())

    statuses = [item["current_status"] for item in data_json["objects"]]

    dataset = {} 
    dataset["data"] = { 
        "Introduced": statuses.count("introduced"), 
        "Passed House": statuses.count("pass_over_house"), 
        "Passed House & Senate": statuses.count("passed_bill"), 
        "Concurrent Resolution": statuses.count("passed_concurrentres"),
        "Simple Resolution": statuses.count("passed_simpleres"), 
        "Ordered Reported": statuses.count("reported"), 
        "Enacted": statuses.count("enacted_signed"), 
    }
    dataset["title"] = "Analyzing the last 100 bills introduced in the US congress"
    data = dataset["data"]
    dataset["description"] = "\n".join([f"{x}: {list(data.values())[ind]}" for ind, x in enumerate(list(data.keys()))])

    return dataset
