import pandas as pd
from datetime import date
from utils import *
from file_names import *

today = date.today()
print("Today's date:", today)

p   = "Dummy_Feb_2022.xlsx"
sheet = pd.read_excel(r'Dummy_Feb_2022.xlsx', sheet_name='schedule', engine='openpyxl')
total_rows = len(sheet)

# For row 0 and column 0
for i in range(0, total_rows):
    #announce lecture
    if(l_index<6):
        if(sheet.iloc[i]["Activity"]==lecture_name[l_index]):
            event_date = sheet.iloc[i]["Date"]
            #change announcement status
            announcement_flag = compare_with_today_in_range(today, event_date, 3) #announce if the event date <= today's date
            if(announcement_flag):
                replace_one_file_line(dir_lec + lecture_file[l_index], 14, "hide_from_announcments: false")
            else:
                replace_one_file_line(dir_lec + lecture_file[l_index], 14, "hide_from_announcments: true")

            l_index = l_index + 1


    #announce event
    if (even_index < 6):
        if(sheet.iloc[i]["Activity"] == event_name[even_index]):
            event_date = sheet.iloc[i]["Date"]
            # change announcement status
            announcement_flag = compare_with_today_in_range(today, event_date, 1)  # announce if the event date <= today's date
            if (announcement_flag):
                replace_one_file_line(dir_event + event_file[even_index], 4, "hide_from_announcments: false")
            else:
                replace_one_file_line(dir_event + event_file[even_index], 4, "hide_from_announcments: true")
            even_index = even_index + 1

    #announce assignments
    if (ass_index < 5):
        if(sheet.iloc[i]["Activity"] == assignment_name[ass_index]):
            event_date = sheet.iloc[i]["Date"]
            # change announcement status
            announcement_flag = compare_with_today_in_range(today, event_date, 3)  # announce if the event date <= today's date
            if (announcement_flag):
                replace_one_file_line(dir_assign + assignment_file[ass_index], 6, "hide_from_announcments: false")
            else:
                replace_one_file_line(dir_assign + assignment_file[ass_index], 6, "hide_from_announcments: true")
            ass_index = ass_index + 1

    #display assignments in schedule
    if (ass_sche_index < 5):
        if(sheet.iloc[i]["Activity"] == assignment_name[ass_sche_index]):
            event_date = sheet.iloc[i]["Date"]
            display_flag = less_or_equal_today(today, event_date)  # announce if the event date <= today's date
            if (display_flag):
                replace_one_file_line(dir_assign + assignment_file[ass_sche_index], 5, "hide_from_schedules: false")    # hide in schedule section

            ass_sche_index = ass_sche_index + 1

    # display assignments due in schedule
    if (ass_due_sche_index < 5):
        if(sheet.iloc[i]["Activity"] == assignment_due_name[ass_due_sche_index]):
            event_date = sheet.iloc[i]["Date"]
            display_flag = less_or_equal_today(today, event_date)  # announce if the event date <= today's date
            if (display_flag):
                replace_one_file_line(dir_assign + assignment_file[ass_due_sche_index], 9, "    hide: false")    # hide in schedule section

            ass_due_sche_index = ass_due_sche_index + 1


    # display post-workshop survey in schedule
    if (sheet.iloc[i]["Activity"] == "Post-workshop survey Due"):
        event_date = sheet.iloc[i]["Date"]
        display_flag = less_or_equal_today(today, event_date)  # announce if the event date <= today's date
        if (display_flag):
            replace_one_file_line(dir_event + event_file[6], 5, "hide: false")

    # display lectures in lecture section
    if (l_sche_index < 6):
        if (sheet.iloc[i]["Activity"] == lecture_name[l_sche_index]):

            event_date = sheet.iloc[i]["Date"]
            display_flag = less_or_equal_today(today, event_date)  # announce if the event date <= today's date
            if (display_flag):
                replace_one_file_line(dir_lec + lecture_file[l_sche_index], 15, "hide_from_schedules: false")  # hide in schedule section
            print(l_sche_index, sheet.iloc[i]["Activity"], lecture_name[l_sche_index])
            l_sche_index = l_sche_index + 1



    # display assignments in assignment section
    if (ass_ass_index < 5):
        if (sheet.iloc[i]["Activity"] == assignment_name[ass_ass_index]):
            event_date = sheet.iloc[i]["Date"]
            display_flag = less_or_equal_today(today, event_date)  # announce if the event date <= today's date
            if (display_flag):
                replace_one_file_line(dir_assign + assignment_file[ass_ass_index], 5, "hide_from_schedules: false")  # hide in schedule section

            ass_ass_index = ass_ass_index + 1