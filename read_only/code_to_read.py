@dataclass
class OperatingSystemInterface:
    """OperatingSystemInterface is a class
    you can access the interface like a resource manager such as
    
    ```python
    with OperatingSystemInterface(directory) as osi:
        osi.do_something()
    # alternatively if there are multiple calls that you want to make you can use
    osi = OperatingSystemInterface()
    with osi as oi:
        oi.system("echo hello world")
    ```
    """
    
    def __init__(self, directory=os.getcwd()) -> None:
        self.directory: str = directory

    def __enter__(self) -> os:
        '''signature description'''
        os.chdir(self.directory)
        return os

    def __exit__(self, *args) -> os:
        '''signature description'''
        os.chdir(os.getcwd())
      
    
    def gcu(self) -> str:
        """gcu has the following params"""
        '''Get the current user i.e. C:/Users/CBE-User 05'''
        return os.path.abspath(__file__).split(r"\protocol")[0]     
                  
    
    def copy_file_from_folder(self, file : str, source_folder: str ="jaguar") -> None:
        """The folder that you are currently working on will be used as destination file
        The source folder will be searched in the protocol folder and is jaguar by default
        the file which will be replace in the local directory has path 
        ``os.path.join(self.directory,file)``
        
        Parameters
        ---
            
        file source_folder="jaguar"
            to be passed as parameter 2
        
        Returns
        ---
        result: None
        """

        source = os.path.join(os.path.abspath(__file__).split(
            r"\jaguar")[0], source_folder, file)
        destination = os.path.join(self.directory, file)

        print(f'''
        copying {source} 
        ---> into 
        {destination}
        ''')
        print(os.getcwd())
        shutil.copy(source, destination)
                          
    
    def move_folder_resources(self, destination_path : str) -> None:
        """move_folder_resources 
        the directory passed as a property will be used as a source path
        
        Parameters
        ---
            
        destination_path str
            to be passed as parameter 2
        
        Returns
        ---
        result: None
        """
        for resource in os.listdir(self.directory):
            destination_dir = os.path.join(destination_path, resource)
            source_dir = os.path.join(self.directory, resource)
            os.rename(source_dir, destination_dir)
                          
    
    def read_word_in_directory(self, word : str) -> 'list[str]':
        """read_word_in_directory has the following params
        
        Parameters
        ---
            
        word str
            to be passed as parameter 2
        
        Returns
        ---
        result: 'list[str]'
        """
        result = []
        for root, directories, file in os.walk(self.directory):
            for file in file:
                print(file)
                with open(file) as f:
                    content = f.read()
                    if content.find(word) != -1:
                        result.append(file)

        return result
                          