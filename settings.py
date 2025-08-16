from pathlib import Path
import sys

# Get the absolute path of the current file
file_path = Path(__file__).resolve()

# Get the parent directory of the current file
root_path = file_path.parent

# Add the root path to the sys.path list if it is not already there
if root_path not in sys.path:
    sys.path.append(str(root_path))

# Get the relative path of the root directory with respect to the current working directory
ROOT = root_path.relative_to(Path.cwd())

# Sources
IMAGE = 'Image'
WEBCAM = 'Webcam'

SOURCES_LIST = [IMAGE, WEBCAM]

# Images config
IMAGES_DIR = ROOT / 'images'
DEFAULT_IMAGE = IMAGES_DIR / 'def.jfif'
DEFAULT_DETECT_IMAGE = IMAGES_DIR / 'def1.jpg'

# Videos config
VIDEO_DIR = ROOT / 'videos'
VIDEOS_DICT = {
    'video_1': VIDEO_DIR / 'video_1.mp4',
    'video_2': VIDEO_DIR / 'video_2.mp4',
    'video_3': VIDEO_DIR / 'video_3.mp4',
    'video_4': VIDEO_DIR / 'video_4.mp4',
    'video_5': VIDEO_DIR / 'video_5.mp4',
}

# ML Model config - **UPDATED TO POINT TO YOUR WASTE CLASSIFICATION MODEL**
MODEL_DIR = Path(r'C:\Users\gurup\Downloads\Waste-Classification-using-YOLOv8-main\Waste-Classification-using-YOLOv8-main\streamlit-detection-tracking - app\weights')
DETECTION_MODEL = MODEL_DIR / 'yolov8_waste.pt'  # <-- Your trained YOLOv8 waste classification model here

# Webcam device index
WEBCAM_PATH = 0
