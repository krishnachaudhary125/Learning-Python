class MlModel:
	model_count = 0

	def __init__(self, name, accuracy):
		self.name = name
		self.accuracy = accuracy
		MlModel.model_count += 1

	def report(self):
		return f"{self.name}: {self.accuracy:.0%}"

	@classmethod
	def count(cls):
		return f"Models trained: {cls.model_count}"

	@staticmethod
	def is_acceptable(acc):
		return acc >= 0.80

m1 = MlModel("RandomForest", 0.80)
m2 = MlModel("SVM", 0.76)
print(m1.report())
print(MlModel.count())
print(MlModel.is_acceptable(0.88))