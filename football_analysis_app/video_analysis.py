import cv2
import torch
import numpy as np
import ultralytics

# Load pre-trained YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5x', pretrained=True)

def analyze_video(video_path):
    # Load video
    cap = cv2.VideoCapture(video_path)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    analysis_results = []
    
    for frame_idx in range(frame_count):
        ret, frame = cap.read()
        if not ret:
            break
        
        # Perform object detection
        results = model(frame)
        detected_objects = results.pandas().xyxy[0].to_dict(orient="records")
        
        # Process detected objects
        frame_analysis = {
            "frame_idx": frame_idx,
            "timestamp": frame_idx / fps,
            "objects": detected_objects
        }
        analysis_results.append(frame_analysis)
    
    cap.release()
    return analysis_results