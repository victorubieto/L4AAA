# L4AAA Open Dataset
The Landmarks for Available Avatar Animations (L4AAA) Open Dataset is a publicly available database designed to assist developers in addressing the issue of limited datasets for 3D animation synthesis. Unlike 2D animation, the creation of 3D animation datasets cannot be achieved through human annotation alone. Accurate manual 3D annotation is a difficult task that requires either a well-equipped laboratory with 3D scans or the construction of a synthetic dataset, both of which come with their own challenges.

The goal of this project is to create a readily accessible dataset that can be continually improved through automation. This dataset operates under the assumption that the 3D avatar's render is realistic enough for a pose and hand recognizer to perceive it as a real person and process it accordingly. By directly linking landmarks with skeleton joint rotations, this dataset aims to make animation synthesis more seamless and efficient for developers.

The dataset can be obtained from the following [link](https://drive.google.com/file/d/1N-t9Pwn2POXmpsGL3vInL04HoXPsIXXd/view?usp=share_link). More information about the data and the distribution of the folders can be found in the README inside.

This work was presented as my final project (see [here](./MasterThesis.pdf)) in the Master of Computer Vision, Barcelona. It is also a key contribution in a tool designed for European SignON project (https://signon-project.eu/).

## Description & Usability
In this repository provides two different scripts for different related purposes:

- [createDDBB](./createDDBB.blend) is a Blender (.blend) script with the source code to generate the Database automatically. To use it, open it, go to the "Scripting" window in the top bar of Blender, and press the run button. Before that, make sure that you have a folder called "All Anims" where you add all the animations that you want to process for your Dataset.

- [animationsML](./animationsML.ipynb) is a Jupyter Notebook (.ipynb) script with the source code with several functions such as training, predicting, storing the model, plotting information... In this file, the code is separated in different cells and any jupyter compiler can execute them sepparately. First, use the last box that separates the Dataset in Train/Test/Validation. Make sure that all paths are correctly linked to your folders and that is it. Above each cell is explained if any input is required from user. 

## Acknowledgments
I would like to extend my gratitude to the following teams:

- [Mixamo](https://www.mixamo.com/) - An extensive web library of open-source 3D animations, it greatly expanded the range of motion and variety of this dataset.
- [Blender](https://www.blender.org/) - A free and open-source 3D creation software used for making animations, models, artwork, and more. It allowed us the render of the virtual avatar performing the animations.
- [Mediapipe](https://github.com/google/mediapipe) - An open-source library from Google with different ML pipelines. It allowed us to perform hand and body tracking, with high accuracy in recognising the virtual avatar.

Their tools and resources have been instrumental in the development of this project and I am deeply grateful for their support.

## License
This project is licensed under the Apache 2.0 License.
