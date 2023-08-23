import json

# Create the dictionary object
data = {
    "annotations": [
        {
            "result": []
        }
    ],
    "data": {
        "image": "D:/eman/internship/image1.jpg"
    }
}

# Open the text file
with open('D:/eman/internship/image1.txt', 'r') as txtfile:
    # Read all lines from the file
    lines = txtfile.readlines()
    for line in lines:
        # Extract line
        line = line.strip()

        # Split the line into individual values
        values = line.split()

        # Create a dictionary object for each value
        annotation = {
            "image_rotation": int(values[0]),
            "value": {
                "x": float(values[1]),
                "y": float(values[2]),
                "width": float(values[3]),
                "height": float(values[4]),
                "rotation": int(values[0]),
                "rectanglelabels": ["object"]
            }
        }

        # Append the annotation to the "result" list in the data dictionary
        data["annotations"][0]["result"].append(annotation)

# Convert the dictionary to JSON
json_data = json.dumps(data, indent=4)

# Write the JSON data to the output file
with open('D:/eman/internship/output.json', 'w') as file:
    file.write(json_data)