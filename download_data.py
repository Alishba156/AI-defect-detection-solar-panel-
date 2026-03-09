from roboflow import Roboflow

# Key yahan nahi likhni, hum terminal se login karenge
rf = Roboflow()

project = rf.workspace("solar-panel-defect-detection").project("yolov8-4qenz")
version = project.version(1)

# Dataset download
dataset = version.download("yolov8")

print("Mubarak ho! Download shuru ho gaya hai.")