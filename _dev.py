from random import randint
import sys
import os
import time
import json
from typing import Any, Dict, List, Union
from pathlib import Path
import shutil
try:
    from src.jaguar_backend.operating_system_interface import OperatingSystemInterface
    from src.jaguar_backend.amplify_application import AmplifyApplication
    from src.jaguar_backend.react_application import ReactApplication
    from src.jaguar_backend.github_repository import GithubRepository
    from src.jaguar_backend._base import WorkflowRepresentation
except ModuleNotFoundError:
    from jaguar_backend.operating_system_interface import OperatingSystemInterface
    from jaguar_backend.amplify_application import AmplifyApplication
    from jaguar_backend.react_application import ReactApplication
    from jaguar_backend.github_repository import GithubRepository
    from jaguar_backend._base import WorkflowRepresentation

if __name__ == "__main__":
    osi = OperatingSystemInterface()
    amplify = AmplifyApplication()
    react = ReactApplication()
    git = GithubRepository()
    workflow_ui = WorkflowRepresentation()

    if len(sys.argv) > 1:
        if sys.argv[1] == "git":
            if len(sys.argv) > 2:
                if sys.argv[2] == "t":
                    git.test_and_push_to_github(sys.argv)
                elif sys.argv[2] == "init":
                    git.push_new_repo_to_github(sys.argv)
                elif sys.argv[2] == "merge":
                    try:
                        git.integrate_new_branch(sys.argv[3])
                    except:
                        git.integrate_new_branch()
                        
                elif sys.argv[2] == "gitignore":
                    git.generate_gitignore()
                else:
                    git.push_new_branch_to_github(sys.argv)

            else:
                print("try to run one of the following")
                print("python _dev.py git t py -> to run the tests ")
                print("python _dev.py git init <target_directory> -> to initialize a repo ")
                print("python _dev.py git <any> <target_directory> -> to initialize a new branch ")

        elif sys.argv[1] == "github":
            if sys.argv[2] == "issue":
                if sys.argv[3] == "create":
                    git.create_issue(sys.argv[4], sys.argv[5])

                elif sys.argv[3] == "read":
                    if len(sys.argv) >= 4:
                        git.read_issues()
                        # git.read_all_issues_on_github()
                    else:
                        git.read_issues()

                elif sys.argv[3] == "close":
                    # ["_dev.py","github","issue","close","from_val","to_val"]
                    if len(sys.argv) > 5:
                        git.close_issues(int(sys.argv[4]), int(sys.argv[5]))
                    else:
                        git.close_issue(sys.argv[4])
            elif sys.argv[2] == "describe":
                # ["_dev.py","github","issue","describe","description",("repository_name")]
                git.add_description_to_repo(sys.argv[3])
                if len(sys.argv) > 4:
                    git.add_description_to_repo(sys.argv[3], sys.argv[4])

            elif sys.argv[2] == "repos":
                if sys.argv[3] == "number":
                    git.list_repositories(number=sys.argv[4])
                elif sys.argv[3] == "language":
                    git.list_repositories(language=sys.argv[4])
                elif sys.argv[3] == "topic":
                    git.list_repositories(topic=sys.argv[4])
                elif sys.argv[3] == "visibility":
                    git.list_repositories(visibility=sys.argv[4])
                else:
                    # [dev.py,github,repos]
                    if len(sys.argv) < 3:
                        git.list_repositories()

            elif sys.argv[2] == "view":
                git.view_repository()

            elif sys.argv[2] == "topic":
                if sys.argv[3] == "add":
                    git.add_topic_to_repo(sys.argv[4])
                elif sys.argv[3] == "remove":
                    git.remove_topic_to_repo(sys.argv[4])
                else:
                    print("add")
                    print("remove")
            elif sys.argv[2] == "visibility":
                git.change_visibility(sys.argv[3])

            else:
                print("issue")
                print("describe")
                print("repos")
                print("view")

        elif sys.argv[1] == "readme":
            if sys.argv[2] == "create":
                git.create_issues_from_readme()
            if sys.argv[2] == "read":
                git.read_todos_from_readme()
            if sys.argv[2] == "cross":
                git.cross_todos_from_readme(sys.argv[3])
            else:
                workflow_ui.pp("apply the following methods to interact with the readme 📰")
                print("create -> to create issues from the readme")
                print("read -> to check all the readme todos")
                print("cross -> tick all the todos that have been completed by passing their title")

        elif sys.argv[1] == "aws":
            if sys.argv[2] == "init":
                amplify.initialize_amplify_application(sys.argv)
            elif sys.argv[2] == "edit":
                amplify.modify_amplify_application(sys.argv)
            elif sys.argv[2] == "u":
                amplify.update_amplify_application(sys.argv)
            elif sys.argv[2] == "publish":
                amplify.push_to_amplify(sys.argv)
            else:
                workflow_ui.describe("aws")
                print("these are the categories that you can select")
                for index, category in enumerate(amplify.categories):
                    print(f"{index} : ", category)

        elif sys.argv[1] == "react":
            if sys.argv[2] == "init":
                react.initialise_npm_process(sys.argv)
            elif sys.argv[2] == "config":
                react.initialise_env_file()
            else:
                print(
                    'running python workflow.py "react" "config" will paste the .env file in the root dir')
                print(
                    'running python workflow.py "react" "init" will initialize the react application')

        elif sys.argv[1] == "push":
            for dir in os.listdir(os.path.join(osi.gcu(), "protocol")):
                with OperatingSystemInterface(os.path.join(osi.gcu(), "protocol", dir)) as op_sys:
                    op_sys.system("python _dev.py g")

        elif sys.argv[1] == "install":
            workflow_ui.pp("INSTALLING JAGUAR <😼⏬>")
            # now you can push all of the changes to github within the protocol folder as follows
            for index, dir in enumerate(os.listdir(os.path.join(osi.gcu(), "protocol"))):
                if dir == "jaguar_backend":
                    pass
                else:
                    # with OperatingSystemInterface(os.path.join(osi.gcu(), "protocol", dir)) as op_sys:
                    #     try:
                    #         op_sys.system("rmdir /S /Q interfaces")
                    #         op_sys.system("del workflow.py")
                    #     except FileExistsError:
                    #         pass
                    osi = OperatingSystemInterface(os.path.join(osi.gcu(), "protocol", dir))
                    osi.copy_file_from_jaguar("_dev.py")
                    osi.copy_folder_from_jaguar(os.path.join("src", "jaguar_backend"))
                    if index + 1 == len(os.listdir(os.path.join(osi.gcu(), "protocol"))):
                        workflow_ui.pp("Installation completed 😇")

        elif sys.argv[1] == "copy":
            if sys.argv[2] == "file":
                if len(sys.argv) > 5:
                    osi.copy_file(sys.argv[3], sys.argv[4])
                else:
                    osi.copy_file(sys.argv[3])
            else:
                if len(sys.argv) > 5:
                    osi.copy_folder(sys.argv[3], sys.argv[4])
                else:
                    osi.copy_folder(sys.argv[3])

        elif sys.argv[1] == "delete":
            osi.delete_folder(sys.argv[2])

        elif sys.argv[1] == "test":
            git.run_tests(sys.argv)

        elif sys.argv[1] == "-h":
            with open(os.path.join(osi.gcu(), "protocol", "jaguar", "commands.txt"), "r") as f:
                for line in f.readlines():
                    print(line)

        elif sys.argv[1] == "create-app":
            if sys.argv[2] == "py":
                workflow_ui.pp("creating a new python application from its template 🐍✨")
                os.system("git clone https://github.com/kesler20/test_setup")
                application_dir = os.path.join(os.getcwd(), "test_setup")
                op_sys = OperatingSystemInterface(application_dir)
                os.system(f"rename test_setup {sys.argv[3]}")
                op_sys.replace_word_in_folder(
                    "template",
                    sys.argv[3],
                    os.path.join(os.getcwd(), sys.argv[3])
                )
                os.rename(
                    os.path.join(sys.argv[3], "src", "template"),
                    os.path.join(sys.argv[3], "src", sys.argv[3])
                )
                os.chdir(os.path.join(os.getcwd(), sys.argv[3]))
                os.system("pip install -e .")
                os.chdir(os.getcwd())

            else:
                workflow_ui.pp("creating a new javascript application from its template ☕✨")
                os.system("git clone https://github.com/kesler20/rta_template")
                application_dir = os.path.join(os.getcwd(), "rta_template")
                os.chdir(application_dir)
                os.system("npm install")
                os.chdir(os.getcwd())
                os.system(f"rename {os.path.join(os.getcwd(),'rta_template')} {os.path.join(os.getcwd(),sys.argv[3])}")

        elif sys.argv[1] == "typescript":
            if sys.argv[2] == "init":
                osi.initialise_typescript_environment()
            elif sys.argv[2] == "convert":
                osi.convert_javascript_files_to_typescript()
            else:
                print("init")
                print("convert")

        elif sys.argv[1] == "create-env":
            osi.create_a_virtualenvironment(sys.argv[2])
        
        elif sys.argv[1] == "i":
            osi.install_package(*sys.argv[2:])
        
        elif sys.argv[1] == "setup-env":
            osi.setup_venv(*sys.argv[2:])
        
        elif sys.argv[1] == "del-env":
            osi.delete_virtualenvironment(*sys.argv[2:])

        elif sys.argv[1] == "ci":
            git.test_and_push_to_github(["_dev.py","git","t",*sys.argv[2:]])

        else:
            # if no domain is passed this will be pushed to github
            git.push_to_github(sys.argv)
        
    else:
        with open(os.path.join(osi.gcu(), "Protocol", "jaguar", "commands.txt"), "r") as f:
            for line in f.readlines():
                print(line)
