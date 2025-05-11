from abc import ABC, abstractmethod
import random
from deepface import DeepFace

class FaceEvaluator(ABC):
    @abstractmethod
    def evaluate(self, image_path: str) -> int:
        pass

class DummyFaceEvaluator(FaceEvaluator):
    def evaluate(self, image_path: str) -> int:
        return random.randint(1, 10)

class DeepFaceEvaluator(FaceEvaluator):
    def evaluate(self, image_path: str) -> int:
        try:
            analysis = DeepFace.analyze(img_path=image_path, actions=['emotion'], enforce_detection=False)[0]
            emotions = analysis['emotion']
            happiness_score = emotions.get('happy', 0)
            score = int(happiness_score / 10) + 1
            return min(score, 10)
        except Exception as e:
            print(f"Klaida analizės metu: {e}")
            return 5

