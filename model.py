from ultralytics import YOLO
import cv2
import os

model = YOLO("best.pt")
print(model.names)
def detect_helmet(image_path):
    result = model(image_path)
    detections = {"with_helmet" : 0 , "without_helmet" : 0}
    for r in result:
        # bounding box image generate
        plotted_image = r.plot()


        output_path = os.path.join("static/uploads", os.path.basename(image_path)) # ye path decide krta hia..basename ka mtlb hai k jis trh /uploads/bike.jpg hai is mie se uplaods hata do bike.jpg rkh do ye iska kam hai
        cv2.imwrite(output_path, plotted_image) # ye save krta hai image..means k output path par plotted image save kro
        for box in r.boxes:
            class_id = int(box.cls[0])
            class_name = model.names[class_id]

            if class_name in detections:
                detections[class_name] += 1
    message = []
    if detections["with_helmet"] > 0:
        message.append(f'With Helmet: {detections["with_helmet"]}')
    if detections["without_helmet"] > 0:
        message.append(f'Without Helmet: {detections["without_helmet"]}')

    if not message:
        message.append("No Helmet Detected")

    return  ", ".join(message)

def detect_helmet_video(video_path):
    capture = cv2.VideoCapture(video_path)
    output_path = os.path.join("static/uploads" , os.path.basename(video_path))
    width = int(capture.get(3))
    height = int(capture.get(4))
    fps = int(capture.get(cv2.CAP_PROP_FPS))
    out = cv2.VideoWriter(output_path , cv2.VideoWriter_fourcc(*'mp4v') , fps , (width,height))
    while capture.isOpened():
        ret,frame = capture.read()
        if not ret:
            break

        result = model(frame)
        for r in result:
            frame = r.plot()
        out.write(frame)
    capture.release()
    out.release()

    return  output_path
