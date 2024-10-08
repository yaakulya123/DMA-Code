import time
import board
import analogio
import neopixel
import digitalio
import audioio
import audiomp3

# Enable the pin (D10) for controlling power to the NeoPixel strip
enable = digitalio.DigitalInOut(board.D10)
enable.direction = digitalio.Direction.OUTPUT
enable.value = True  # Turn on the power

# Setup the photoresistor on A1
photoresistor = analogio.AnalogIn(board.A1)

# NeoPixel setup
pixel_pin = board.D5  # NeoPixel data pin
num_pixels = 12  # Number of pixels in the NeoPixel ring
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.5, auto_write=False)

# Output from external speaker
speaker = audioio.AudioOut(board.A0)

# Initialize the MP3 decoder with paths inside the "mang" folder
mp3_0 = audiomp3.MP3Decoder(open("mang/0.mp3", "rb"))
mp3_1 = audiomp3.MP3Decoder(open("mang/1.mp3", "rb"))

# Function to get light level from the photoresistor
def get_light_level():
    return photoresistor.value

# Function to blink NeoPixels in a color
def blink_color(color1, color2, delay):
    pixels.fill(color1)
    pixels.show()
    time.sleep(delay)
    pixels.fill(color2)
    pixels.show()
    time.sleep(delay)

# Function to play the given MP3 stream
def play_mp3(mp3stream):
    if not speaker.playing:
        speaker.play(mp3stream)
    # Restart the file if it's finished playing to loop continuously
    if not speaker.playing:
        mp3stream.file.seek(0)

# Function to stop any currently playing sound
def stop_sound():
    speaker.stop()

# Main loop
last_light_condition = None

while True:
    light_level = get_light_level()
    print("Light level:", light_level)
    
    # Define threshold to determine if the room is dark or bright
    if light_level < 2000:  # Dark room
        if last_light_condition != "dark":
            stop_sound()  # Stop any other sound that might be playing
            last_light_condition = "dark"
        
        blink_color((0, 0, 255), (255, 255, 255), 0.1)  # Blink Blue and White
        play_mp3(mp3_1)  # Play "1.mp3" from the "mang" folder
    
    else:  # Bright room
        if last_light_condition != "bright":
            stop_sound()  # Stop any other sound that might be playing
            last_light_condition = "bright"
        
        blink_color((255, 0, 0), (255, 165, 0), 0.1)  # Blink Red and Orange
        play_mp3(mp3_0)  # Play "0.mp3" from the "mang" folder

    time.sleep(0.1)  # Check every tenth of a second
