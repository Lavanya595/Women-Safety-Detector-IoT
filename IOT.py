import RPi.GPIO as GPIO
from twilio.rest import Client

# Twilio configuration (replace with your real credentials from Twilio Console)
ACCOUNT_SID = "ACb1c2d3e4f5g6h7i8j9k0l1m2n3o4p5q"   # Example SID (AC + 32 chars)
AUTH_TOKEN = "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6"    # Example Token (32 chars hex)
TWILIO_PHONE = "+15005550006"                      # Twilio trial phone number
DEST_PHONE = "+919603631230"                       # Your phone number

# Set up the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set the GPIO pins for LED and Touch Sensor
LED_PIN = 27
TOUCH_SENSOR_PIN = 17

# Set up the LED pin as an output and the touch sensor pin as an input
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(TOUCH_SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Function to send SMS using Twilio
def send_sms(body):
    try:
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages.create(
            body=body,
            from_=TWILIO_PHONE,
            to=DEST_PHONE
        )
        print(f"SMS sent successfully! SID: {message.sid}")
    except Exception as e:
        print(f"Failed to send SMS: {str(e)}")

# Callback for touch sensor
def touch_sensor_callback(channel):
    if GPIO.input(TOUCH_SENSOR_PIN) == GPIO.HIGH:
        GPIO.output(LED_PIN, GPIO.HIGH)
        print("Touch detected! LED ON.")
        send_sms("ALERT: The girl is in DANGER! Reach her and HELP quickly.")
    else:
        GPIO.output(LED_PIN, GPIO.LOW)
        print("No touch detected! LED OFF.")

# Detect touch sensor state changes
GPIO.add_event_detect(TOUCH_SENSOR_PIN, GPIO.BOTH, callback=touch_sensor_callback, bouncetime=300)

try:
    while True:
        pass  # Keep running

except KeyboardInterrupt:
    print("Program stopped by user.")

finally:
    GPIO.cleanup()