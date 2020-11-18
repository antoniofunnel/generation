import sys, json

#{"averageOrderAmountV2":null,"createdAt":"2020-04-11T09:59:38Z","firstName":"Giles","email":"hello@sculpd.co.uk","displayName":"Giles Harrison","id":"gid:\/\/shopify\/Customer\/3090485018729","locale":"en","ordersCount":"0","totalSpentV2":{"amount":"0.0","currencyCode":"GBP"},"updatedAt":"2020-06-25T07:15:15Z","state":"DISABLED","tags":["newsletter"]}

def jsonl_reader(file_name):
    json_rows = []
    for row in open(file_name, "r"):
        json_rows.append(json.loads(row))
    return json_rows

def parse(json_rows):
    pass

json_rows = jsonl_reader("large_file.jsonl")

rows = parse(json_rows)


print(f"The type of the json_rows is: {type(json_rows)}")
print(f"The size of the json_rows is: {sys.getsizeof(json_rows)}")
print(f"The type of the rows is: {type(rows)}")
print(f"The size of the rows is: {sys.getsizeof(rows)}")
