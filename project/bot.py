from tweet import *
from get_data import *
from make_chart import *

dataset = get_data()
chart = make_chart(dataset["data"])
response = upload_image(chart, dataset["description"], dataset["title"])
# print(response)