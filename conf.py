confpath = './YOLOv8_deepsort_count/ultralytics/yolo/v8/detect/maincfg.txt'
vid_names = ["rtsp://localhost:8554/live0.stream", "https://cam18.yar-net.ru/privokzalnaya_2/mono.m3u8?token=9c73ec3a163279527c89a1dfd8abfab9"]
outfile_names = ["out0", "out1"]
line0 = [(190, 669), (603, 152)]
line1 = [(312, 426), (570, 504)]
cfgdict = {
    'model': 'yolov8m.pt',
    'imgsz': 960,
    'line0': repr(line0),
    'line1': repr(line1),
    'source0': vid_names[0],
    'source1': vid_names[1],
    'outname0': outfile_names[0],
    'outname1': outfile_names[1],
}
