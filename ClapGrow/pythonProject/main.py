import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('path/to/your/credentials.json', scope)

# Authorize the clientsheet
client = gspread.authorize(creds)

# Get the instance of the Spreadsheet
sheet = client.open('Your Google Sheet Name')

# Get the first sheet of the Spreadsheet
worksheet = sheet.get_worksheet(0)

# Get the value from the cell where the number 30,00,000 is input
# Assuming the value is in cell A1
cell_value = worksheet.acell('A1').value
number_from_sheet = int(cell_value.replace(',', ''))

# Net Premium from the document
net_premium = 2895421

# Compare the values
if net_premium > number_from_sheet:
    print("The net premium is greater than the number mentioned in the Google sheet.")
elif net_premium < number_from_sheet:
    print("The net premium is lesser than the number mentioned in the Google sheet.")
else:
    print("The net premium is equal to the number mentioned in the Google sheet.")
