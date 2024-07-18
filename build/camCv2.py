import cv2
import numpy as np

# CUDAが有効なデバイスを確認
print(cv2.getBuildInformation())

# CUDAがサポートされているかチェック
if not cv2.cuda.getCudaEnabledDeviceCount():
    raise Exception("CUDAがサポートされていません")

# CUDAデバイスを設定
cv2.cuda.setDevice(0)

# カメラの設定 デバイスIDは0
cap = cv2.VideoCapture(0)

# 繰り返しのためのwhile文
while True:
    # カメラからの画像取得
    ret, frame = cap.read()
    
    # フレームをGPUにアップロード
    gpu_frame = cv2.cuda_GpuMat()
    gpu_frame.upload(frame)
    
    # カメラの画像を表示（GPUからCPUにダウンロード）
    frame = gpu_frame.download()
    cv2.imshow('camera', frame)
    
    # 繰り返し分から抜けるためのif文
    key = cv2.waitKey(10)
    if key == 27:  # ESCキー
        break

# メモリを解放して終了するためのコマンド
cap.release()
cv2.destroyAllWindows()
