from jaguar_backend.operating_system_interface import OperatingSystemInterface
from pathlib import Path
import os
from typing import List, Any, Union, Dict, Optional, Tuple
from jaguar_backend.file import File
from jaguar_backend._base import WorkflowRepresentation
from random import randint


class GithubRepository:
    """GithubRepository is a class which allows you to
    both use the ``git`` and the ``gh`` cli tool"""

    def __init__(self) -> None:
        self.workflow_ui = WorkflowRepresentation()
        # init session
        self.__set_up()

    def __set_up(self) -> None:
        """The setup method is run once at the start of the session to
        set the root directory as the default repository for github"""
        os.system("gh repo set-default")

    def add_description_to_repo(self, description: str, repo: Optional[str] = None):
        """add a description to the given repo"""
        if repo is None:
            osi = OperatingSystemInterface()
            repo = osi.gcf()
        print(f'gh repo edit https://github.com/kesler20/{repo} --description "{description}"')
        os.system(f'gh repo edit https://github.com/kesler20/{repo} --description "{description}"')
        print(f"https://github.com/kesler20/{repo}")

    def run_tests(self, args: List[str]):
        """runs the tests found within the repository

        Parameters
        ---
        args : List[str]
            the last parameter is whether you want to
            run manual tests or not
            ``["_dev.py","test","py","manual"]``

        Example
        ---
        to run manual tests        
        ```bash
        python _dev.py "test" "py" "manual" "jaguar_backend"  
        ```

        to run automatic tests
        ```bash
        python _dev.py "test" "py"
        ```

        Returns
        ---
        None
        """
        _type = args[2]
        if _type == "py":
            if len(args) > 3:
                self.workflow_ui.pp("running manual tests in python 🐍 🧪 ⚙️")
                manual_test_folder = os.path.join(
                    __file__.split("jaguar_backend")[0],
                    "jaguar_backend",
                    "tests"
                )
                if len(args) > 4:
                    manual_test_folder = os.path.join(
                        __file__.split("protocol")[0],
                        "protocol",
                        args[4],
                        "tests"
                    )

                test_passed = []
                for test_file in os.listdir(manual_test_folder):
                    try:
                        print(os.path.join(manual_test_folder, test_file))
                        self.workflow_ui.pp(f"running the following test {test_file}")
                        os.system(f"python {os.path.join(manual_test_folder,test_file)}")
                        self.workflow_ui.pp(f"test passed at {test_file} ✅")
                        test_passed.append(test_file)
                        for test_file_passed in test_passed:
                            print("passed the following tests ✅", test_file_passed)
                    except:
                        self.workflow_ui.pp("ERROR found in:", test_file)
                        self.workflow_ui.pp(f"test passed at {test_file} ❌")
            else:
                self.workflow_ui.pp("running automatic tests in python 🐍 🧪 🤖")
                os.system("python -m pytest tests")
        else:
            self.workflow_ui.pp("running javascript tests using npm ☕ 🧪")
            os.system("npm tests")

    def list_repositories(
        self,
        number: Optional[int] = None,
        language: Optional[str] = None,
        topic: Optional[str] = None,
        visibility: Optional[str] = None
    ) -> None:
        """list_repositories
        this method allows to list repositories and filter them depending on conditions

        Parameters
        ---
        number : Optional[int] = None
            the number of repos to list
        language : Optional[str] = None
            the primary language of the repos that you want to display 
        topic : Optional[str] = None
            the topic to use to filter the repos
        visibility : Optional[str] = None
            filter the repos by visibility (private or public)

        Returns
        --
        None
        """
        self.workflow_ui.pp("checking the repos 🥂")
        if number is not None:
            print(f"gh repo list --limit {number} kesler20")
            os.system(f"gh repo list --limit {number} kesler20")
        if language is not None:
            print(f"gh repo list kesler20 --language {language}")
            os.system(f"gh repo list kesler20 --language {language}")
        if topic is not None:
            print(f"gh repo list kesler20 --topic {topic}")
            os.system(f"gh repo list kesler20 --topic {topic}")
        if visibility is not None:
            print(f"gh repo list kesler20 --visibility {visibility}")
            os.system(f"gh repo list kesler20 --visibility {visibility}")
        if number is None and language is None and topic is None and visibility is None:
            print("gh repo list kesler20")
            os.system("gh repo list kesler20")

    def view_repository(self):
        os.system("gh repo view --web")

    def add_topic_to_repo(self, topic: str):
        os.system(f"gh repo edit --add-topic {topic}")
        osi = OperatingSystemInterface()
        repo = osi.gcf()
        print(f"https://github.com/kesler20/{repo}")

    def remove_topic_to_repo(self, topic: str):
        os.system(f"gh repo edit --remove-topic {topic}")
        osi = OperatingSystemInterface()
        repo = osi.gcf()
        print(f"https://github.com/kesler20/{repo}")

    def generate_gitignore(self):
        root_dir = os.path.abspath(__file__.split("protocol")[0])

        self.workflow_ui.pp("initializing the node environment 🟢NJS")
        os.system("npm init")
        self.workflow_ui.pp("install the generate-gitignore globally and generate the gitignore 🔶.gitignore")
        os.system("npm install --global generate generate-gitignore")
        os.system("gen gitignore")

        with open(os.path.join(
            root_dir,
            "protocol",
            "jaguar",
            "git_ignore",
            ".gitignore"
        ), "r") as read_file, open(".gitignore", "a") as write_file:
            content = read_file.readlines()
            write_file.writelines(content)
            write_file.write("# mqtt client credentials\n")

        # append the mqtt credentials files
        with open(".gitignore", "a") as append_file:
            for file_name in os.listdir(os.path.join(
                root_dir,
                "protocol",
                "jaguar",
                "test_iot_client_credentials"
            )):
                append_file.write(f"{file_name}\n")
        os.system("del package.json")

    def change_visibility(self, visibility: str):
        os.system(f"gh repo edit --visibility {visibility}")
        osi = OperatingSystemInterface()
        repo = osi.gcf()
        print(f"https://github.com/kesler20/{repo}")

    def create_issue(self, title: str, detail: Optional[str] = None) -> None:
        print(title)
        if detail is None:
            os.system(f'gh issue create --title "{title}" --body "{title}"')
        else:
            os.system(f'gh issue create --title "{title}" --body "{detail}"')

    def read_issues(self) -> List[str]:
        os.system("gh issue list")

    def close_issues(self, from_val: int, to_val: int) -> None:
        for issueID in range(from_val, to_val + 1):
            os.system(f"gh issue close {issueID}")

    def close_issue(self, issueID: int) -> None:
        os.system(f"gh issue close {issueID}")

    def integrate_new_branch(self, trunk_branch_name: str =None) -> None:
        """integrate_new_branch

        Note
        ---
        before running this method make sure that all the tests are passing

        this method will:
        1. checkout to master
        2. pull the latest changes
        3. checkout to the new-feature branch
        4. pull the latest changes
        6. merge the new-feature to master
        7. push to master
        8. delete the branch locally
        9. delete the branch origin
        """
        if trunk_branch_name is None:
            trunk_branch_name = "master"
        self.workflow_ui.pp("checking out to master to pull the latest changed ⏬")
        os.system(f"git checkout {trunk_branch_name}")
        os.system("git branch")
        os.system(f"git pull origin {trunk_branch_name}")
        self.workflow_ui.pp("checking out to new-feature to pull the latest changed ⏬⏬")
        self.workflow_ui.pp("")
        os.system("git checkout new-feature")
        os.system("git branch")
        os.system("git pull")
        os.system("git add .")
        os.system('git commit -m "ready to merge"')
        os.system('git push --set-upstream origin new-feature')
        self.workflow_ui.pp(f"checking out to {trunk_branch_name} to merge the new changes 👯‍♂️⭐💱")
        self.workflow_ui.pp("")
        os.system(f"git checkout {trunk_branch_name}")
        os.system("git branch")
        os.system("git merge new-feature")
        self.workflow_ui.pp(f"pushing the {trunk_branch_name} with the new feature ⤴️🤩✨")
        self.workflow_ui.pp("")
        os.system("git add .")
        os.system('git commit -m "merged new-feature"')
        os.system(f"git push origin {trunk_branch_name}")
        self.workflow_ui.pp("deleting the new-feature branch locally and on gh🎯🗑️")
        self.workflow_ui.pp("")
        os.system("git branch -d new-feature")
        os.system("git push origin --delete new-feature")

    def create_issues_from_readme(self):
        readme = File(Path("README.md"))
        uncompleted_todos = readme.read_line_by_condition(lambda line: line.startswith("- [ ]"))
        for todo in uncompleted_todos:
            todo = todo.replace("- [ ] ", "")
            todo = todo.replace("\n", "")
            self.create_issue(todo)

    def read_all_issues_on_github(self):
        #TODO:
        self.workflow_ui.pp("reading all the issues that are still open 📑")
        os.system("gh repo list")
   
    def read_todos_from_readme(self):
        readme = File(Path("README.md"))
        uncompleted_todos = readme.read_line_by_condition(lambda line: line.startswith("- [ ]"))
        completed_todos = readme.read_line_by_condition(lambda line: line.startswith("- [x]"))
        for todos in completed_todos:
            title = todos.replace("- [x] ", "")
            print(f"✅ {title}")
            print("")
        for todos in uncompleted_todos:
            title = todos.replace("- [ ] ", "")
            print(f"❌ {title}")
            print("")

    def cross_todos_from_readme(self, title: str):
        readme = File(Path("README.md"))
        readme_content = readme.readlines()
        readme.write("")
        for line in readme_content:
            line = line.replace("\n", "")
            if line.find(title) != -1:
                line = line.replace("[ ]", "[x]")
            readme.append(line)

    def test_and_push_to_github(self, args: List[str]) -> None:
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
        Parameters:
        args 
            is of the following type 
        ``["filename", "git", "t", "py", "commit_message","target_directory"]``

        - _type - str : this can be py or js and it dictates what types of tests are run 
        - target_directory - str : this is the directory which the os will cd into

        ---
        Returns:
        - None
        '''
        _type = "py"
        commit_message = "c make it better (untested)"
        target_directory = os.getcwd()
        if len(args) == 3:
            pass
        elif len(args) == 4:
            _type = args[3]
        elif len(args) == 5:
            _type = args[3]
            commit_message = args[4]
        else:
            _type = args[3]
            commit_message = args[4]
            target_directory = args[5]

        self.workflow_ui.pp(f"cd into --> {target_directory} 🚕")
        os.chdir(target_directory)
        self.workflow_ui.pp(f"pull recent changes from github 😼⤵️")
        os.system("git pull")

        if _type == "js":
            self.workflow_ui.pp("running tests using npm ☕Script 🧪")
            os.system("npm test")

        if _type == "py":
            self.workflow_ui.pp("running tests using pytest 🐍🧪")
            os.system("pytest tests")
            self.workflow_ui.pp("checking that the system is type safe 👩‍🚀 🐍")
            os.system("python -m mypy src")

        self.workflow_ui.pp("formatting code using prettier ✨")
        os.system("prettier -w .")

        test_result = input("have all the tests passed? (y/n):")
        if test_result == "y":
            self.workflow_ui.pp(
                "the tests have passed so we can push to github ✅")
            os.system("git add . ")
            os.system(
                f'git commit -m "{self.__style_commit_message(commit_message)}"')
            os.system("git push ")
            os.system("echo https://github.com/kesler20?tab=repositories")
        else:
            self.workflow_ui.pp("workflow completed without pushing ❌")
            os.system("echo https://github.com/kesler20?tab=repositories")

    def push_to_github(self, args: List[str]) -> None:
        """push_to_github has the following params

        arg is of the following type ``["filename", "commit_message", "target_directory"]`` 
        """
        commit_message = "c make it better (untested)"
        target_directory = os.getcwd()
        if len(args) > 1:
            commit_message = args[1] if len(args[1]) > 1 else commit_message
        elif len(args) > 2:
            target_directory = args[2]
        else:
            pass

        self.workflow_ui.pp("pushing untested code 😞")
        self.workflow_ui.pp(f"cd into --> {target_directory} 🚕")
        os.chdir(target_directory)
        os.system("git pull")
        os.system("git add . ")
        os.system(
            f'git commit -m "{self.__style_commit_message(commit_message)}"')
        os.system("git push ")
        os.system("echo https://github.com/kesler20?tab=repositories")

    def push_new_repo_to_github(self, args: List[str]) -> None:
        """push_new_repo_to_github has the following params

        arg is of the following type ``["filename", "git", "init", "target_directory"]`` 
        """
        target_directory = os.getcwd()
        if len(args) >= 4:
            target_directory = args[3]

        self.workflow_ui.pp("making a new folder 📁")
        os.system(f"mkdir {target_directory}")
        self.workflow_ui.pp("initializing a new github repository ➡️")
        os.chdir(target_directory)
        os.system("git init")
        os.system("git add . ")
        os.system(
            f'git commit -m "{self.__style_commit_message("c first commit")}"')
        self.workflow_ui.pp("now you can publish the branch from VS Code")
        os.system(f'code "" "{target_directory}"')

    def push_new_branch_to_github(self, args: List[str]) -> None:
        """push_new_branch_to_github has the following params

        arg is of the following type ``["filename", "git", "-b", "target_directory"]`` 
        """
        target_directory = os.getcwd()
        if len(args) >= 4:
            target_directory = args[3]

        os.chdir(target_directory)
        self.workflow_ui.pp("making a new branch 🌳")
        os.system("git checkout -b new-feature")
        os.system("git add . ")
        os.system(
            f'git commit -m "{self.__style_commit_message("c add new feature")}"')
        self.workflow_ui.pp("publishing the new branch to github ⌚")
        os.system(f"git push --set-upstream origin new-feature")
        os.system("echo https://github.com/kesler20?tab=repositories")

    def __style_commit_message(self, commit_message: str) -> str:
        """style_commit_message has the following params

        Parameters
        ---

        commit_message str
            to be passed as parameter 2

        Returns
        ---
        result: str
        """
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
