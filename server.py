# import SimpleHTTPServer
# import SocketServer

# PORT = 8000

# Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

# httpd = SocketServer.TCPServer(("", PORT), Handler)

# print("serving at port", PORT)
# httpd.serve_forever()


from flask import Flask
import os
# import youtube_face_swap
import time
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


# @app.route('/morph')
# def morph():
#     # os.system("python test.py")
#     # process_video(in_filename="", out_filename="", keep_audio=False, down_scale=2)
#     #process_video("./temp/src_video.mp4", "output.mp4")
#     ts = time.time()
#     output_filename = str(int(ts))
#     youtube_face_swap.process_video(
#         in_filename="./temp/src_video_irinia1.mp4", out_filename=output_filename + ".mp4", keep_audio=False, down_scale=4)
#     return "morph"


# @app.route('/downloadVideo/<url>')
# def downloadVideo(url):
#     youtube_face_swap.download_video(url=url, start=42, stop=52)
#     return


@app.route('/uploadVideo')
def upload_video():
    filename = './temp/proc_video.avi'
    return send_file(filename, mimetype='image/gif')
    return "getVideo"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
