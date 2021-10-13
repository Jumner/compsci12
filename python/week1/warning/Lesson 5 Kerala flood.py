import csv

def create_kerala_districts(filename):
    
    kerala_flood_info = {}

    with open(filename, "r") as file_in:





    return kerala_flood_info
        


def add_kerala_flood_warnings(filename, kerala_flood_info):

    with open(filename, "r") as file_in:

        




def print_kerala_flood_info(kerala_flood_info):
    for key in (kerala_flood_info):
        print(key)
        print(kerala_flood_info[key])


def main():
    

      flood_dict = create_kerala_districts("district_wise_details.csv")
      add_kerala_flood_warnings("warnings_actual_predicted.csv", flood_dict)

      print_kerala_flood_info(flood_dict)

main()
        
