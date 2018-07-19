import global_variable as gv
import copy

def check_file_type():

    exist_question={"error_list":'',"empty_file":'',"encode_utf_8":'',"encode_Windows_1252":'',"ascii":''}
    exist_question['error_list'] = copy.deepcopy(gv.error_list)
    exist_question['empty_file'] = copy.deepcopy(gv.empty_file)
    exist_question['encode_utf_8'] = copy.deepcopy(gv.encode_utf_8)
    exist_question['encode_Windows_1252'] = copy.deepcopy(gv.encode_Windows_1252)
    exist_question['encode_ascii'] = copy.deepcopy(gv.encode_ascii)




    return exist_question