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
	
	# print role order
	print_role_order = {1:villager, 2:seer, 3:medium, 4:werewolf, 5:possessed}
	
	def get_role_list() -> list:
		return Role._role_table.keys()
	
	def get_print_role_order() -> list:
		return list(Role.print_role_order.values())
	
	def get_appear_print_role_order(appear_role_set:set) -> list:
		all_role_order = Role.get_print_role_order()

		for role in all_role_order:
			if role not in appear_role_set:
				all_role_order.remove(role)

		return all_role_order

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