class Role():
	# villager team
	villager = "VILLAGER"
	villager_ja = "村人"
	seer = "SEER"
	seer_ja = "占い師"
	medium = "MEDIUM"
	medium_ja = "霊媒師"

	# werewolf team
	werewolf = "WEREWOLF"
	werewolf_ja = "人狼"
	possessed = "POSSESSED"
	possessed_ja = "狂人"

	# team
	villager_team = "Villager Team"
	villager_team_ja = "村人陣営"
	werewolf_team = "Werewolf Team"
	werewolf_team_ja = "人狼陣営"

	# role team
	_villager_team = set([villager, seer, medium])
	_werewolf_team = set([werewolf, possessed])
	
	# translation dict
	_role_table = {villager:villager_ja,seer:seer_ja,medium:medium_ja,
				possessed:possessed_ja, werewolf:werewolf_ja}
	
	def is_villager_team(role:str) -> bool:
		return role in Role._villager_team
	
	def is_werewolf_team(role:str) -> bool:
		return role in Role._werewolf_team 
	
	def is_villager(role:str) -> bool:
		return role == Role.villager
	
	def is_seer(role:str) -> bool:
		return role == Role.seer
	
	def is_possessed(role:str) -> bool:
		return role == Role.possessed
	
	def is_werewolf(role:str) -> bool:
		return role == Role.werewolf
	
	def is_exist_role(role:str) -> bool:
		return role in Role._role_table
	
	def is_exist_role_ja(role_ja:str) -> bool:
		return role_ja in Role._role_table.values()