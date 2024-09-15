import time
import board
import neopixel

# Initialize the on-board RGB LED
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)

print("Running...")
print("Sending the info to the M4 Express")


# Define colors for different times of the day
SUNRISE = (255, 153, 51)  # Orange for sunrise
NOON = (135, 206, 250)    # Blue for noon
SUNSET = (255, 69, 0)     # Red for sunset
NIGHT = (25, 25, 112)     # Dark blue for night
STARS = (255, 255, 255)   # White for twinkling stars

print("Code Sent!")

print("Executing....")

# Time each color is displayed (seconds)
display_time = 7.5

# Set the initial brightness
pixel.brightness = 0.2

# Function to display a color for a specified duration with brightness
def display_color(color, duration, brightness):
    pixel.brightness = brightness
    pixel.fill(color)
    time.sleep(duration)

# Function to create a twinkling stars effect during the night
def twinkling_stars(duration, star_duration=0.1, base_brightness=0.1, star_brightness=0.3):
    end_time = time.monotonic() + duration
    while time.monotonic() < end_time:
        pixel.brightness = base_brightness
        pixel.fill(NIGHT)  # Night color
        time.sleep(star_duration)
        pixel.brightness = star_brightness
        pixel.fill(STARS)  # Twinkling star effect
        time.sleep(star_duration)

# Main loop to cycle through the day
while True:
    display_color(SUNRISE, display_time, 0.3)  # Sunrise with gentle brightness
    display_color(NOON, display_time, 0.8)     # Noon with full brightness
    display_color(SUNSET, display_time, 0.5)   # Sunset with medium brightness
    twinkling_stars(7.5)                       # Twinkling stars effect during the night
