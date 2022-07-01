# Gesture Tracking for Low-End Virtual Reality Systems (GT4LEVRS)

GT4LEVRS project is an improvement to an open-source virtual reality headset.
The goal is to forster the popularization of virtual reality (VR) applications in low-income countries, such as Brazil, providing a piece of VR software that runs affordable and low-cost computers, i.e., those that do not have a GPU or oder hardware accelerator.

One of the barriers to total imersion and simulation for virtual reality headsets are the controllers, which are not capable of reproducing the high level of detail of the human hand movement. 
The project goal is to support VR users with a low-cost VR headset to interact with the virtual environment using only their hands. 
For that, a prototype of a computer vision system using a "regular" webcam was built to perform hand-pose estimation on the user hands. 
The hand-pose estimation is than transmited to a virtual environment developed in Unity. 
This is a simple prototype but it can be used as example on how to use the develope VR software.

A comparison between the developed systems and the commercial Leapmotion hand recognition system has been carried out.
We created a hand-pose estimation dataset consisting in a set of videos.
Each video shows a user making different sorts of gestures, i.e., static gestures, slow-moving gestures, and fast-moving gestures.

This project was created in the context of a bachelor's final thesis in the Computer Engineering course of Federal University of Technology - Paraná (UTFPR), campus Curitiba, by Lucas Kuttner Amin and Rafael Hideo Toyomoto supervised by Prof. Marco Wehrmeister.
In addition to the source code and the videos dataset, this work has evaluated qualitatively the advantages regarding the range of motion and interaction between the hands and disadvantages in the performance of image capture and processing.
Pros and cons of the propose VR software have been analysed and discussed.
The full text of this bachelor's theis (in Portuguese) can be found in http://repositorio.utfpr.edu.br/jspui/

Shield: [![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

---

# Quick Starting

## Requirements

- Python 3.6.x or superior
- Unity 3D 2020 or superior

## Opening and starting GT4LEVRS

Navigate into `handtracking` folder and open it as a python project (we used PyCharm IDE).

```Bash
cd handtracking
```

Install all requirements from `requirement.txt`.

```Bash
pip install -r requirements.txt
```


You can activate differents debugging modes by global flags configuration. Open the following script:

```
src/app/config.py
```

and change the values inside the class `DebugOption` as you wish.

Then, navigate into source folder:

```Bash
cd src
```

create a logs folder at running location, required for execution:

```Bash
mkdir logs
```

and run the runner script:

```Bash
python run.py
```

> If you are using PyCharm, you can create a running configuration with `src/app/main.py` script just running it. Remember, with that approach you will need create the `logs` folder on `src/app/` instead of `src/`.

This command starts your webcam and serves data at port 5555 for Unity example application.

## Running Unity Examples:

Open the Unity project inside `UnityProject` folder with Unity Editor.

Choose a scene inside the following folder:

```Bash
UnityProject/Assets/Scenes/
```

- `Test 3D Hand.unity` : Scene with 3D hand model tracked by data from python server 
- `Test Simple Hand.unity` : Scene with generated skeleton hands by data from python server

Sample hands model configured with GT4LEVRS listener script are on folliwing folder:

```
UnityProject/Assets/HandTrackingSystem/Prefabs/
```
