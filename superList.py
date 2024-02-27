#DUNDER MAGIC METHODS

class SuperList():
	def __init__(self, bhakticentre):
		bhakticentreList = {'Aecs Layout', 'Panathur', 'Kagadaspura', 'kanamangala', 'anjanagondahalli'}
		self.bhakticentre = bhakticentre
		self.bhakticentreList = bhakticentreList

class aecsBhaktiCentreLeader(SuperList):
	def __init__(self, name):
		super().__init__('AECSBhaktiCentre')
		self.name = 'HG Yugal Kishore Prabhuji'

	def __len__(name):
		return(1000)

aecs = aecsBhaktiCentreLeader(SuperList)
print(aecs.bhakticentreList)