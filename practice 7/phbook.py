from connect import *


while True:
    print("List of commands")
    print('1.Insert from terminal')
    print("2.Insert from csv file")
    print("3.Edit name")
    print("4.Edit phone number")
    print("5.Search by name or phone number")
    print("6.Delete by name or phone number")
    print("7.Search by pattern")
    print("8. Get contacts with pagiation")
    print("9.Insert or update")
    print("10.Insert from list")
    print("11.Delete with name or number")
    print("12.quit")
    choice=input("choose the option ")
    if choice =="12":
        print("quitting the programm")
        break
    if choice =="1":
        name=input("enter contact name")
        phonenum=input("enter phone number")
        add_contact(name,phonenum)
    if choice =="2":
        import_csv("contacts.csv")
    if choice == "3":
        num=input("enter number of contact")
        new_name=input("enter new name")
        update_name(new_name,num)
    if choice =="4":
        num=input("enter number of contact")
        new_num=input("enter new number")
        update_phone(new_num,num)
    if choice=="5":
        query=input("enter name or number")
        searching(query)
    if choice=="6":
        query=input("enter a number or name")
        delete_concact(query)
    if choice =="7":
        pattern=input("write a pattern")
        search_pattern(pattern)
    if choice =="8":
        limit=int(input("enter a limit"))
        offset=int(input("write offset"))
        get_paginated(limit,offset)
    if choice=="9":
        name=input("enter a name you want to update or insrt")
        num=input("enter a number")
        insert_or_update(name,num)
    if choice=="10":
        names=list(map(str,input("enter all names").split()))
        nums=list(map(str,input("enter all numbers").split()))
        insert_many(names,nums)
    if choice=="11":
        query=input("enter a name or a number")
        delete_contact(query)



