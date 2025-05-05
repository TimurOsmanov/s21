#!/usr/bin/env python3
import os
import subprocess


def check_env() -> bool:
    try:
        my_env: str = os.environ["VIRTUAL_ENV"]
        init_env_dir: str = my_env.split("/")[-2]
        env_name: str = my_env.split("/")[-1]
        return True if init_env_dir == 'ex00' and env_name == 'shireeth' else False

    except Exception as e:
        print(f"ERROR: {e} - you run script from wrong env")
        return False


def run_sh_command(cmd_name: list, shell: bool = True) -> str:
    try:
        result: subprocess.CompletedProcess = subprocess.run(cmd_name, shell=shell, encoding='utf-8', capture_output=True)
        return result.stdout[:-1]
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")


def main() -> None:
    try:
        if check_env():
            run_sh_command(cmd_name=["echo 'beautifulsoup4==4.12.3\npytest==8.3.4\nrequests' > requirements.txt"])
            run_sh_command(cmd_name=['pip install -r requirements.txt'])
            disp_lib = run_sh_command(cmd_name=['pip freeze'])
            print(disp_lib)
            run_sh_command(cmd_name=['pip freeze > requirements.txt'])
            run_sh_command(cmd_name=["tar", "-cvf", "archive.tar", f'{os.environ["VIRTUAL_ENV"]}'], shell=False)

    except Exception as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()
