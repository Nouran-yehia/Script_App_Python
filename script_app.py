import re
import json
import fileinput
import datetime
import sys
import os
import os.path
from os import path

def welcome():
    guest_name = input("Please enter your name: ")
    if not guest_name:
        welcome()
    print ("welcome {},".format(guest_name))
    home()
def home():
    while True:
        option = input("Please select an option:- \n 1- Enter reg to register \n 2- Enter log to login \n 3- Enter ex to exit \n")
        if option == "reg":
            register()
        elif option == "log":
            login()
        elif option == "ex":
            sys.exit("Thanks for using our App :), Good Bye!")
        else:
            print("You didn't enter a right selection")
            True
def fname():
    while True:
        first_name = input("Note: Enter h to return to home OR Enter ex to exit \n Enter your First name: ")
        if not first_name:
            print("you didn't enter your first name! \n")
            True
        else:
            if first_name == "h" or first_name == "H":
                home()
            if first_name == "ex" or first_name == "EX" or first_name == "Ex":
                sys.exit("Thanks for using our App :), Good Bye!")
            else:
                return first_name
def lname():
    while True:
        last_name = input("Note: Enter h to return to home OR Enter ex to exit \n PLease enter your last name: ")
        if not last_name:
            print("you didn't enter your last name! \n")
            lname()
        else:
            if last_name == "h" or last_name == "H":
                home()
            if last_name == "ex" or last_name == "EX" or last_name == "Ex":
                sys.exit("Thanks for using our App :), Good Bye!")
            else:
                return last_name
def email_exists_valid(email):
    if path.exists("users.txt"):
        with open("projects.txt", "rt") as u:
            if email in u.read():
                return True
            else:
                return False
def email1():
    while True:
        email = input("Note: Enter h to return to home OR Enter ex to exit \n Please enter your email: ")        
        t = email_exists_valid(email)
        if t == True:
            print("You already have an account!")
            login()
        else:
            if email:
                if email == "h" or email == "H":
                    home()
                elif email == "ex" or email == "EX" or email == "Ex":
                    sys.exit("Thanks for using our App :)")
                else:
                    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
                    if (re.search(regex,email)):
                        return email
                    else:
                        print("You entered invalid email!")
                        True
            if not email:
                print("you didn't enter your email! \n")
                True
        
def password1():
    while True:
        password = input("Note: Enter h to return to home OR Enter ex to exit \n Please enter your Password: ")
        if password:
            if password == "h" or password == "H":
                home()
            elif password == "ex" or password == "EX" or password == "Ex":
                sys.exit("Thanks for using our App :), Good Bye!")
            else:
                return password
        elif not password:
            print("you didn't enter your password!")
            True
    
def conf_password1(password):
    while True:
        conf_password = input("Please confirm your password:")
        if conf_password:
            if conf_password == "h" or conf_password == "H":
                home()
            elif conf_password == "ex" or conf_password == "EX" or conf_password == "Ex":
                sys.exit("Thanks for using our App :), Good Bye!")
            else:
                if conf_password == password:
                    return conf_password
                else:
                    print("password confirmation is not equal to your password!")
                    True
        else:
            print("You didn't confirm your password!")
            True

def mobile_num1():
    while True:
        mobile_num = input("Please enter your Mobile number: ")
        if mobile_num:
            if mobile_num == "h" or mobile_num == "H":
                home()
            elif mobile_num == "ex" or mobile_num == "EX" or mobile_num == "Ex":
                sys.exit("Thanks for using our App :), Good Bye!")
            else:
                regex = "^(01)[0-2][0-9]\d{7}"
                if (re.search(regex,mobile_num)):
                    return mobile_num
                else:
                    print("invalid mobile number")
                    True
        else:
            print("you didn't enter your mobile number!")
            True
def register():
    first_name = fname()
    last_name = lname()
    email = email1()
    password = password1()
    conf_password = conf_password1(password)
    mobile_num = mobile_num1()
    user = {
        "first_name":first_name,
        "last_name":last_name,
        "email":email,
        "password":password,
        "conf_password":conf_password,
        "mobile_num": mobile_num
        }
    with open("users.txt", "a+") as u:
        u.write(str(user)+"\n")
        print ("you are signed up successfully :)")
    login()

def login():
    if path.exists("users.txt"):
        email_input = input("Login\n Email: \n")
        password_input = input("Password: ")
        with open("users.txt", "rt") as u:
            for line in u:
                if email_input in line:
                    data = line
                else:
                    data = ""
        if data == "":
            print("wrong email")
            opt = input("to try again enter log, to register enter reg")
            if opt == "log":
                login()
            elif opt == "reg":
                register()
        else:
            data_1 = eval(data)
            pass_readed = data_1.get('password')
            name_readed = data_1.get('first_name')
            email_readed = data_1.get('email')
            if password_input == pass_readed:
                print (" You are logged in, Welcome back {} ".format(name_readed))
                logged_option(email_readed)
    else:
        opt_input = input("No users created yet, Please enter 2 and register or 3 to exit !\n")
        if opt_input == 2:
            home()
        if opt_input == 3:
            sys.exit("Thanks for using our App :), Good Bye!")
def logged_option(email_readed):
    while True:
        opt_log = input("Please choose an option \n 1 to create new project \n 2 to Edit your project \n 3 to list all the projects \n 4 to search for a specific project \n 5 to remove your project \n") 
        if opt_log == "1":
            create_project(email_readed)
        elif opt_log == "2":
            edit_project(email_readed)
        elif opt_log == "3":
            list_project()
        elif opt_log == "4":
            search_project()
        elif opt_log == "5":
            remove_project(email_readed)
        else:
            print ("You entered a wrong option , Please try again")
            True
def pro_title():
    while True:
        title = input("Enter t to logout \n Enter ex to exit \n Please enter the project title: ")
        if title:
            if title == "t" or title == "T":
                home()
            elif title == "ex" or title == "EX" or title == "Ex":
                sys.exit("Thanks for using our App :), Good Bye!")
            else:
                return title
        else:
            print ("You didn't enter the title")
            True 
def pro_details():
    while True:
        details = input("Note: Enter t to logout \n Enter ex to exit \n Please enter the project details: ")
        if details:
            if details == "t" or details == "T":
                home()
            elif details == "ex" or details == "EX" or details == "Ex":
                sys.exit("Thanks for using our App :), Good Bye!")
            else:
                return details
        else:
            print("You didn't enter the project's details")
            True

def pro_total_target():
    while True:
        total_target = input("Note: Enter r return to options \n Enter t to logout \n Enter ex to exit \n Please enter the project's total target in EGP: ")
        if total_target:
            if total_target == "t" or total_target == "T":
                home()
            elif total_target == "ex" or total_target == "EX" or total_target == "Ex":
                sys.exit("Thanks for using our App :), Good Bye!")
            else:
                return total_target
        else:
            print ("You didn't enter the project's total target")
            True

def set_start_time():
    while True:
        start_time = input("please enter the project's start date :")
        regex = "^(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[0-2])\/([12][0-9]{3})$"
        if (re.search(regex,start_time)):
            return start_time
        else:
            print("You didn't enter a valid start time")
            True

def set_end_time():
    while True:
        end_time = input("please enter the project's end date :")
        regex = "^(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[0-2])\/([12][0-9]{3})$"
        if (re.search(regex, end_time)):
            return end_time
        else:
            print ("You didn't enter a valid end date")
            True
                
def create_project(signed_email):
    if path.exists("projects.txt"):
        flag = bef_pro_crud(signed_email)
        if flag == True:
            print ("You already have created your project")
        else:
            title = pro_title()
            details = pro_details()
            total_target = pro_total_target()
            start_time = set_start_time()
            end_time = set_end_time()
            date = {
                "start_time": start_time,
                "end_time": end_time
            }
            project = {
                "title": title,
                "details": details,
                "total_target":total_target,
                "date": date,
                "owner_email": signed_email
            }
            with open("projects.txt", "a+") as u:
                u.write(str(project)+"\n")
                print("Your project created successfully!")
    else:
        title = pro_title()
        details = pro_details()
        total_target = pro_total_target()
        start_time = set_start_time()
        end_time = set_end_time()
        date = {
            "start_time": start_time,
            "end_time": end_time
        }
        project = {
            "title": title,
            "details": details,
            "total_target":total_target,
            "date": date,
            "owner_email": signed_email
        }
        with open("projects.txt", "w") as u:
            u.write(str(project)+"\n")
            print("Your project created successfully!")
    end_options()
def end_options():
    while True:
        opt2 = input ("Enter 2 to Logout \n Enter 3 to Exit \n")        
        if opt2 == "2":
            home()
        elif opt2 == "3":
            sys.exit("Thanks for using our App :), Good Bye!")
        else:
            print ("you entered wrong selection value!")
            True


def bef_pro_crud(email_input):
    with open("projects.txt", "rt") as u:
        if email_input in u.read():
            return True
        else:
            return False

def read_projects():
    with open("projects.txt", "rt") as p:
        lines = p.readlines()
        print(lines)

def edit_project(signed_email):
    if path.exists("projects.txt"):
        t = bef_pro_crud(signed_email)
        if t == True:
            while True:
                with open("projects.txt", "rt") as u:
                    for line in u:
                        if signed_email in line:
                            data = eval(line)
                            title = data.get('title')
                            details = data.get('details')
                            date = data.get('date')
                            total_target = data.get('total_target')
                            start_time = date.get("start_time")
                            end_time = date.get("end_time")        
                opt = input("Please enter the key that you want to edit on:\n Enter 1 to edit title \n Enter 2 to edit details \n Enter 3 to edit total target \n Enter 4 to edit date \n")
                if opt == "1":
                    opt2 = input("please enter 2 to return to edit menu \n Instead of {} Enter the new title: ".format(title))
                    if opt2:
                        if opt2 == 2:
                            True
                        elif opt2:
                            line_num = line_number(signed_email)
                            with open("projects.txt", "r") as infile:
                                lines = infile.readlines()
                            with open("projects.txt", "w") as outfile:
                                for pos, line in enumerate(lines):
                                    if pos != line_num:
                                        outfile.write(line)
                            new_title = opt2
                            line1 = {
                                "title": new_title,
                                "details": details,
                                "total_target": total_target,
                                "date": date,
                                "owner_email": signed_email
                                    }
                            with open("projects.txt", "a+") as u:                                   
                                u.write(str(line1)+"\n")
                                print("Your project's title updated successfully!")
                                u.close()
                            end_options()            
                        else:
                            print("Your entered a wrong value!")
                            True
                    else:
                        print("You didn't enter a new title!")
                        True
                elif opt == "2":
                    opt3 = input("Please enter 2 to return to edit menu \n Enter new Details: ")
                    if opt3:
                        if opt3 == 2:
                            True
                        else:
                            new_details = opt3
                            line_num = line_number(signed_email)
                            with open("projects.txt", "r") as infile:
                                lines = infile.readlines()
                            with open("projects.txt", "w") as outfile:
                                for pos, line in enumerate(lines):
                                    if pos != line_num:
                                        outfile.write(line)
                            new_details = opt3
                            line2 = {
                                "title": title,
                                "details": new_details,
                                "total_target": total_target,
                                "date": date,
                                "owner_email": signed_email
                                    }
                            with open("projects.txt", "a+") as u:                                   
                                u.write(str(line2)+"\n")
                                print("Your project's description updated successfully!")
                                u.close()
                            end_options()            
                    else:
                        print("You didn't enter a value!")  
                        True   
                elif opt == "3":
                    opt4 = input("Please enter 2 to return to edit menu \n Enter new total target value: ")
                    if opt4:
                        if opt4 == 2:
                            True
                        regex1= "^[0-9]*$"
                        if re.search(regex1,opt4):
                            new_total_target = opt4
                            line_num = line_number(signed_email)
                            with open("projects.txt", "r") as infile:
                                lines = infile.readlines()
                            with open("projects.txt", "w") as outfile:
                                for pos, line in enumerate(lines):
                                    if pos != line_num:
                                        outfile.write(line)
                            line3 = {
                                "title": title,
                                "details": details,
                                "total_target": new_total_target,
                                "date": date,
                                "owner_email": signed_email
                                    }
                            with open("projects.txt", "a+") as u:                                   
                                u.write(str(line3)+"\n")
                                print("Your project's total target updated successfully!")
                                u.close()
                            end_options()               
                        else:
                            print ("You didn't enter a valid target value")
                            True
                    else:
                        print ("You didn't enter a value!")
                        True
                elif opt == "4":
                    opt5 = input("Enter new start date: ")
                    opt6 = input("Enter new end date: ")
                    if opt5 and opt6:
                        new_date = {
                            "start_time": opt5,
                            "end_time":opt6
                        }
                        line_num = line_number(signed_email)
                        with open("projects.txt", "r") as infile:
                            lines = infile.readlines()
                        with open("projects.txt", "w") as outfile:
                            for pos, line in enumerate(lines):
                                if pos != line_num:
                                    outfile.write(line)
                        line4 = {
                            "title":title,
                            "details": details,
                            "total_target": total_target,
                            "date": new_date,
                            "owner_email": signed_email
                                }
                        with open("projects.txt", "a+") as u:                                   
                            u.write(str(line4)+"\n")
                            print("Your project's dates updated successfully!")
                            u.close()
                        end_options()            
                    else:
                        print("You didn't enter the start and end date!")
                        True
                else:
                    print("You didn't enter a true choice!")
                    True
        else:
            print("You didn't create a project yet")
    else:
        print("There is no projects yet")        

def line_number(signed_email):
    with open("projects.txt") as f:
        for num, line in enumerate(f, 1):
            if signed_email in line:
                line_num = num-1
                return line_num
    


def remove_project(signed_email):
    if path.exists("projects.txt"):
        line_num = line_number(signed_email)
        t = bef_pro_crud(signed_email)
        if t == True:
            opt = input("Are you sure you want to remove your project y or n ? \n")
            if opt:
                if opt == "y" or opt == "Y":
                    with open("projects.txt", "r") as infile:
                        lines = infile.readlines()
                    with open("projects.txt", "w") as outfile:
                        for pos, line in enumerate(lines):
                            if pos != line_num:
                                outfile.write(line)
                    print("Your project deleted successfully :)")
                elif opt == "n" or opt == "N":
                    end_options()
                else:
                    print("Invalid choice")
            else:
                print("You didn't enter your choice!")
        else:
            print("You don't have a project to remove!")
            end_options()
    else:
        print("there is no projects yet!")
def search_project(): ##Bouns
    while True:
        start_date = input("Please enter the start date that you want to search for the project on it: ")
        end_date = input("Please enter the end date that you want to search for :")
        if path.exists("projects.txt"):
            with open("projects.txt", "rt") as u:
                for line in u:
                    if start_date and end_date in line:
                        data = eval(line)
                        tit = data.get('title')
                        det = data.get('details')
                        owner = data.get('owner_email')
                        target = data.get('total_target')
                        date = data.get('date')
                        str_date = date.get('start_time')
                        end_date = date.get('end_time')
                        print ("------------------------------------------------------------")
                        print("Project:{}".format(tit))
                        print("Project's Details: {}".format(det))
                        print("Project's target value: {}".format(target))
                        print("Owner's Email: {}".format(owner))
                        print("Start Date: {}".format(str_date))
                        print("End Date: {}".format(end_date))
                        print("=============================================================")
                if not start_date and end_date in line:
                    print("No project found!")
        else:
            print("There is no projects yet!")
        end_options()
    
def list_project():
    if path.exists("projects.txt"):
         with open("projects.txt", "rt") as u:
            for line in u:
                data = eval(line)
                tit = data.get('title')
                det = data.get('details')
                owner = data.get('owner_email')
                target = data.get('total_target')
                date = data.get('date')
                # datee = eval(date)
                str_date = date.get('start_time')
                end_date = date.get('end_time')
                print("----------------------------------------------------------------------")
                print("Project:{}".format(tit))
                print("Project's Details: {}".format(det))
                print("Project's target value: {}".format(target))
                print("Owner's Email: {}".format(owner))
                print("Start Date: {}".format(str_date))
                print("End Date: {}".format(end_date))
                print("=======================================================================")
        
    else:
        print("There is no projects to list!")
        end_options()

welcome()