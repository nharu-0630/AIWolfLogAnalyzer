import os
from lib import util
from lib.action import LogAction
from lib.column import (
    Status,
    Talk,
    Vote,
    Divine,
    Execute,
    AttackVote,
    Attack,
    Result
)


def analyze_log(agentRoleRate:dict, roleSet:set, analyzeLogPath:str) -> None:
    currentGameRole = dict()    # key: agent name value: role

    with open(analyzeLogPath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            splitted_line = line.split(",")
            day = splitted_line[0]
            action = splitted_line[1]

            if(LogAction.is_status(action=action)):
                agentRole = Status.get_role(splitted_line=splitted_line)
                agentName = Status.get_aget_name(splitted_line=splitted_line)
                print(agentName + ":" + agentRole)
            elif(LogAction.is_talk(action=action)):
                pass
            elif(LogAction.is_vote(action=action)):
                pass
            elif(LogAction.is_divine(action=action)):
                pass
            elif(LogAction.is_execute(action=action)):
                pass
            elif(LogAction.is_attack_vote(action=action)):
                pass
            elif(LogAction.is_attack(action=action)):
                pass
            elif(LogAction.is_result(action=action)):
                pass

if __name__ == "__main__":
    configPath = "./res/config.ini"
    inifile = util.check_config(config_path=configPath)
    inifile.read(configPath,"UTF-8")

    agentRoleRate = dict()      # key: agent name value: (key: role value: win num)
    roleSet = set()             # keep role

    for log in os.listdir(inifile.get("log","path")):
        currentLog = inifile.get("log","path") + log
        analyze_log(agentRoleRate=agentRoleRate, roleSet=roleSet, analyzeLogPath=currentLog)