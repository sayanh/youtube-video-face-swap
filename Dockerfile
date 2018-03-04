FROM ubuntu:16.04

RUN apt update && apt-get install -y ffmpeg libx264-dev software-properties-common
RUN add-apt-repository -y ppa:deadsnakes/ppa && apt-get update && apt install -y python3.6 python3-pip cmake libfontconfig1 libxrender1 libsm6 libxext6

RUN mkdir -p /test && mkdir -p /youtube-video-face-swap && mkdir -p /youtube-video-face-swap/models
COPY 3_youtube_face_swap.py /youtube-video-face-swap/youtube_face_swap.py
COPY requirements.txt /youtube-video-face-swap/
COPY umeyama.py /youtube-video-face-swap/
COPY models /youtube-video-face-swap/models/
RUN pip3 install -r /youtube-video-face-swap/requirements.txt

COPY 1_get_faces_from_yt.py /youtube-video-face-swap/get_faces_from_yt.py
COPY face_extractor.py /youtube-video-face-swap/
COPY google_scraper.py /youtube-video-face-swap/
COPY utils.py /youtube-video-face-swap/
COPY model.py /youtube-video-face-swap/
COPY pixel_shuffler.py /youtube-video-face-swap/
CMD [ "/bin/bash", "-c", "python3", "server.py" ]