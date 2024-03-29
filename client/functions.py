##text functions


##read txt file and return value
def Read_To_Txt(file_name):
    file_info = []
    file_name = file_name + ".txt"
    f = open(file_name, "r")
    while True:
        line_info = f.readline()
        if line_info != "":
            file_info.append(line_info.split(","))
        else:
            break
    ##get rids of the \n
    file_info[0][-1] = file_info[0][-1][:-1]
    file_info[1][-1] = file_info[1][-1][:-1]
    return file_info


##Write info to a .txt file

def Write_To_Text(file_name, info):
    with open(file_name + ".txt", "a") as f:
        f.write(info + "\n")
    f.close()


##Delets all data in .  `txt file
def Clear_Txt(file_name):
    file_name = file_name + ".txt"
    file = open(file_name, "r+")
    file.truncate(0)
    file.close()


##turns an array into a str which is suitable to be writen to a .txt file
def Array_Formatter(array):
    array = str(array)
    array = array.replace("'", "")
    array = array.replace("[", "")
    array = array.replace("]", "")
    array = array.replace(" ", "")
    return array


##checks that the login details are correct
def Login_Checker(username_widget, password_widget, loggin_info):
    username = username_widget.get()
    password = password_widget.get()

    for x in range(len(loggin_info[0])):
        if loggin_info[0][x] == username:
            if loggin_info[1][x] == password:
                return True
