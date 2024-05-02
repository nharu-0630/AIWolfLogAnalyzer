import os
import configparser
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

def initialize_role(agentRoleRate:dict, roleSet:set, agentName:str, agentRole:str) -> None:
    
    if agentRole not in roleSet:
        roleSet.add(agentRole)

    # for all agent
    for agentName in agentRoleRate:
        for role in roleSet:
            agentRoleRate[agentName][role] = 0

def initialize_agent(agentRoleRate:dict, roleSet:set, agentName:str, agentRole:str, day:int) -> None:

    if agentName not in agentRoleRate:
        agentRoleRate[agentName] = dict()
        agentRoleRate[agentName]["gameNum"] = 0
    
    if day == 0:
        agentRoleRate[agentName]["gameNum"] += 1
    
    initialize_role(agentRoleRate=agentRoleRate, roleSet=roleSet, agentName=agentName, agentRole=agentRole)

def analyze_log(inifile:configparser.ConfigParser, agentRoleRate:dict, roleSet:set, analyzeLogPath:str) -> None:
    currentGameRole = dict()    # key: agent name value: role

    with open(analyzeLogPath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            splitted_line = line.split(",")
            day = int(splitted_line[0])
            action = splitted_line[1]

            if LogAction.is_status(action=action):
                agentRole = Status.get_role(splitted_line=splitted_line)
                agentName = Status.get_aget_name(splitted_line=splitted_line, include_number=inifile.getboolean("agent","classify_by_number"))

                # set
                currentGameRole[agentName] = agentRole
                initialize_agent(agentRoleRate=agentRoleRate, roleSet=roleSet, agentName=agentName, agentRole=agentRole, day=day)

            elif LogAction.is_talk(action=action):
                pass
            elif LogAction.is_vote(action=action):
                pass
            elif LogAction.is_divine(action=action):
                pass
            elif LogAction.is_execute(action=action):
                pass
            elif LogAction.is_attack_vote(action=action):
                pass
            elif LogAction.is_attack(action=action):
                pass
            elif LogAction.is_result(action=action):
                winner = Result.get_winner(splitted_line=splitted_line)
                print(winner)

if __name__ == "__main__":
    configPath = "./res/config.ini"
    inifile = util.check_config(config_path=configPath)
    inifile.read(configPath,"UTF-8")

    agentRoleRate = dict()      # key: agent name value: (key: role value: win num)
    roleSet = set()             # keep role

    for log in os.listdir(inifile.get("log","path")):
        currentLog = inifile.get("log","path") + log
        analyze_log(inifile=inifile, agentRoleRate=agentRoleRate, roleSet=roleSet, analyzeLogPath=currentLog)
    
    print(agentRoleRate)