import argparse
import os
from env import Django_Server  

def start_server():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    manage_path = os.path.join(base_dir, "manage.py")

    command = f"python3 {manage_path} runserver {Django_Server.host}:{Django_Server.port} &"
    
    if getattr(Django_Server, "settings", None):
        command += f" --settings={Django_Server.settings}"

    print("서버를 시작합니다...")
    os.system(command)
    print(f"{Django_Server.host}:{Django_Server.port}에서 Django 서버가 시작되었습니다.")
    command_result = f"head -n 30"
    os.system(command_result)

def kill_server():
    kill_command = f"lsof -t -i:{Django_Server.port} | xargs kill -9"
    print("서버를 종료합니다...")
    os.system(kill_command)
    print(f"{Django_Server.port} 포트에서 실행 중인 Django 서버가 종료되었습니다.")

parser = argparse.ArgumentParser(description="Django 서버 관리 스크립트")
subparsers = parser.add_subparsers(dest="command", help="사용할 명령어를 선택하세요.")

start_parser = subparsers.add_parser("start", help="Django 서버를 시작합니다.")

kill_parser = subparsers.add_parser("kill", help="Django 서버를 종료합니다.")

args = parser.parse_args()

if args.command == "start":
    start_server()
elif args.command == "kill":
    kill_server()
else:
    parser.print_help()
