class SuperList(list):
	def __len__(self):
		return 5000


checkList = SuperList()
print(len(checkList))
print(issubclass(SuperList, list))