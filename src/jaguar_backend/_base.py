import os
from typing import List
import time

class WorkflowRepresentation:

    def pp(self, print_message: str):
        print(f"------------- {print_message}")
        time.sleep(1)
     
    def describe(self, topic: str):
        if topic == "aws":
            print("=============== INIT ==============")
            print("to initialise a brand new application run 'aws init'")
            print(
                "this is preferred to do in it in the console as you will not have the amplify application")
            print("configured locally")
            print("make sure that you are in your root directory !!")
            print("make sure to document each of the amplify names and resources")
            print("=============== IMPORT ==============")
            print("to import an existing application you can use the 'amplify pull appid' suggested through the console")
            print("make sure that there are no amplify related files locally first")
            print("=================== ADD ===========================")
            print(
                "to update an amplify application use the 'aws edit' command and otherwise the 'aws update'")
            print("the former is used to add new categories to your amplify application")
            print(
                "the latter is used to remove existing categories and to replace them with new ones")