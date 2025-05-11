from face_evaluator import DeepFaceEvaluator
from chat_wrapper import ChatWrapper
from models.user_image import UserImage
from models.evaluation_report import EvaluationReport
from file_manager import FileManager
import os 
import sys
print(sys.path) 

if not os.path.exists("face_evaluator.py"):
    print("❗ Failas 'face_evaluator.py' nerastas.")
    exit()

def main():
    uploads_folder = "uploads"
    files = os.listdir(uploads_folder)
    
    if not files:
        print("❗ Pridėk bent vieną nuotrauką į 'uploads/' aplanką.")
        return

    image_path = os.path.join(uploads_folder, files[0])
    image = UserImage(image_path, "Jonas") 
    

    evaluator = DeepFaceEvaluator()
    score = evaluator.evaluate(image.file_path)

    report = EvaluationReport(image.user_name, score)

    chat = ChatWrapper()
    message = chat.generate_response(score)

    print(message)
    FileManager.save_report(report)

if __name__ == "__main__":
    main()
