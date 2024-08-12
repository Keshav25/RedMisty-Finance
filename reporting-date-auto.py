import os
import datetime

folder_path = r"D:\\accounting\"

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)

# if weekend, get friday
if yesterday.weekday() >= 5:
    new_date = yesterday - datetime.timedelta(days=yesterday.weekday()-4)
else:
    new_date = yesterday

# format date
new_date_str = new_date.strftime("%m.%d.%Y")

for filename in os.listdir(folder_path):
    if filename[:10].count('.') == 2:
        new_filename = filename.replace(filename[:10], new_date_str)

        os.rename(os.path.join(folder_path, filename),
                  os.path.join(folder_path, new_filename))

        print(f"Renamed {filename} to {new_filename}")
