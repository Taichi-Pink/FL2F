#first step: update files

import os
import pandas as pd
from datetime import date
#from datetime import datetime, timedelta
from utils import *
from file_names import *

today = date.today()
print("Today's date:", today)

sheet = pd.read_excel(r'ERIN_July_2022.xlsx', sheet_name='schedule', engine='openpyxl')

total_rows = len(sheet)

for i in range(0, total_rows):
    # change lecture date
    if(l_index<6):
        if(sheet.iloc[i]["Activity"]==lecture_name[l_index]):
            event_date = sheet.iloc[i]["Date"]
            print("date: " + event_date)
            replace_one_file_line(dir_lec + lecture_file[l_index], 2, "date: "+event_date)
            replace_one_file_line(dir_lec + lecture_file[l_index], 14, "hide_from_announcments: true")  # announcement status
            replace_one_file_line(dir_lec + lecture_file[l_index], 15, "hide_from_schedules: true")     # hide in lecture section
            if (l_index < 5):
                video_lenth = 23
                for x in range(0, video_nums[l_index]):
                    replace_one_file_line(dir_lec + lecture_file[l_index], video_lenth, "  hide_from_lectures: true")  # not hide in lecture section
                    video_lenth = video_lenth + 3

            l_index = l_index + 1

    # change assignment date
    if (ass_index < 5):
        if(sheet.iloc[i]["Activity"] == assignment_name[ass_index]):
            event_date = sheet.iloc[i]["Date"]
            replace_one_file_line(dir_assign + assignment_file[ass_index], 2, "date: " + event_date)
            replace_one_file_line(dir_assign + assignment_file[ass_index], 5, "hide_from_schedules: true")    # hide in schedule and assignment section
            replace_one_file_line(dir_assign + assignment_file[ass_index], 6, "hide_from_announcments: true") # announcement status
            replace_one_file_line(dir_assign + assignment_file[ass_index], 9, "    hide: true")               # hide in schedule section
            ass_index = ass_index + 1

    if (ass_due_sche_index < 5):
        if(sheet.iloc[i]["Activity"] == assignment_due_name[ass_due_sche_index]):
            event_date = sheet.iloc[i]["Date"]
            replace_one_file_line(dir_assign + assignment_file[ass_due_sche_index], 10, "    date: " + event_date) #hide in schedule section
            ass_due_sche_index = ass_due_sche_index + 1

    if (even_index < 12):
        if(sheet.iloc[i]["Activity"] == event_name[even_index]):
            event_date = sheet.iloc[i]["Date"]
            replace_one_file_line(dir_event + event_file[even_index], 2, "date: " + event_date)
            replace_one_file_line(dir_event + event_file[even_index], 4, "hide_from_announcments: true") # announcement status
            if(event_name[even_index]=="Post-workshop survey Due"):
                replace_one_file_line(dir_event + event_file[even_index], 5, "hide: true")               #hide in schedule section

            even_index = even_index + 1


