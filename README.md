<p align="justify">
<h1><b>Fire-Extinguisher-Bot</b></h1>
  <h2>Open Projects 2021</h2>
</p>

![Bot Design](https://github.com/Ch0ubey/Fire-Extinguisher-Bot/blob/99d7aaeea15895aa91a57da3c2a6b9b1c1923cc6/Images%20and%20Videos/Images/Bot_view_1.jpg)
<div align="center"><em>Bot View 1</em></div>
<br/>

![Bot Design 2](https://github.com/Ch0ubey/Fire-Extinguisher-Bot/blob/99d7aaeea15895aa91a57da3c2a6b9b1c1923cc6/Images%20and%20Videos/Images/Bot_view_4.PNG)
<div align="center"><em>Bot View 2</em></div>
<br/>
 
<p align="justify">
  <h2>Abstract</h2>
</p>
<p align="justify">
  
- Automatic Fire Extinguisher Robot is a Hardware-based model used to put out the fire during fire accidents automatically. The Bot has features to move in the direction of fire  and extinguish it automatically.
- The Bot finds its applications in rescue operations during fire accidents where concerned authorities can take time to enter the fire-prone areas.
- Development of this autonomus bot using Controllers and image processing can help us to control fire without human inputs.Thus, minimising delays and unavailiblity of services.

</p>
 
<p align="justify">
  <h2>Motivation</h2>
</p>
<p align="justify">
  
The motivation behind this project essentially originated from our desire to learn new things. We can use this autonomous bot in case of laboratories or domestic fires, which can save lives or act as a quick remedy before the concerned authorities arrive. Although this technology is relatively unused in India, it can significantly impact the lives we lose to Fire incidents and our complete dependency on Emergency services.

</p>

<p align="justify">
  <h2>Mechanical Aspect of Design</h2>
</p>
<p align="justify">

The Mechanical Design is explicitly made for significant weight carrying capacity using mild steel as a material having composition of 0.20-0.30% Carbon and Manganese. It is sturdy and reliable and can easily transverse through domestic terrain.
The navigation of this can be both manual and automated. In the automatic mode, it is regulated via a PID Wall Following System.
> ## Wheel Assembly
> 
>The bot uses the Timing Belt Mechanism for the wheel Assembly. It provides an advantage of effortless mobility and significant weight carrying capacity over all the other mechanisms.

<p align="center">
  <img src="https://github.com/Ch0ubey/Fire-Extinguisher-Bot/blob/734ad0370c93da568aa504aa3b49e69dac5bd6af/Images%20and%20Videos/Images/Bot_view_2.PNG">
  <br/><i>Timing Belt and Rollers</i>
</p>

> ## Nozzle Mechanism
> 
>The nozzle is a 2-axis gimbal. This Mechanism can rotate 30 degrees in both horizontal directions and 30 degrees in both vertical directions.

<p align="center">
  <img src="https://github.com/Ch0ubey/Fire-Extinguisher-Bot/blob/e53ffc0dbc5896a10a27d20bba5699513d492f58/Images%20and%20Videos/Images/Nozzle%20Mechanism.PNG">
  <br/><i>Nozzle mechanism</i>
</p>

> ## Handle Pushing Mechanism
> 
>Leadscrew Mechanism can provide a torque of a considerable magnitude and resist the back force applied by the handle. Due to these factors, we use a leadscrew mechanism for handle pushing in our bot.

</p>
<p align="center">
  <img src="https://github.com/Ch0ubey/Fire-Extinguisher-Bot/blob/734ad0370c93da568aa504aa3b49e69dac5bd6af/Images%20and%20Videos/Images/Leadscrew%20mechanism.jpeg"><br/>
  <i>Leadscrew mechanism</i>
</p>
<p align="justify">
 
> ## Stair Climbing
> 
>The stair climbing mechanism works based on two-timing belts, positioned at an angle of 23 Degrees from the ground. We decided on this angle after a brief round of simulation on coppeliasim.

</p>
<p align="center">
  <img src="https://github.com/Ch0ubey/Fire-Extinguisher-Bot/blob/99d7aaeea15895aa91a57da3c2a6b9b1c1923cc6/Images%20and%20Videos/Images/Bot_view_3.PNG">
  <br/><i>Wheel assembly</i>
</p>
<p align="justify">
  <h2>Electrical Aspect of Design</h2>
</p>
<p align="justify">
  
- We used microcontrollers for BOT movement and nozzle movement.

<p align="center">
  <img src="https://github.com/Ch0ubey/Fire-Extinguisher-Bot/blob/9e1d842a9c91a54889573999508a2310fe07a7fe/Images%20and%20Videos/Images/BOT%20algorithm.jpg"><br/>
  <i>BOT algorithm</i>
</p>

- We also used Ultrasonic distance sensors, Temperature sensors and Flame sensors.
<br/>

![Bot Design](https://github.com/Ch0ubey/Fire-Extinguisher-Bot/blob/675ec79065b406595411fb3a4fc21760a32cbd39/Images_videos/Images/Fire%20Detection%20with%20Coordinates.png)
<div align="center"><em>simulation</em></div>
<br/>

- For image processing we used camera (*as a Hardware part*). The image processing Software used is OpenCV. The data about the image is fed to OpenCV, where the image is converted to HSV and GreyScale format. Approximate Centre Coordinates of the fire are calculated. This Data is then stored in a text file for the simulation software or Audrino to use.
<br/>

![Bot Design](https://github.com/Ch0ubey/Fire-Extinguisher-Bot/blob/734ad0370c93da568aa504aa3b49e69dac5bd6af/Images%20and%20Videos/Images/Image_processing_openCV.jpg)
<div align="center"><em>Image processing</em></div>
<br/>
</p>

<p align="justify">
  <h2>Simulation</h2>
</p>
<p align="justify">
  
For simulation purpose we used the following softwares :-
- Solidworks
    > For mechanical designing of our BOT.
- Tinkercad
    > For simulating Temperature sensor working.
- Coppeliasim
    > For simulating Stair climbing, Wall detection, Wheel PID and Fire detection.
- Python and openCV
    > For Image processing to detect fire and marking that center of fire (high intensity zone) with circle. 

For elaborative explanation, you can refer [here](https://github.com/Ch0ubey/Fire-Extinguisher-Bot/blob/49c68fb09d31af3eed7d412b4f8d0a11268a28de/Simulation/README.md).

</p>
<p align="justify">
  <h2>Applications</h2>
</p>
<p align="justify">
  
- The main objective of the fire extinguishing bot is to search for the fire and put it off. Sensors are used to evaluate the environment in which the bot is operating and allows the bot to adjust actions based on collected data. The buzzer used will be helpful in alarming people about the danger.
- As it is an autonomus bot which uses Controllers and image processing, so it can help us to control fire without human inputs.
- Using this bot we can minimise delays and unavailiblity of services during emergency.
- It can be highly useful in extinguishing fire where probability of explosion is high. For eg. Hotel kitchens, LPG/CNG gas stores, etc.

</p>
<p align="justify">
  <h2>Cost Structure</h2>
</p>

| Components   |Amount(INR)  |      Quantity      |  Cost(INR) |
|----------    |:------:|:-------------:     |------:|
| Ultrasonic sensors     |  75    |  7     |  525 |
| Temperature sensors    |  75    |1            |  75 |
| Flame sensors     |   59     |1      |  59 |
| Camera| 300 | 1|  300|
|Arduino UNO|500|1| 500|
|Encoder|1500|1| 1500|
|Dc motors|1500|1| 1500|
|Lead screw|100|1| 100|
|Timing belt (G/GB type) | 400| 1 |400|
|Wheels(lower) |480| 6|2880|
|Wheels(upper)|320 | 2|640|
|3D Printing Filament| 1200|1|1200|
|Fire extinguisher (ABC powder 4kg)|1000|2|2000|
|Mild steel (Body material)|50|2|100|
|**Total Cost**| | |**11,699**|

<p align="justify">
  <h2>Limitations</h2>
</p>

- Takes time to detect fire
- Needs manual assistance while changing the fire extinguishers
- Usable for household fires only
<p align="justify">
  <h2>Future Improvement</h2>
</p>
<p align="justify">
 
* Install cameras in every room
* Link with smoke sensors in the area
* Use custom made cylinders to avoid manual assistance

 </p>
<p align="justify">
  <h2>Team members</h2>
</p>
<p align="justify">

1. [Akanksha Vijayvergiya](https://github.com/Akanksha-247)
2. [Eeshan Punde](https://github.com/eeshanpunde14)
3. [Ganesh Kalanidhi](https://github.com/GaneshK-RKE)
4. [Mritunjay Kumar Choubey](https://github.com/Ch0ubey)
5. [Poreddy Sahith Reddy](https://github.com/sahithreddyporeddy)
6. [Srushti Parbat](https://github.com/SrushtiParbat)

</p>  
<p align="justify">
  <h2>Mentors</h2>
</p>
<p align="justify">

1. [Naman Agarwalla](https://github.com/naman99-agar)
2. [Parul Chaudhary](https://github.com/Parul253)
3. [Shubham Goyal](https://github.com/shubham491981)

</p>
<p align="justify">
  <h2>Refrences link</h2>
</p>
<p align="justify">
  
- [Coppeliasim Tutorial](https://www.youtube.com/watch?v=PwGY8PxQOXY&list=PLjzuoBhdtaXOoqkJUqhYQletLLnJP8vjZ)
- [Solidworks Tutorial](https://youtube.com/playlist?list=PLkMYhICFMsGajeARsY7N1t1jhbtMb1poL)
- [2 axis gimbal](https://www.youtube.com/watch?v=i6UoxhNlr1U)
- [Image processing openCV](https://www.youtube.com/watch?v=Z78zbnLlPUA&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq)
- [Coppeliasim Documentation](https://www.coppeliarobotics.com/helpFiles/index.html)

  </p>
