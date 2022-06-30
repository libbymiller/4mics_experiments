"""
 To control the pixel ring of the ReSpeaker microphone array
 Copyright (c) 2016-2017 Seeed Technology Limited.

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""
import apa102
from gpiozero import LED


class PixelRing:
    PIXELS_N = 12

    MONO = 1
    SPIN = 3
    ARC  = 5
    CUSTOM = 6

    def __init__(self):

        self.dev = apa102.APA102(num_led=self.PIXELS_N)
        self.power = LED(5)
        self.power.on()

    def show(self, data):
#       print("data",data)
        for i in range(self.PIXELS_N):
#           print("i",int(data[4*i + 1]),int(data[4*i + 2]),int(data[4*i + 3]))
            self.dev.set_pixel(i, int(data[4*i + 1]), int(data[4*i + 2]), int(data[4*i + 3]))

        self.dev.show()

    def off(self):
        self.show([0] * 4 * 12)

    def set_direction(self, angel):
        if angel < 0 or angel > 360:
            return

        position = int((angel + 15) % 360 / 30) % self.PIXELS_N
        new_pos = (position+6)%12
        print("POS",position,new_pos)
        p = []
        for i in range(0, self.PIXELS_N):
          if(i==new_pos): 
             p = p + [0, 0, 255, 0]
          else:
             p = p + [0, 0, 0, 0]

        pixels = p
#        pixels = [0,0,0] * self.PIXELS_N
#        pixels[position] = [0, 255, 0]
#        pixels  = [0, 0, position, 24 - position] * self.PIXELS_N
        self.show(pixels)
        return position


pixel_ring = PixelRing()

"""
if __name__ == '__main__':
    import time

    pixel_ring.spin()
    time.sleep(3)
    for level in range(4, 8):
        pixel_ring.arc(level)
        time.sleep(1)

    angel = 0
    while True:
        try:
            pixel_ring.set_direction(angel)
            angel = (angel + 30) % 360
            time.sleep(1)
        except KeyboardInterrupt:
            break

    pixel_ring.off()
"""
