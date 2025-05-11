import csv

class FileManager:
    @staticmethod
    def save_report(report, file_path='data/results.csv'):
        with open(file_path, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([report.user, report.score, report.timestamp])
