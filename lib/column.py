from . import util

class CommonColumn():
    # day, action, index
    day = "day"
    action = "action"
    index = "index"

    column = {day:0, action:1, index:2}

    def __init_subclass__(cls) -> None:
        if hasattr(cls, "originalColumn"):
            # cls.column.update(getattr(cls,"originalColumn"))
            cls.column = dict(**cls.column,**getattr(cls,"originalColumn"))
        else:
            print(cls.__name__ + " has no \"originalColumn\"")
    
    @classmethod
    def get_day(cls, splitted_line:list) -> int:
        return int(splitted_line[cls.column[cls.day]])
    
    @classmethod
    def get_action(cls, splitted_line:list) -> str:
        return splitted_line[cls.column[cls.action]]

    @classmethod
    def get_index(cls, splitted_line:list) -> int:
        return int(splitted_line[cls.column[cls.index]])

class Status(CommonColumn):
    # day, action, index, role, alive or dead, agent name
    role = "role"
    state = "state"
    agent_name = "agent_name"

    originalColumn = {role:3, state:4, agent_name:5}

    @classmethod
    def get_role(cls, splitted_line:list) -> str:
        return splitted_line[cls.column[cls.role]]
    
    @classmethod
    def get_aget_name(cls, splitted_line:list, include_number:bool=False) -> str:

        if include_number:
            return splitted_line[cls.column[cls.agent_name]]

        return util.remove_number(text=splitted_line[cls.column[cls.agent_name]])
    
class Talk(CommonColumn):
    # day, action, index, agent_comment_index, agent_index, comment
    agent_comment_index = "agent_comment_index"
    agent_index = "agent_index"
    comment = "comment"

    originalColumn = {agent_comment_index:3, agent_index:4, comment:5}

class Vote(CommonColumn):
    # day, action, index, vote_target
    vote_target = "vote_target"

    originalColumn = {vote_target:3}

class Divine(CommonColumn):
    # day, action, index, divined_target, divine_result
    divined_target = "divined_target"
    divine_result = "divine_result"

    originalColumn = {divined_target:3, divine_result:4}

class Execute(CommonColumn):
    # day, action, executed_agent_index, executed_agent_role
    executed_agent_index = "executed_agent_index"
    executed_agent_role = "executed_agent_role"

    originalColumn = {executed_agent_index:2, executed_agent_role:3}

class AttackVote(CommonColumn):
    # day, action, vote_agent_index, attack_vote_target
    vote_agent_index = "vote_agent_index"
    attack_vote_target = "attack_vote_target"

    originalColumn = {vote_agent_index:2, attack_vote_target:3}

class Attack(CommonColumn):
    # day, action, attack_target, success_flag
    attack_target = "attack_target"
    success_flag = "success_flag"    

    originalColumn = {attack_target:2, success_flag:3}

class Result(CommonColumn):
    # day, action, villager_num, werewolf_num, winner
    villager_num = "villager_num"
    werewolf_num = "werewolf_num"
    winner = "winner"

    originalColumn = {villager_num:2, werewolf_num:3, winner:4}

    @classmethod
    def get_winner(cls, splitted_line:list) -> str:
        return splitted_line[cls.column[cls.winner]]