import json
with open('intents.json', 'r') as object_1:
    data = json.load(object_1)
print("Data in the json file is loaded:")
print(data)
#this is the example of recursive function
def strip_recursive(x):
    if isinstance(x, str):
        # Function of Strip Function
        # strip function is used to remove both the leading and trailing white spaces from the string
        # if no parameter is passed then only leading and trailing white spaces are removed
        return x.strip()
    elif isinstance(x, list):
        return [strip_recursive(v) for v in x]
    elif isinstance(x, dict):
        return dict ((strip_recursive(a), strip_recursive(b))for (a, b) in x.items())
    return x
#Calling function
output = strip_recursive(data)
#this is the filtered output
print("\n")
print("Filtered output after recursive operation on Data:")
print(output)
#Saving the new file

with open('output.json', 'w') as fp:
    json.dump(output, fp, indent=4, sort_keys=True)
