import re

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

def removehtmlstyling(file_old_path, file_new_path):
    new_csv_data = ""
    with open(file_old_path, encoding="utf8") as f:
        for data in f:
            new_csv_data += cleanhtml(data)
    with open(file_new_path, "w+", encoding="utf8") as f:
        f.write(new_csv_data)           

file_old_path = r'<file_path>'
file_new_path = r'<file_path>'
removehtmlstyling(file_old_path, file_new_path)