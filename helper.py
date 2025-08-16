from ultralytics import YOLO
import streamlit as st
import cv2
import pafy
import settings

def load_model(model_path):
    """
    Loads a YOLOv8 model from the specified path (.pt file).
    """
    model = YOLO('weights/yoloooo.pt')
    return model

def display_tracker_options():
    display_tracker = st.radio("Display Tracker", ('Yes', 'No'))
    if display_tracker == 'Yes':
        tracker_type = st.radio("Tracker Type", ("bytetrack.yaml", "botsort.yaml"))
        return True, tracker_type
    return False, None

def _display_detected_frames(conf, model, st_frame, image, is_display_tracking=False, tracker=None):
    """
    Display detected objects on a video frame using YOLOv8.
    """
    image = cv2.resize(image, (720, int(720 * 9 / 16)))

    if is_display_tracking:
        result = model.track(image, conf=conf, persist=True, tracker=tracker)
    else:
        result = model.predict(image, conf=conf)

    res_plotted = result[0].plot()
    st_frame.image(res_plotted, caption='Detected Frame', channels="BGR", use_column_width=True)

def play_webcam(conf, model):
    source_webcam = settings.WEBCAM_PATH
    is_display_tracker, tracker = display_tracker_options()

    if st.sidebar.button('Detect Trash'):
        try:
            cap = cv2.VideoCapture(source_webcam)
            st_frame = st.empty()
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                _display_detected_frames(conf, model, st_frame, frame, is_display_tracker, tracker)
            cap.release()
        except Exception as e:
            st.sidebar.error("Error accessing webcam: " + str(e))

def play_youtube_video(conf, model):
    url = st.sidebar.text_input("YouTube video URL")
    is_display_tracker, tracker = display_tracker_options()

    if st.sidebar.button('Detect Trash'):
        try:
            video = pafy.new(url)
            best = video.getbest(preftype="mp4")
            cap = cv2.VideoCapture(best.url)
            st_frame = st.empty()
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                _display_detected_frames(conf, model, st_frame, frame, is_display_tracker, tracker)
            cap.release()
        except Exception as e:
            st.sidebar.error("Error loading video: " + str(e))

def play_stored_video(conf, model):
    video_key = st.sidebar.selectbox("Choose a video", list(settings.VIDEOS_DICT.keys()))
    is_display_tracker, tracker = display_tracker_options()

    if st.sidebar.button('Detect Trash in Video'):
        try:
            cap = cv2.VideoCapture(settings.VIDEOS_DICT[video_key])
            st_frame = st.empty()
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                _display_detected_frames(conf, model, st_frame, frame, is_display_tracker, tracker)
            cap.release()
        except Exception as e:
            st.sidebar.error("Error loading video: " + str(e))
