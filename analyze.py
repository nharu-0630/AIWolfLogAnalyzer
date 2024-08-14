import configparser
import math
import os

from lib import util
from lib.action import LogAction
from lib.column import (
    Attack,
    AttackVote,
    CommonColumn,
    Divine,
    Execute,
    Result,
    Status,
    Talk,
    Vote,
)
from lib.count import GameResult
from lib.role import Role


def initialize_agent(
    agentGameResult: dict, appearRoleSet: set, agentName: str, agentRole: str, day: int
) -> None:

    appearRoleSet.add(agentRole)

    if agentName not in agentGameResult:
        agentGameResult[agentName] = GameResult()

    if day == 0:
        agentGameResult[agentName].game_num_increment()
        agentGameResult[agentName].role_result(agentRole).allocated_num_increment()


def check_win_or_lose(agentGameResult: dict, currentGameRole: dict, winnerTeam: str):

    for agent in agentGameResult:
        agentRole = currentGameRole[agent]

        if Role.is_villager_team(role=agentRole):
            if winnerTeam == Role.villager_team:
                agentGameResult[agent].win_num_increment()
                agentGameResult[agent].role_result(agentRole).win_num_increment()
            else:
                agentGameResult[agent].lose_num_increment()
                agentGameResult[agent].role_result(agentRole).lose_num_increment()
        else:
            if winnerTeam == Role.werewolf_team:
                agentGameResult[agent].win_num_increment()
                agentGameResult[agent].role_result(agentRole).win_num_increment()
            else:
                agentGameResult[agent].lose_num_increment()
                agentGameResult[agent].role_result(agentRole).lose_num_increment()


def analyze_log(
    inifile: configparser.ConfigParser,
    agentGameResult: dict,
    appearRoleSet: set,
    analyzeLogPath: str,
) -> None:
    currentGameRole = dict()  # key: agent name value: role

    with open(analyzeLogPath, "r", encoding="utf-8") as f:
        for line in f:
            # print(line)
            line = line.rstrip("\n")
            splitted_line = line.split(",")
            day = CommonColumn.get_day(splitted_line=splitted_line)
            action = CommonColumn.get_action(splitted_line=splitted_line)

            if LogAction.is_status(action=action):
                agentRole = Status.get_role(splitted_line=splitted_line)
                agentName = Status.get_aget_name(
                    splitted_line=splitted_line,
                    include_number=inifile.getboolean("agent", "classify_by_number"),
                )

                # set
                currentGameRole[agentName] = agentRole
                initialize_agent(
                    agentGameResult=agentGameResult,
                    appearRoleSet=appearRoleSet,
                    agentName=agentName,
                    agentRole=agentRole,
                    day=day,
                )

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
                check_win_or_lose(
                    agentGameResult=agentGameResult,
                    currentGameRole=currentGameRole,
                    winnerTeam=winner,
                )


def print_result(
    inifile: configparser.ConfigParser, agentGameResult: dict, appearRoleSet: set
) -> None:
    f = None
    denominator = 1
    word_width = 20
    ratio_digit = 10

    if inifile.getboolean("log", "save_to_file"):
        f = open(inifile.get("log", "output_file_name"), "w")

    #   Result  Times   Win Lose
    if not inifile.getboolean("log", "ratio_flag"):
        print(
            f"{'Result':<{word_width}}\t{'Times':<{ratio_digit//2}}\t{'Win'}\t{'Lose'}",
            file=f,
        )
    else:
        print(
            f"{'Result':<{word_width}}\t{'Times':<{ratio_digit//2}}\t{'Win':<{ratio_digit}}\t\t{'Lose'}",
            file=f,
        )

    for agent in agentGameResult:
        print("Agent: " + agent, file=f)

        for role in Role.get_appear_print_role_order(appear_role_set=appearRoleSet):

            if inifile.getboolean("log", "ratio_flag"):
                ratio_digit = inifile.getint("log", "ratio_digit")
                denominator = agentGameResult[agent].role_result(role).allocated_num

            allocated_num = agentGameResult[agent].role_result(role).allocated_num
            win_num = round(
                agentGameResult[agent].role_result(role).win_num / denominator,
                ratio_digit,
            )
            lose_num = round(
                agentGameResult[agent].role_result(role).lose_num / denominator,
                ratio_digit,
            )

            if not inifile.getboolean("log", "ratio_flag"):
                win_num = int(win_num)
                lose_num = int(lose_num)
                print(
                    f"{role:<{word_width}}\t{allocated_num:<{ratio_digit//2}}\t{win_num}\t{lose_num}",
                    file=f,
                )
            else:
                # role total_times, win_num, lose_num
                print(
                    f"{role:<{word_width}}\t{allocated_num:<{ratio_digit//2}}\t{win_num:.{ratio_digit}f}\t{lose_num:.{ratio_digit}}",
                    file=f,
                )

        if inifile.getboolean("log", "ratio_flag"):
            denominator = agentGameResult[agent].game_num

        total_win = agentGameResult[agent].win_num
        total_lose = agentGameResult[agent].lose_num
        total_win_num = round(total_win / denominator, ratio_digit)
        total_lose_num = round(total_lose / denominator, ratio_digit)

        if not inifile.getboolean("log", "ratio_flag"):
            total_win_num = int(total_win_num)
            total_lose_num = int(total_lose_num)
            print(
                f"{'Total':<{word_width}}\t{agentGameResult[agent].game_num:<{ratio_digit//2}}\t{total_win_num}\t{total_lose_num}\n",
                file=f,
            )
        else:
            # Total game_total_times    win ose
            print(
                f"{'Total':<{word_width}}\t{agentGameResult[agent].game_num:<{ratio_digit//2}}\t{total_win_num:.{ratio_digit}f}\t{total_lose_num:.{ratio_digit}f}\n",
                file=f,
            )

    if inifile.getboolean("log", "save_to_file"):
        f.close()


def get_latest_logs(log_dir: str) -> list:
    log_files = []
    for root, _, files in os.walk(log_dir):
        for file in files:
            if file.endswith(".log") and "ERROR" not in file:
                log_files.append(os.path.join(root, file))
    log_files.sort(key=os.path.getmtime, reverse=True)
    return log_files


if __name__ == "__main__":
    configPath = "./res/config.ini"
    inifile = util.check_config(config_path=configPath)
    inifile.read(configPath, "UTF-8")

    agentGameResult = dict()  # key: agent name   value: GameResult
    appearRoleSet = set()  # role set

    log_files = get_latest_logs(inifile.get("log", "path"))

    for log in log_files:
        analyze_log(
            inifile=inifile,
            agentGameResult=agentGameResult,
            appearRoleSet=appearRoleSet,
            analyzeLogPath=log,
        )

    print_result(
        inifile=inifile, agentGameResult=agentGameResult, appearRoleSet=appearRoleSet
    )
