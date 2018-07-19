import os

def creat_dest_file( path_dict, dest_home="E://DMP_database" ):
    save_excel_path = dest_home + "//" + path_dict["database"] + "//" + path_dict["table"] + "//" + path_dict["table"] + ".xls"

    if  not os.path.exists(dest_home+"//"+path_dict["database"]+"//"+path_dict["table"]):
        os.makedirs(dest_home+"//"+path_dict["database"]+"//"+path_dict["table"])
    #else:
        #os.remove(dest_home+"//"+path_dict["database"]+"//"+path_dict["table"])
    os.chdir(dest_home+"//"+path_dict["database"]+"//"+path_dict["table"])

    if not os.path.exists(dest_home+"//"+path_dict["database"]+"//"+path_dict["table"]+"//"+path_dict["table"]+".xls"):
        file = open(dest_home+"//"+path_dict["database"]+"//"+path_dict["table"]+"//"+path_dict["table"]+".xls", "w")
        file.close()
    return save_excel_path





        #f_cursor=open(dest_home+"//"+path_dict["database"]+"//"+path_dict["table"]+"//"+path_dict["table"]+".xls","a+")
        #f_cursor.close()
        #return f_cursor


# if  not os.path.exists("d:/dest_home/list"):
#     os.makedirs("d:/dest_home/list")
# os.chdir('d:/dest_home/list')
# fi=open("list.xls","a+")


    #os.path.exists(no_exist_file.txt)