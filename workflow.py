from random import randint
import sys
import os
import time
import json
from interfaces.os_interface import OperatingSystemInterface

osi = OperatingSystemInterface()
user_directory = osi.gcu()

# this will offset py 4 the args that you pass since arg[0] is workflow.py arg[1] is class and arg[2] is a function
argument_number = len(["workflow.py","class","function"])


class FileSynchronizer(object):

    def __init__(self) -> None:
        self.all_directories = os.listdir(r"C:\Users\Uchek\protocol")
        self.default_files_to_copy = [r"interfaces\os_interface.py", "workflow.py"]

    def synchronize_files_from_jaguar(self, *args):
        '''
        to separate between files and folders put a 'f filename.extension' in front of your files
        '''
        directories_to_copy_to, files_to_copy = self.sort_args(args)  
        
        # now you can push all of the changes to github within the protocol folder as follows
        for dir in directories_to_copy_to:
            if dir == "jaguar":
                pass
            else:
                with OperatingSystemInterface(os.path.join(r"C:\Users\Uchek\protocol", dir)) as op_sys:
                    self.create_folders_where_needed(dir,files_to_copy)

                osi = OperatingSystemInterface(
                    os.path.join(r"C:\Users\Uchek\protocol", dir))
                for file in files_to_copy:
                    osi.copy_file_from_folder(file)
    
    def create_folders_where_needed(self,dir,files_to_copy:list[str]):
        folders = []
        for file in files_to_copy:
            for folder in file.split(r"\ ".replace(" ",""))[:-1]:
                folders.append(folder)
        most_deeply_nested_folder = os.path.join(r"C:\Users\Uchek\protocol", dir,**folders)
        if not os.path.isdir(most_deeply_nested_folder):
            os.system(f"mkdir {most_deeply_nested_folder}")
            print(most_deeply_nested_folder,os.path.isdir(most_deeply_nested_folder))
 
    def sort_args(self,*args):
        if len(args) == 0:
            directories_to_copy_to = self.all_directories
            files_to_copy = self.default_files_to_copy
        else:
            directories_to_copy_to = []
            files_to_copy = []
            for arg in args:
                if arg.startswith("f "):
                    files_to_copy.append(arg)
                else:
                    directories_to_copy_to.append(arg)
        return directories_to_copy_to, files_to_copy   

    def search_for_dir(dir,dirs: list[str]):
        # 'we want to get this kind of behavior to traverse the file system
        # if os.path.isdir(os.path.join(r"C:\Users\Uchek\protocol", dir, dirs[0])):
        #   if os.path.isdir(os.path.join(r"C:\Users\Uchek\protocol", dir, dirs[0],dirs[1]))
        
        # this can be emulated by appending the dirs that exists in the list of the arguments and doing so until
        # we do not find a dir'
        
        i = 0
        folders = [dirs[i]]
        while i < len(dirs) - 1:
            if os.path.isdir(os.path.join(r"C:\Users\Uchek\protocol", dir,*folders)):
                i += 1
                folders.append(dirs[i])
        return folders             

class WorkflowRepresentation(object):

    def __init__(self) -> None:
        pass

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

class AmplifyApplication(object):

    def __init__(self) -> None:
        self.categories = ["notifications", 'api', 'auth', 'custom', 'storage',
                           'analytics', 'function', 'geo', 'hosting', 'interactions', 'predictions', 'xr']

        self.initial_args = len(["workflow.py", "aws", "function_signature"])
        self.workflow_ui = WorkflowRepresentation()
    
    def update_amplify_application(self,*categoryIDs):
        '''modify_amplify_application will;
        1. remove each category selected through the category ids
        2. add each category selected through the category ids
        3. check the amplify status between each addition
        4. push the changes to the amplify application
        5. pull the changes to the local backend

        ---
        Params:
        - categoryIDs : list or strings, this will be turned into a list of integers and used to access the desired
        category from the categories list

        ---
        Returns: 
        - None
        '''
        categoryIDs = categoryIDs[0]
        os.system(
            "start https://docs.google.com/spreadsheets/d/1bVORUU7gE_fYZW1FjpHu0Y-peRuyXPBO-o7_NsMurnI/edit#gid=1067183673")
        os.system(r'start excel "{}\onedrive\documents\amplify-55X8f_accessKeys"'.format(osi.gcu()))
        for categoryID in categoryIDs:
            category = self.categories[int(categoryID)]
            self.workflow_ui.pp(
                f"removing the selected categories form amplify 🗑️:{category}")
            os.system(f"amplify remove {category}")
            self.workflow_ui.pp(
                f"adding a new category to amplify ⭐ category:{category}")
            os.system(f"amplify add {category}")
            self.workflow_ui.pp("checking the amplify status 🔍")
            os.system("amplify status")
            self.workflow_ui.pp(
                f"adding a new category to amplify ⭐ category:{category}")
            self.workflow_ui.pp(f"pushing to amplify ✏️")
            os.system("amplify push")
            self.workflow_ui.pp(f"pull locally ⤵️")
            os.system("amplify pull")


    def modify_amplify_application(self, *categoryIDs):
        '''modify_amplify_application will;
        1. add each category selected through the category ids
        2. check the amplify status between each addition
        3. push the changes to the amplify application
        4. pull the changes to the local backend

        ---
        Params:
        - categoryIDs : list or strings, this will be turned into a list of integers and used to access the desired
        category from the categories list

        ---
        Returns: 
        - None
        '''
        categoryIDs = categoryIDs[0]
        os.system(
            "start https://docs.google.com/spreadsheets/d/1bVORUU7gE_fYZW1FjpHu0Y-peRuyXPBO-o7_NsMurnI/edit#gid=1067183673")
        os.system(r'start excel "{}\onedrive\documents\amplify-55X8f_accessKeys"'.format(osi.gcu()))
        for categoryID in categoryIDs:
            category = self.categories[int(categoryID)]
            self.workflow_ui.pp(
                f"adding a new category to amplify ⭐ category:{category}")
            os.system(f"amplify add {category}")
            self.workflow_ui.pp("checking the amplify status 🔍")
            os.system("amplify status")
            self.workflow_ui.pp(
                f"adding a new category to amplify ⭐ category:{category}")
            self.workflow_ui.pp(f"pushing to amplify ✏️")
            os.system("amplify push")
            self.workflow_ui.pp(f"pull locally ⤵️")
            os.system("amplify pull")

    def initialize_amplify_application(self, *categoryIDs):
        categoryIDs = categoryIDs[0]
        os.system(
            "start https://docs.google.com/spreadsheets/d/1bVORUU7gE_fYZW1FjpHu0Y-peRuyXPBO-o7_NsMurnI/edit#gid=1067183673")
        os.system(r'start excel "{}\onedrive\documents\amplify-55X8f_accessKeys"'.format(osi.gcu()))
        self.workflow_ui.pp("initialize a new amplify application 👶")
        os.system("amplify init")
        for categoryID in categoryIDs:
            category = self.categories[int(categoryID)]
            self.workflow_ui.pp(
                f"adding a new category to amplify ⭐ category:{category}")
            os.system(f"amplify add {category}")
            self.workflow_ui.pp("checking the amplify status 🔍")
            os.system("amplify status")
            self.workflow_ui.pp(
                f"adding a new category to amplify ⭐ category:{category}")
            self.workflow_ui.pp(f"pushing to amplify ✏️")
            os.system("amplify push")
            self.workflow_ui.pp(f"pull locally ⤵️")
            os.system("amplify pull")

    def sync_env_variable_to_aws_exports(self):
        AWS_CONFIG_DATA = []

        source_dir = os.path.join(os.getcwd(), "src")
        print(f"----------- looking for the aws-exports.js in {source_dir} 🔎")
        time.sleep(1)
        with open(f"{source_dir}/aws-exports.js", "r") as aws_config_file, open(f"{os.getcwd()}/aws-exports.json", "w") as write_file:
            content = aws_config_file.readlines()

            print("-------------------------- aws-export.js found ✅")
            print(aws_config_file.read())
            time.sleep(1)
            # filter the first three lines
            clean_content = list(
                filter(lambda line: content.index(line) > 3, content))
            clean_content.insert(0, "[{")

            # filter the last two lines
            clean_content = list(filter(lambda line: clean_content.index(
                line) < len(clean_content) - 2, clean_content))
            clean_content.append("}]")

            print("--------------------- cleaning up the file to make a json 🧹")
            time.sleep(1)

            for index, line in enumerate(clean_content):
                write_file.write(line)

        with open(f"{os.getcwd()}/aws-exports.json", "r") as read_config_file:
            content: 'list[dict]' = json.loads(read_config_file.read())
            keys = list(content[0].keys())

            print(
                f"----------------------- converting the parsed dictionary to .env variables ⚙️")
            time.sleep(1)
            print(content[0])

            print("------------------------  ---> ")
            for k in keys:
                upper_k = k.upper()
                AWS_CONFIG_DATA.append(
                    f'REACT_APP_{upper_k} = "{content[0][k]}"')
            print(f'REACT_APP_{upper_k} = "{content[0][k]}"')

        print("------------------------------- getting the current .env file ✅")
        time.sleep(1)
        with open(".env", "r+") as env_file:
            content = env_file.readlines()
            clean_content = list(
                filter(lambda line: line.find("REACT_APP_AWS") == -1, content))
            for line in clean_content:
                print(line)

            for variable in AWS_CONFIG_DATA:
                clean_content.append(variable)

        print("---------------------------- writing to the final .env file ✏️")
        time.sleep(1)
        with open(".env", "w") as write_to_env_file:
            clean_content = list(set(clean_content))
            for line in clean_content:
                line = line.replace("\n", "")
                print(line)
                write_to_env_file.write(f'{line}\n')
            os.remove("aws-exports.json")

    def push_to_amplify(self,*args):
        '''
        In order to publish to amplify make sure that you have initialised the correct application
        and that the repository is bering configure

        According to the documentation after adding the hosting category you can commit by running amplify push
        ---
        ```cmd
        amplify push
        ```
        '''
        target_directory = os.getcwd()
        self.workflow_ui.pp(f"cd into --> {target_directory} 🚕")
        os.chdir(target_directory)
        self.workflow_ui.pp("running tests using npm 🧪")
        os.system("npm test")
        self.workflow_ui.pp("formatting code using prettier ✨")
        os.system("prettier -w .")
        result = input("are you satisfied with the result of the tests? (y/n):")
        if result == "y":
            self.workflow_ui.pp("the tests have passed so we can push to github ✅")
            os.system("git pull")
            os.system("git add . ")
            os.system('git commit -m "make it better"')
            os.system("git push ")
            self.workflow_ui.pp("publishing the application to amplify ✅")
            os.system("amplify publish")
        
        self.workflow_ui.pp("workflow completed successfully ✅")

class ReactApplication(object):

    def __init__(self) -> None:
        self.workflow_ui = WorkflowRepresentation()

    def initialise_env_file(self, *args):
        with open(".env", "w") as env, open(os.path.join(osi.gcu(), "Protocol", "jaguar", "config.py"),"r") as configs:
            content = configs.read()
            env.write(content)

    def initialise_npm_process(self, *args) -> None:
        '''signature description'''

        target_directory = os.getcwd()
        self.workflow_ui.pp(f"cd into --> {target_directory} 🚕")
        os.chdir(target_directory)
        
        self.workflow_ui.pp(f"clone react project -> {args[0]} ⤵️")
        os.system(f"git clone https://github.com/kesler20/{args[0]}")

        self.workflow_ui.pp("pull resent changes from github ↪️")
        os.system("git pull")
        self.workflow_ui.pp(
            " making sure that the npm packages are installed ⚙️")
        os.system("npm i")
        self.workflow_ui.pp("starting the application")
        os.system("npm start")

class GithubRepository(object):
    '''This is a representation of your directory according to github'''

    def __init__(self) -> None:
        self.workflow_ui = WorkflowRepresentation()

    def test_and_push_to_github(self, *args) -> None:
        '''test_and_push_to_github will:
        1. cd into target_directory
        2. git pull the latest changes from github
        3. run the tests, depending on whether is a python or javascript repo:
        - jest for javascript
        - pytest for python
        4. code formatting using prettier
        5. push the changes to github with the custom message

        you can call this method by running:
        ```bash
        python workflow.py "git" "t" "py" "t commit message for changing test code"
        ```
        ---
        Params:
        - _type - str : this can be py or js and it dictates what types of tests are run 
        - target_directory - str : this is the directory which the os will cd into

        ---
        Returns:
        - None
        '''
        _type = "py"
        commit_message = "c make it better (untested)"
        target_directory = os.getcwd()
        if len(args) == 0:
            pass
        elif len(args) == 1:
            _type = args[0]
        elif len(args) == 2:
            _type = args[0]
            commit_message = args[1]
        else:
            _type = args[0]
            commit_message = args[1]
            target_directory = args[2]

        self.workflow_ui.pp(f"cd into --> {target_directory} 🚕")
        os.chdir(target_directory)
        self.workflow_ui.pp(f"pull recent changes from github 😼⤵️")
        os.system("git pull")

        if _type == "js":
            self.workflow_ui.pp("running tests using npm ☕Script 🧪")
            os.system("npm test")

        if _type == "py":
            self.workflow_ui.pp("running tests using pytest 🐍🧪")
            os.system("python -m pytest src/tests")
            self.workflow_ui.pp("checking types 🐍📰")
            os.system("mypy src")
        
        self.workflow_ui.pp("formatting code using prettier ✨")
        os.system("prettier -w .")
        
        test_result = input("have all the tests passed? (y/n):")
        if test_result == "y":
            self.workflow_ui.pp(
                "the tests have passed so we can push to github ✅")
            os.system("git add . ")
            os.system(
                f'git commit -m "{self.style_commit_message(commit_message)}"')
            os.system("git push ")
        else:
            self.workflow_ui.pp("workflow completed without pushing ❌")

    def push_to_github(self, *args) -> None:
        '''signature description'''
        commit_message = "c make it better (untested)"
        if len(args[0][0]) > 1:
            commit_message = args[0][0]
        target_directory = os.getcwd()

        self.workflow_ui.pp("pushing untested code 😞")
        self.workflow_ui.pp(f"cd into --> {target_directory} 🚕")
        os.chdir(target_directory)
        os.system("git pull")
        os.system("git add . ")
        os.system(f'git commit -m "{self.style_commit_message(commit_message)}"')
        os.system("git push ")
    
    def push_new_repo_to_github(self, *args) -> None:
        '''signature description'''
        args = args[0]
        target_directory = os.getcwd()

        if len(args) == 1:
            self.push_new_branch_to_github(target_directory)
        
        self.workflow_ui.pp("making a new folder 📁")
        os.system(f"mkdir {target_directory}")
        self.workflow_ui.pp("initializing a new github repository ➡️")
        os.chdir(target_directory)
        os.system("git init")
        os.system("git add . ")
        os.system(f'git commit -m "{self.style_commit_message("c first commit")}"')
        self.workflow_ui.pp("now you can publish the branch from VS Code")
        os.system(f"start code {target_directory}")
    
    def push_new_branch_to_github(self, target_directory):
        os.chdir(target_directory)
        self.workflow_ui.pp("making a new branch 🌳")
        os.system("git checkout -b new-feature")
        os.system("git add . ")
        os.system(f'git commit -m "{self.style_commit_message("c add new feature")}"')
        self.workflow_ui.pp("publishing the new branch to github ⌚")
        os.system(f"git push --set-upstream origin new-feature")

    # internal function
    def style_commit_message(self, commit_message: str) -> str:
        # this is to make commit messages more interesting
        code_commit_message_emojis = ["😕", "⭐", "✊", "🤝", "👐"]
        if commit_message.startswith("t "):
            message_prefix = "test:"
            message_suffix = "🧪"
            commit_message = commit_message.replace("t ", " ")

        elif commit_message.startswith("d "):
            message_prefix = "documentation:"
            message_suffix = "📰"
            commit_message = commit_message.replace("d ", " ")

        elif commit_message.startswith("c "):
            message_prefix = "code:"
            message_suffix = code_commit_message_emojis[randint(
                0, len(code_commit_message_emojis) - 1)]
            commit_message = commit_message.replace("c ", " ")
        
        elif commit_message.startswith("TODO:"):
            message_prefix = ""
            message_suffix = "🔴🔴🔴"
            
        else:
            message_prefix = ""
            message_suffix = ""

        return message_prefix + commit_message + message_suffix


if __name__ == "__main__":
    amplify = AmplifyApplication()
    react = ReactApplication()
    git = GithubRepository()
    workflow_ui = WorkflowRepresentation()
    synch = FileSynchronizer()

    if sys.argv[1] == "git":
        if sys.argv[2] == "t":
            git.test_and_push_to_github(*sys.argv[argument_number:])
        elif sys.argv[2] == "init":
            git.push_new_repo_to_github(sys.argv[argument_number:])
        else:
            git.push_to_github(*sys.argv[argument_number:])

    elif sys.argv[1] == "aws":
        if sys.argv[2] == "init":
            amplify.initialize_amplify_application(sys.argv[argument_number:])
        elif sys.argv[2] == "edit":
            amplify.modify_amplify_application(sys.argv[argument_number:])
        elif sys.argv[2] == "u":
            amplify.update_amplify_application(sys.argv[argument_number:])
        elif sys.argv[2] == "sync":
            amplify.sync_env_variable_to_aws_exports(sys.argv[argument_number:])
        elif sys.argv[2] == "publish":
            amplify.push_to_amplify(sys.argv[argument_number:])
        else:
            workflow_ui.describe("aws")
            print("these are the categories that you can select")
            for index, category in enumerate(amplify.categories):
                print(f"{index} : ", category)

    elif sys.argv[1] == "react":
        if sys.argv[2] == "init":
            react.initialise_npm_process(*sys.argv[argument_number:])
        elif sys.argv[2] == "config":
            react.initialise_env_file(*sys.argv[argument_number:])
        else:
            print(
                'running python workflow.py "react" "config" will paste the .env file in the root dir')
            print(
                'running python workflow.py "react" "init" will initialize the react application')

    elif sys.argv[1] == "sync":
        synch.synchronize_files_from_jaguar(sys.argv[1:])

    elif sys.argv[1] == "push":
        for dir in os.listdir(r"C:\Users\Uchek\protocol"):
            with OperatingSystemInterface(os.path.join(r"C:\Users\Uchek\protocol", dir)) as op_sys:
                op_sys.system("python workflow.py g")

    elif sys.argv[1] == "install":
        workflow_ui.pp("INSTALLING JAGUAR <😼⏬>")
        # now you can push all of the changes to github within the protocol folder as follows
        for dir in os.listdir(r"C:\Users\Uchek\protocol"):
            if dir == "jaguar":
                pass
            else:
                with OperatingSystemInterface(os.path.join(r"C:\Users\Uchek\protocol", dir)) as op_sys:
                    # simulate that you are in the sofia silent folder
                    op_sys.system("mkdir interfaces")
                osi = OperatingSystemInterface(
                    os.path.join(r"C:\Users\Uchek\protocol", dir))
                osi.copy_file_from_folder(r"interfaces\os_interface.py")
                osi.copy_file_from_folder("workflow.py")

    elif sys.argv[1] == "-h":
        with open("commands.txt", "r") as f:
            for line in f.readlines():
                print(line)

    elif sys.argv[1] == "copy":
        folders = []
        files = []
        for arg in sys.argv[2:]:
            if arg.startswith("f "):
                files.append(arg)
            else:
                folders.append(arg)
        files = [file.replace("f ","") for file in files]
        for dir in folders:
            if dir == "jaguar":
                pass
            else:
                for file in files:
                    osi = OperatingSystemInterface(
                        os.path.join(r"C:\Users\Uchek\protocol", dir))
                    osi.copy_file_from_folder(r"{}".format(file))

    else:
        git.push_to_github(sys.argv[1:])

    