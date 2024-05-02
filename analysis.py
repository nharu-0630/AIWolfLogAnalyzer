import os
import configparser
from lib import util
from lib.role import Role
from lib.count import GameResult
from lib.action import LogAction
from lib.column import (
    CommonColumn,
    Status,
    Talk,
    Vote,
    Divine,
    Execute,
    AttackVote,
    Attack,
    Result
)

def initialize_agent(agentGameResult:dict, appearRoleSet:set, agentName:str, agentRole:str, day:int) -> None:

    appearRoleSet.add(agentRole)

    if agentName not in agentGameResult:
        agentGameResult[agentName] = GameResult()

    if day == 0:
        agentGameResult[agentName].game_num_increment()
        agentGameResult[agentName].role_result(agentRole).allocated_num_increment()

def check_win_or_lose(agentGameResult:dict, currentGameRole:dict, winnerTeam:str):

    for agent in agentGameResult:
        agentRole = currentGameRole[agent]

        if Role.is_villager_team(role=agentRole):
            if winnerTeam == Role.villager_team:
                agentGameResult[agent].role_result(agentRole).win_num_increment()
            else:
                agentGameResult[agent].role_result(agentRole).lose_num_increment()
        else:
            if winnerTeam == Role.werewolf_team:
                agentGameResult[agent].role_result(agentRole).win_num_increment()
            else:
                agentGameResult[agent].role_result(agentRole).lose_num_increment()

def analyze_log(inifile:configparser.ConfigParser, agentGameResult:dict, appearRoleSet:set, analyzeLogPath:str) -> None:
    currentGameRole = dict()    # key: agent name value: role

    with open(analyzeLogPath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            splitted_line = line.split(",")
            day = CommonColumn.get_day(splitted_line=splitted_line)
            action = CommonColumn.get_action(splitted_line=splitted_line)

            if LogAction.is_status(action=action):
                agentRole = Status.get_role(splitted_line=splitted_line)
                agentName = Status.get_aget_name(splitted_line=splitted_line, include_number=inifile.getboolean("agent","classify_by_number"))

                # set
                currentGameRole[agentName] = agentRole
                initialize_agent(agentGameResult=agentGameResult, appearRoleSet=appearRoleSet, agentName=agentName, agentRole=agentRole, day=day)

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
                check_win_or_lose(agentGameResult=agentGameResult, currentGameRole=currentGameRole, winnerTeam=winner)

def print_result(agentGameResult:dict, appearRoleSet:set) -> None:
    print("Result".ljust(Role.get_max_role_name_length()) + "\t" + "Times", end="\t")
    print("Win", end="\t")
    print("Lose",end="\n\n")

    for agent in agentGameResult:
        print("Agent: " + agent)
        total_win = 0
        total_lose = 0

        for role in Role.get_appear_print_role_order(appear_role_set=appearRoleSet):
            print(role.ljust(Role.get_max_role_name_length()) + "\t" + str(agentGameResult[agent].role_result(role).allocated_num),end="\t")
            print(str(agentGameResult[agent].role_result(role).win_num),end="\t")
            print(str(agentGameResult[agent].role_result(role).lose_num))
            total_win += agentGameResult[agent].role_result(role).win_num
            total_lose = agentGameResult[agent].role_result(role).lose_num
        
        print("Total".ljust(Role.get_max_role_name_length()) + "\t" + str(agentGameResult[agent].game_num), end="\t")
        print(total_win,end="\t")
        print(total_lose,end="\n\n")

if __name__ == "__main__":
    configPath = "./res/config.ini"
    inifile = util.check_config(config_path=configPath)
    inifile.read(configPath,"UTF-8")

    agentGameResult = dict()    # key: agent name   value: GameResult
    appearRoleSet = set()       # role set

    for log in os.listdir(inifile.get("log","path")):
        currentLog = inifile.get("log","path") + log
        analyze_log(inifile=inifile, agentGameResult=agentGameResult, appearRoleSet=appearRoleSet, analyzeLogPath=currentLog)
    
    print_result(agentGameResult=agentGameResult, appearRoleSet=appearRoleSet)