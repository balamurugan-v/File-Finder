import datetime
import time
import os
import gspread
Counter = 0
S_no = 1
content = ""
from oauth2client.service_account import ServiceAccountCredentials
CURR_DIR = os.path.dirname(os.path.abspath(_file_))

SCOPES = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive',
      'https://www.googleapis.com/auth/spreadsheets']

def get_api_connection():
	global S_no
	global starting_time
	global content
	credential_path = os.path.join(CURR_DIR, CLIENT_SECRET_FILE)
	credentials = ServiceAccountCredentials.from_json_keyfile_name(credential_path, SCOPES)
	google_connection = gspread.authorize(credentials)
	googlesheetdata = google_connection.open_by_key(SHEET_ID).worksheet(SHEET_NAME)
	if S_no == 1:
	    row = ["S.no", "starting_time", "Directory", "Total_lines", "Time_of_arrival", "status"]
	    googlesheetdata.insert_row(row, 1)
	content = str(datetime.datetime.now())
	googlesheetdata.update_cell(2, 1, S_no)
	googlesheetdata.update_cell(2, 2, starting_time)
	googlesheetdata.update_cell(2, 3, "//home/File finder/file.txt/")
	googlesheetdata.update_cell(2, 4, Counter)
	googlesheetdata.update_cell(2, 5, content)
	googlesheetdata.update_cell(2, 6, "accepted")

def activities():
	global content
	try:
	    CON_FILE = "../data2/input/source.txt"
	    file_stats = os.stat(CON_FILE)
	    if file_stats.st_size == 0:
		print("File detected.......")
		print("NO contents present.......")
		return 0
	    else:
		print("file detected.....")
		print("processing........")
		global Counter
		file = open(CON_FILE, "r")
		Content = file.read()
		CoList = Content.split("\n")
		for i in CoList:
		    if i:
		        Counter += 1
		get_api_connection()
	except Exception:
	   pass
	return 0

starting_time = ""
if _name_ == '_main_':
	starting_time = str(datetime.datetime.now())
	while True:
	    print("attempting to read file......")
	    a = activities()
	    if a == 0:
		time.sleep(10)
		print("trying again")
	    else:
		print("success")
		break

