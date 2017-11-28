import items


class NonPlayerCharacter():
	def __init__(self):
		raise NotImplementedError("Do not create raw NPC objects.")

	def __str__(self):
		return self.name


class Trader(NonPlayerCharacter):
	def __init__(self):
		self.name = "Trader"
		self.gold = 100
		self.inventory = [items.CrustyBread(),
						items.CrustyBread(),
						items.CrustyBread(),
						items.HealingPotion(),
						items.HealingPotion()]