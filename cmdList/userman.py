import base64 #加解密库
from colorama import Fore #彩色文字库
import json #解析和保存json配置文件
import pwinput #密码输入库
from textwrap import dedent #格式化输出库

__doc__ = "PyOS User Manager"

__usage__ = {
    "log": "Show current login user",
    "create": "Create a new user",
    "change": "Change current user password"
}

def execute(self,args):
    match args[0]:
        case "log":
            print(f"Now login: {Fore.GREEN}{self.user}")
        case "create":
            newname=input('Name: ')
            newpwd=pwinput.pwinput()
            if newname in self.names:
                print(f"{Fore.YELLOW}WARNING: The name was created!")
                return 
            self.cfg["accounts"][newname]=base64.b64encode(newpwd.encode("utf-8")).decode("utf-8")
            with open("config.json","w",encoding="utf-8") as f:
                json.dump(self.cfg,f,ensure_ascii=False,indent=4)
            print(f'{Fore.GREEN}Created successfully.')
        case "change":
            stpasswd = base64.b64decode(self.cfg["accounts"][self.user].strip()).decode("utf-8")
            oldpwd = pwinput.pwinput("Old Password: ")
            if oldpwd == stpasswd:
                newpwd = pwinput.pwinput("New Password: ")
                self.cfg["accounts"][self.user]=base64.b64encode(newpwd.encode("utf-8")).decode("utf-8")
                with open("config.json","r+",encoding="utf-8") as f:
                    json.dump(self.cfg,f,ensure_ascii=False,indent=4)
                print(f'{Fore.GREEN}Resetted successfully.')
            else:
                print(f"{Fore.RED}ERROR: Invalid username or password!")
            # elif self.usercho == "3":
                # oldname=input('OldName: ')
                # stpasswd = base64.b64decode(self.cfg["accounts"][oldname].strip()).decode("utf-8")
                # pwd=pwinput.pwinput()
                # if pwd==stpasswd and oldname in self.cfg["accounts"].keys() and oldname!="root":
                    # newname=input("NewName: ")
                    # del self.cfg["accounts"][oldname]
                    # self.cfg["accounts"][newname]=base64.b64encode(pwd.encode("utf-8")).decode("utf-8")
                    # with open("config.json","r+",encoding="utf-8") as f:
                        # json.dump(self.cfg,f,ensure_ascii=False,indent=4)
                    # print(f'{Fore.GREEN}Resetted successfully.')
                # else:
                    # print(f"{Fore.RED}ERROR: Invalid username or password!")
                # usermenu()