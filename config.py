import os
from os import path

flag = True
while(flag):
    literal = f'''
    :::::::::::::::::::::::::::::::::::::::::::::::::::::
    |       Welcome to CRUD Programme using Python      |
    :::::::::::::::::::::::::::::::::::::::::::::::::::::
    | > Insert 1 for Create                             |
    | > Insert 2 for Read                               |
    | > Insert 3 for Update                             |
    | > Insert 4 for Delete                             |
    | > Insert 5 for Exit                               |
    :::::::::::::::::::::::::::::::::::::::::::::::::::::
    '''
    try:
        user_value = int(input(literal))
        match(user_value):
            case 1:
                try:
                    user_data = input("> Insert data to write: \n")
                    config = open("userdata.txt","w+")
                    config.write(str(user_data))
                    config.close()
                except Exception as e:
                    print("Something went wrong",e)
                    # ---------------------------------------------------
                    # ---------------------------------------------------
            case 2:
                try:
                    condition = path.exists("userdata.txt")
                    if(condition):
                        config = open("userdata.txt","r")
                        data = config.read()
                        reading_literal_start = f'''
                        :::::::::::::::::::::::::::::::::::::::::::::::::::::
                        |       Reading All Data from the userdata.txt      |
                        :::::::::::::::::::::::::::::::::::::::::::::::::::::
                        '''
                        print(reading_literal_start)

                        rawData = "" # Store the all the data

                        # Reading the data through iterating and adding inside the rawData
                        for i in data:
                            rawData+=i
                        
                        print(rawData) # Print all the data after sucessfully read
                        reading_literal_end = f'''
                        :::::::::::::::::::::::::::::::::::::::::::::::::::::
                        '''
                        print(reading_literal_end)
                        config.close()
                    else:
                        print("Please create file first then delete the same!")
                except Exception as e:
                    print("Something went wrong",e)
                    # ---------------------------------------------------
                    # ---------------------------------------------------
            case 3:
                try:
                    condition = path.exists("userdata.txt")
                    if(condition):
                        updating_literal_start = f'''
                        :::::::::::::::::::::::::::::::::::::::::::::::::::::
                        |      Updating All Data from the userdata.txt      |
                        :::::::::::::::::::::::::::::::::::::::::::::::::::::
                        ℹ Note: Updating data will have the old data with it
                        '''
                        print(updating_literal_start)
                        user_data = input("> Insert data to update: \n")
                        config = open("userdata.txt","a+")
                        config.write(str(user_data))
                        config.close()
                        updating_literal_end = f'''
                        :::::::::::::::::::::::::::::::::::::::::::::::::::::
                        '''
                        print(updating_literal_end)
                    else:
                        print("Please create file first then delete the same!")
                except Exception as e:
                    print("Something went wrong",e)
                    # ---------------------------------------------------
                    # ---------------------------------------------------
            case 4:
                try:
                    condition = path.exists("userdata.txt")
                    if(condition):
                        deleting_literal_start = f'''
                        :::::::::::::::::::::::::::::::::::::::::::::::::::::
                        |      Deleting All Data from the userdata.txt      |
                        :::::::::::::::::::::::::::::::::::::::::::::::::::::
                            ℹ Note: Deleting will not delete the file      
                        '''
                        print(deleting_literal_start)
                        acept_term = str(input("Do you sure want to delete the data? \n(y/n): "))
                        if(acept_term.lower() == "y"):
                            config = open("userdata.txt","w")
                            config.write("")
                            config.close()
                        else:
                            None
                        deleting_literal_end = f'''
                        :::::::::::::::::::::::::::::::::::::::::::::::::::::
                        '''
                        print(deleting_literal_end)
                    else:
                        print("Please create file first then delete the same!")
                except Exception as e:
                    print("Something went wrong",e)
                    # ---------------------------------------------------
                    # ---------------------------------------------------
            case 5:
                condition = path.exists("userdata.txt")
                if(condition):
                    print("Exiting from the Programme delete the userdata file!")
                    acept_term = str(input("Do you sure want to delete the file? \n(y/n): "))
                    if(acept_term.lower() == "y"):
                        os.remove("userdata.txt")
                    else:
                        None
                else:
                    None
                # -->
                end_literal = f'''
                :::::::::::::::::::::::::::::::::::::::::::::::::::::
                |     Thank You for using this Python Programme     |
                :::::::::::::::::::::::::::::::::::::::::::::::::::::
                '''
                print(end_literal)
                flag = False
                # ---------------------------------------------------
                # ---------------------------------------------------
            case other:
                print("Sorry! you mistakenly entered higher or lesser number please enter the number from 1 to 5")
    except Exception as e:
        print("Please enter only number value from 1 to 5")
    finally:
        print("Loading...................")