class LogAction():
    status = "status"
    talk = "talk"
    vote = "vote"
    divine = "divine"
    execute = "execute"
    attackVote = "attackVote"
    attack = "attack"
    result = "result"

    def is_status(action:str) -> bool:
        return LogAction.status == action
    
    def is_talk(action:str) -> bool:
        return LogAction.talk == action
    
    def is_vote(action:str) -> bool:
        return LogAction.vote == action
    
    def is_divine(action:str) -> bool:
        return LogAction.divine == action
    
    def is_execute(action:str) -> bool:
        return LogAction.execute == action
    
    def is_attack_vote(action:str) -> bool:
        return LogAction.is_attack_vote == action
    
    def is_attack(action:str) -> bool:
        return LogAction.attack == action
    
    def is_result(action:str) -> bool:
        return LogAction.result == action