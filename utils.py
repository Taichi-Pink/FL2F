from datetime import datetime, timedelta

def open_file(file_name):
    f = open(file_name, "r")
    filedata = f.read()
    print(filedata)
    return filedata

def replace(filedata, file_name, replace_before, replace_after):
    filedata = filedata.replace(replace_before, replace_after)
    print(filedata)
    f_w = open(file_name, "w")
    f_w.write(filedata)

def less_or_equal_today(today, event_date):
    event_date = event_date.split('T')[0]
    liss = event_date.split('-')
    y1, m1, d1 = event_date.split('-')
    year1, month1, day1 = int(y1), int(m1), int(d1)
    day2, year2, month2 = today.day, today.year, today.month
    if ((year1 > year2) or ((year1 == year2) & (month1 > month2)) or ((year1 == year2) & (month1 == month2) & (day1 > day2))):
        return False
    else:
        return True

def equal_today(today, event_date):
    event_date = event_date.split('T')[0]
    liss = event_date.split('-')
    y1, m1, d1 = event_date.split('-')
    year1, month1, day1 = int(y1), int(m1), int(d1)
    day2, year2, month2 = today.day, today.year, today.month
    if ((year1 == year2) & (month1 == month2) & (day1 == day2)):
        return True
    else:
        return False

def large_or_equal_today(today, event_date):
    event_date = event_date.split('T')[0]
    liss = event_date.split('-')
    y1, m1, d1 = event_date.split('-')
    year1, month1, day1 = int(y1), int(m1), int(d1)
    day2, year2, month2 = today.day, today.year, today.month
    if ((year1 < year2) or ((year1 == year2) & (month1 < month2)) or ((year1 == year2) & (month1 == month2) & (day1 < day2))):
        return False
    else:
        return True

# if event date is in [today-3days, today], display
def compare_with_today_in_range(today, event_date, N):
    flag1 = less_or_equal_today(today, event_date)
    date_N_days_ago = today - timedelta(days=N)
    flag2 = large_or_equal_today(date_N_days_ago, event_date)
    if(flag2 & flag1):
        return True
    else:
        return False

def find_string(filedata, find_string):
    flag = filedata.find(find_string)
    return flag

def create_lecture_file(f_name):
    print("ok")

def replace_one_file_line(file_path, line_no, replaced_string):
    print(file_path)
    file = open(file_path, "r")
    count = 0
    replacement = ""
    # using the for loop
    for line in file:
        #line = line.strip() # this will remove the white spaces that are leading and trailing, so don't use this strip() function
        if(count==line_no):
            line = replaced_string + "\n"
        replacement = replacement + line
        count = count + 1
    #print(replacement)
    file.close()
    # opening the file in write mode
    fout = open(file_path, "w")
    fout.write(replacement)
    fout.close()
