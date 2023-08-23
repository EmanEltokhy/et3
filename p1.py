import os
import shutil
import csv
import datetime

def extract_images(source_folder, destination_folder, report_file):
    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Open the CSV file for writing the report
    with open(report_file, 'w', newline='') as csvfile:
        fieldnames = ['Image Name', 'Image Size', 'Last Modification Date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Traverse all folders and sub-folders
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                # Check if the file is an image
                if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                    source_file = os.path.join(root, file)

                    # Copy the image to the destination folder
                    destination_file = os.path.join(destination_folder, file)
                    shutil.copy2(source_file, destination_file)

                    # Get image information
                    image_size = os.path.getsize(source_file)/1024
                    modification_date = os.path.getmtime(source_file)
                    modification_date = datetime.datetime.fromtimestamp(modification_date).strftime('%a %B %d %H:%M:%S %Y')

                    # Remove the prefix from the image name
                    image_name = file.split('-', 1)[-1]

                    # Write the information to the CSV file
                    writer.writerow({'Image Name': image_name, 'Image Size': f'{image_size.__round__(1)} KB', 'Last Modification Date': modification_date})


# if __name__ == '__main__':
extract_images('D:/eman/internship/dairies', 'D:/eman/internship/dataset', 'D:/eman/internship/report.csv')
