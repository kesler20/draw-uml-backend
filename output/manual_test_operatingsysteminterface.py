
import unittest
from operatingsysteminterface import OperatingSystemInterface

print("Testing:" + OperatingSystemInterface.__doc__)
        
if __name__ == "__main__":
    operatingsysteminterface = OperatingSystemInterface()
    
    operatingsysteminterface.gcu()
                
    operatingsysteminterface.copy_file_from_folder(file, source_folder)
                
    operatingsysteminterface.move_folder_resources(destination_path)
                
    operatingsysteminterface.read_word_in_directory(word)
                
        