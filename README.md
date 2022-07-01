# 4mics_experiments
Some respeaker 4 mics experiments

I'm trying to estimate the direction of arrival (DoA) of sound with a [4 mic hat from respeaker](https://respeaker.io/4_mic_array/).

The [USB version of this hat](https://respeaker.io/usb_4_mic_array/) does it (see [this repo](https://github.com/respeaker/usb_4_mic_array.git) using [these instructions](https://wiki.seeedstudio.com/ReSpeaker-USB-Mic-Array/#doa-direction-of-arrival)). There's plenty of code around from respeaker but I couldn't find exactly what I wanted, which was to estimate both the direction and volume of the audio as a step towards seeing if it was a significant enough noise to pay attention to. I don't think this is enough - it perhaps needs some measure that there's a consistent noise - and a cutoff (though the cutoff would probably need some sampling of the ambient noise levels or something like that). Currently the the mic is "hearing" things I can't hear, or the calculations are wrong (or too approximate). I am not an expert.

The code here for the 4-mic hat uses [GCC-PHAT Cross-Correlation](http://www.xavieranguera.com/phdthesis/node92.html) which you can do with python and numpy, adapted from [this respaker repo](https://github.com/respeaker/mic_array/blob/master/mic_array.py#L88). I've added basic volume estimation [adapted from this stackoverflow answer](https://stackoverflow.com/questions/25868428/pyaudio-how-to-check-volume).

# Install

On a pi 3b - just happened to be what I had.

Set it up (I used Raspberry pi OS lite, buster (legacy))

Enable spi using `sudo raspi-config`

Install prerequisites. Might not need sudo for the pip3 but I ran it as sudo as I assumed spi needed it. Maybe not!

    sudo apt install git
    sudo apt install python3
    sudo apt install python3-pip
    sudo apt install python3-pyaudio 
    sudo pip3 install spidev gpiozero 

Then

    sudo apt-get update
    git clone https://github.com/respeaker/seeed-voicecard.git
    cd seeed-voicecard
    sudo ./install.sh
    sudo reboot
      
test with

    arecord -l
    
output is something like

    > arecord -l
     **** List of CAPTURE Hardware Devices ****
     card 1: seeed4micvoicec [seeed-4mic-voicecard], device 0: bcm2835-i2s-ac10x-codec0 ac10x-codec0-0 [bcm2835-i2s-ac10x-codec0 ac10x-codec0-0]
     Subdevices: 1/1
     Subdevice #0: subdevice #0
  
  
 Then 
 
     git clone https://github.com/respeaker/mic_array.git
     cd mic_array
     
 then checkout `mic_array_4mics.py` and `pixels_4mic.py` from this repo and copy them into that directory
 
 `sudo python3 mic_array.py` to run it
 
