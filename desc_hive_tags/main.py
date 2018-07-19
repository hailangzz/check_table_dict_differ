import read_file_path as rfp
import copy
import global_variable as gv


def tags():
    auto_check_database_dict = copy.deepcopy(rfp.read_file_path("E:\hive_database"))

def main():
    #dw_ods()
    tags()

if __name__ == '__main__':
    main()


