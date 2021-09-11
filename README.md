# webvtt-thumbail-generator
webvtt thumbnail generator made using python

# Dependancies
- opencv
- numpy
- tqdm 

# How to Use

    py run.py {filename}
  
It will create a `Thumbnail` folder and will create `.vtt` and `.jpg` files according to the filename

# Example

    py run.py nature-underwater-dolphin-animal-aquarium-zoo-blue-104839-full.mp4

## Result
nature-underwater-dolphin-animal-aquarium-zoo-blue-104839-full_1.jpg
![dolphin](https://cdn.jsdelivr.net/gh/calvinanto/webvtt-thumbail-generator/Example/nature-underwater-dolphin-animal-aquarium-zoo-blue-104839-full_1.jpg)

<details>
<summary>nature-underwater-dolphin-animal-aquarium-zoo-blue-104839-full.vtt</summary>
  
    WEBVTT

    00:00:00.000 --> 00:00:01.000
    nature-underwater-dolphin-animal-aquarium-zoo-blue-104839-full_1.jpg#xywh=0,0,426,240

    00:00:01.000 --> 00:00:02.000
    nature-underwater-dolphin-animal-aquarium-zoo-blue-104839-full_1.jpg#xywh=426,0,426,240

    00:00:02.000 --> 00:00:03.000
    nature-underwater-dolphin-animal-aquarium-zoo-blue-104839-full_1.jpg#xywh=852,0,426,240

    00:00:03.000 --> 00:00:04.000
    nature-underwater-dolphin-animal-aquarium-zoo-blue-104839-full_1.jpg#xywh=1278,0,426,240

    00:00:04.000 --> 00:00:05.000
    nature-underwater-dolphin-animal-aquarium-zoo-blue-104839-full_1.jpg#xywh=1704,0,426,240

    00:00:05.000 --> 00:00:06.000
    nature-underwater-dolphin-animal-aquarium-zoo-blue-104839-full_1.jpg#xywh=0,240,426,240

    00:00:06.000 --> 00:00:07.000
    nature-underwater-dolphin-animal-aquarium-zoo-blue-104839-full_1.jpg#xywh=426,240,426,240

    00:00:07.000 --> 00:00:08.000
    nature-underwater-dolphin-animal-aquarium-zoo-blue-104839-full_1.jpg#xywh=852,240,426,240

    00:00:08.000 --> 00:00:09.000
    nature-underwater-dolphin-animal-aquarium-zoo-blue-104839-full_1.jpg#xywh=1278,240,426,240

    00:00:09.000 --> 00:00:10.000
    nature-underwater-dolphin-animal-aquarium-zoo-blue-104839-full_1.jpg#xywh=1704,240,426,240

    00:00:10.000 --> 00:00:11.000
    nature-underwater-dolphin-animal-aquarium-zoo-blue-104839-full_1.jpg#xywh=0,480,426,240

    00:00:11.000 --> 00:00:12.000
    nature-underwater-dolphin-animal-aquarium-zoo-blue-104839-full_1.jpg#xywh=426,480,426,240

    00:00:12.000 --> 00:00:13.000
    nature-underwater-dolphin-animal-aquarium-zoo-blue-104839-full_1.jpg#xywh=852,480,426,240

    00:00:13.000 --> 00:00:14.000
    nature-underwater-dolphin-animal-aquarium-zoo-blue-104839-full_1.jpg#xywh=1278,480,426,240

    00:00:14.000 --> 00:00:15.000
    nature-underwater-dolphin-animal-aquarium-zoo-blue-104839-full_1.jpg#xywh=1704,480,426,240

    00:00:15.000 --> 00:00:16.000
    nature-underwater-dolphin-animal-aquarium-zoo-blue-104839-full_1.jpg#xywh=0,720,426,240

    00:00:16.000 --> 00:00:17.000
    nature-underwater-dolphin-animal-aquarium-zoo-blue-104839-full_1.jpg#xywh=426,720,426,240

    00:00:17.000 --> 00:00:18.000
    nature-underwater-dolphin-animal-aquarium-zoo-blue-104839-full_1.jpg#xywh=852,720,426,240

    00:00:18.000 --> 00:00:19.000
    nature-underwater-dolphin-animal-aquarium-zoo-blue-104839-full_1.jpg#xywh=1278,720,426,240

    00:00:19.000 --> 00:00:20.000
    nature-underwater-dolphin-animal-aquarium-zoo-blue-104839-full_1.jpg#xywh=1704,720,426,240

    00:00:20.000 --> 00:00:21.000
    nature-underwater-dolphin-animal-aquarium-zoo-blue-104839-full_1.jpg#xywh=0,960,426,240

    00:00:21.000 --> 00:00:22.000
    nature-underwater-dolphin-animal-aquarium-zoo-blue-104839-full_1.jpg#xywh=426,960,426,240

    00:00:22.000 --> 00:00:23.000
    nature-underwater-dolphin-animal-aquarium-zoo-blue-104839-full_1.jpg#xywh=852,960,426,240

    00:00:23.000 --> 00:00:23.857
    nature-underwater-dolphin-animal-aquarium-zoo-blue-104839-full_1.jpg#xywh=1278,960,426,240
 </details>
 
# TODO
- Add more parameters
- Generate thumbnail at image location instead of code
- Creating GUI
