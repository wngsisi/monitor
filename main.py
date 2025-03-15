import cv2

def gstreamer_pipeline(
    capture_width=1280, 
    capture_height=720, 
    display_width=1280,
    display_height=720, 
    framerate=60,       
    flip_method=0,      
):
    return (
        "nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )

if __name__ == "__main__":
    capture_width = 1280
    capture_height = 720

    display_width = 1280
    display_height = 720

    framerate = 60			
    flip_method = 0			


    print(gstreamer_pipeline(capture_width,capture_height,display_width,display_height,framerate,flip_method))


    cap = CV2.VideoCapture(gstreamer_pipeline(flip_method=0), CV2.CAP_GSTREAMER)

    if cap.isOpened():
        window_handle = CV2.namedWindow("CSI Camera", CV2.WINDOW_AUTOSIZE)

        while CV2.getWindowProperty("CSI Camera", 0) >= 0:
            ret_val, img = cap.read()
            CV2.imshow("CSI Camera", img)

            keyCode = CV2.waitKey(30) & 0xFF
            if keyCode == 27:
                break

        cap.release()
        CV2.destroyAllWindows()
    else:
        print("open failed") 
