import serial

# 接続するポートを指定（必要に応じて変更）
PORT = "/dev/ttyUSB0"
BAUDRATE = 2400

def main():
    ser = serial.Serial(PORT, BAUDRATE, timeout=1)
    print(f"Connected to {PORT}")

    try:
        while True:
            data = ser.read(14)  # DE-5000 は約14バイト送信
            if data:
                print(data.hex())
                # ここで解析して人間が読める値に変換も可能
    except KeyboardInterrupt:
        print("終了します")
    finally:
        ser.close()

if __name__ == "__main__":
    main()
