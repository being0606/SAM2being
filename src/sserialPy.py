import serial
import time

# 포트와 보드레이트를 설정합니다.
ser = serial.Serial('/dev/tty.usbmodem1101', 9600)
time.sleep(2)  # 아두이노와의 초기 통신 안정화를 위해 잠시 대기

try:
    while True:
        command = input("Enter command (F for Forward, B for Backward, S for Stop): ").strip().upper()

        if command in ['F', 'B', 'S']:
            ser.write(command.encode())  # 명령을 아두이노로 전송
            print(f"Sent: {command}")
            
        # 아두이노로부터 응답을 받을 수도 있습니다.
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').strip()
            print(f"Received: {data}")

except KeyboardInterrupt:
    print("Program interrupted.")

finally:
    # 시리얼 포트를 닫습니다.
    ser.close()