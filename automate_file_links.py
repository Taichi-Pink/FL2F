import pandas as pd
from datetime import date
from utils import *
from file_names import *

sheet = pd.read_excel(r'ERIN_July_2022.xlsx', sheet_name='file_link', engine='openpyxl')
total_rows = len(sheet)

###yearly
# replace_one_file_line(dir_lec + lecture_file[0], 19, "- url: " + sheet.iloc[0]["Links"])
# replace_one_file_line(dir_lec + lecture_file[1], 19, "- url: " + sheet.iloc[1]["Links"])
# replace_one_file_line(dir_lec + lecture_file[2], 19, "- url: " + sheet.iloc[2]["Links"])
# replace_one_file_line(dir_lec + lecture_file[3], 19, "- url: " + sheet.iloc[3]["Links"])
# replace_one_file_line(dir_lec + lecture_file[4], 19, "- url: " + sheet.iloc[4]["Links"])
#
# #yearly
# replace_one_file_line(dir_lec + lecture_file[0], 21, "- url: " + sheet.iloc[5]["Links"])
# replace_one_file_line(dir_lec + lecture_file[0], 24, "- url: " + sheet.iloc[6]["Links"])
# replace_one_file_line(dir_lec + lecture_file[0], 27, "- url: " + sheet.iloc[7]["Links"])
# replace_one_file_line(dir_lec + lecture_file[1], 21, "- url: " + sheet.iloc[8]["Links"])
# replace_one_file_line(dir_lec + lecture_file[1], 24, "- url: " + sheet.iloc[9]["Links"])
# replace_one_file_line(dir_lec + lecture_file[1], 27, "- url: " + sheet.iloc[10]["Links"])
# replace_one_file_line(dir_lec + lecture_file[1], 30, "- url: " + sheet.iloc[11]["Links"])
# replace_one_file_line(dir_lec + lecture_file[2], 21, "- url: " + sheet.iloc[12]["Links"])
# replace_one_file_line(dir_lec + lecture_file[2], 24, "- url: " + sheet.iloc[13]["Links"])
# replace_one_file_line(dir_lec + lecture_file[2], 27, "- url: " + sheet.iloc[14]["Links"])
# replace_one_file_line(dir_lec + lecture_file[2], 30, "- url: " + sheet.iloc[15]["Links"])
# replace_one_file_line(dir_lec + lecture_file[2], 33, "- url: " + sheet.iloc[16]["Links"])
# replace_one_file_line(dir_lec + lecture_file[3], 21, "- url: " + sheet.iloc[17]["Links"])
# replace_one_file_line(dir_lec + lecture_file[3], 24, "- url: " + sheet.iloc[18]["Links"])
# replace_one_file_line(dir_lec + lecture_file[3], 27, "- url: " + sheet.iloc[19]["Links"])
# replace_one_file_line(dir_lec + lecture_file[3], 30, "- url: " + sheet.iloc[20]["Links"])
# replace_one_file_line(dir_lec + lecture_file[4], 21, "- url: " + sheet.iloc[21]["Links"])
# replace_one_file_line(dir_lec + lecture_file[4], 24, "- url: " + sheet.iloc[22]["Links"])
# replace_one_file_line(dir_lec + lecture_file[4], 27, "- url: " + sheet.iloc[23]["Links"])
# replace_one_file_line(dir_lec + lecture_file[4], 30, "- url: " + sheet.iloc[24]["Links"])

#yearly
#replace_one_file_line('/Users/liuziyi/Documents/Github/FL2F/materials.md', 31, "[Booklet](" + sheet.iloc[16]["Links"] + ")" )

#update links for each WS
replace_one_file_line(dir_event + event_file[0], 9, "[meeting schedule register file](" + sheet.iloc[25]["Links"] + ")" )
replace_one_file_line(dir_event + event_file[1], 9, "[meeting schedule register file](" + sheet.iloc[26]["Links"] + ")" )
replace_one_file_line(dir_event + event_file[2], 9, "[meeting schedule register file](" + sheet.iloc[27]["Links"] + ")" )
replace_one_file_line(dir_event + event_file[3], 9, "[meeting schedule register file](" + sheet.iloc[28]["Links"] + ")" )
replace_one_file_line(dir_event + event_file[5], 9, "[meeting schedule register file](" + sheet.iloc[29]["Links"] + ")" )
replace_one_file_line(dir_event + event_file[7], 9, "[meeting schedule register file](" + sheet.iloc[30]["Links"] + ")" )

#change this code!!!! update links for each WS
assign5_index = 26
replace_one_file_line(dir_assign + assignment_file[4], assign5_index, "* ["+ sheet.iloc[32]["Names"] +"](" + sheet.iloc[32]["Links"] + ")" )
replace_one_file_line(dir_assign + assignment_file[4], assign5_index + 1, "* ["+ sheet.iloc[33]["Names"] +"](" + sheet.iloc[33]["Links"] + ")" )
replace_one_file_line(dir_assign + assignment_file[4], assign5_index + 2, "* ["+ sheet.iloc[34]["Names"] +"](" + sheet.iloc[34]["Links"] + ")" )
replace_one_file_line(dir_assign + assignment_file[4], assign5_index + 3, "* ["+ sheet.iloc[35]["Names"] +"](" + sheet.iloc[35]["Links"] + ")" )
#####




