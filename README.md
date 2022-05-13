# Vehicle detection, Classification and number plate Text Extraction
As a capstone project for PECE 3203 ( Image Processing Lab )
By-<br>
1 Samruddhi Deode <br>
2 Arundhati Korlahalli <br>
3 Akhila Nori



MOTIVATION
We often see that traffic signal durations are not dynamic. Even if there are very few vehicles on the road, they might have to wait for a really long time unnecessarily. This makes the drivers frustrated and leads to more people jumping the red signals or breaking traffic rules.
This problem motivated us to tackle the above listed problems using the concepts learnt through our Image Processing course. 
We have tried to capture a video of the on-ground traffic & analyze the vehicle density (we have also designed a mechanism to classify the vehicle to give an estimate of bus density, two wheeler and four wheeler density separately). This can be used to model the traffic signal duration at a particular time of the day according to the predicted vehicle density in that area.
If the vehicle owners still run red lights or not follow the traffic rules then they must be held accountable. So the number plate text extraction module helps to reveal the identity of the owner who engages in illegal behavior.

PROBLEM STATEMENT
Our project primarily focuses on 3 main aspects : <br>
i) Convert a on-ground traffic video into its constituent frames and extract vehicles from each frame. <br>
ii) Classify the extracted vehicles into various categories (like car, bus, motorcycle etc.) <br>
ii )Extract number plate text from detected vehicles. <br>

LEARNING OBJECTIVE <br>
We have learnt various image processing concepts throughout the semester.This project gave us an opportunity to apply the concepts to a real world problem.The objectives are as follows: <br>
1.Detect vehicles from a video and extract them using image enhancement, contouring,    smoothening etc. <br>
2. Categorize the extracted image using a trained  Machine learning model . <br>
3. Highlight the number plate from an image of a vehicle. This includes finding contours and applying arithmetic operations to the image. For extracting text, we used pytesseract. <br>
4. To analyze our solution to the problem and determine the scope of the project. Discuss applications and future scope. <br>

How to run the project? <br>
1. create folders Frames1, Frames2, cars, input and output.
2. Save video1 and video2 inside the input folder.
3. Create folders CARS, MOTORCYCLES, BUS, BICYCLE, TRUCK, OTHERS and extracted_cars inside the output folder.
4. Save images of cars on whom you wish to perform text extraction in the cars folder.
