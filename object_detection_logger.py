import csv
import datetime
import isaacgym  # NVIDIA Isaac Sim package
import torch

class ObjectDetectionLogger:
    def __init__(self, log_file="detected_objects.csv"):
        self.log_file = log_file
        self.fields = ["Timestamp", "Object_ID", "Object_Name", "Position_X", "Position_Y", "Position_Z"]
        self.init_csv()

    def init_csv(self):
        """Initialize the CSV file with headers."""
        try:
            with open(self.log_file, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(self.fields)
            print(f"[INFO] Log file '{self.log_file}' initialized.")
        except Exception as e:
            print(f"[ERROR] Failed to initialize log file: {e}")

    def log_object(self, object_id, object_name, position):
        """Log detected object details into the CSV file."""
        try:
            with open(self.log_file, mode="a", newline="") as file:
                writer = csv.writer(file)
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                writer.writerow([timestamp, object_id, object_name, position[0], position[1], position[2]])
            print(f"[LOG] {object_name} (ID: {object_id}) logged at {position}.")
        except Exception as e:
            print(f"[ERROR] Failed to log object: {e}")

# Example Usage
if __name__ == "__main__":
    logger = ObjectDetectionLogger()

    # Simulating object detection (Replace with actual Isaac Sim data)
    detected_objects = [
        (101, "Cube", (1.2, 3.4, 0.5)),
        (102, "Sphere", (0.6, 2.1, 1.0)),
        (103, "Cylinder", (2.0, 1.5, 0.8)),
    ]

    for obj in detected_objects:
        logger.log_object(obj[0], obj[1], obj[2])
