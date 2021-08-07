# **Fire-Extinguisher-Bot**
*Open Projects 2021*
![Bot Design](Images_videos/Images/Bot_view_1.jpg "*Bot Design*")
![Bot Design 2](Images_videos/Images/Bot_view_4.PNG)
## Abstract
Automatic Fire Extinguisher Robot is a Hardware-based model used to put out the fire during fire accidents automatically. The Bot has features to move in the direction of fire and extinguish it automatically.
The Bot finds its applications in rescue operations during fire accidents where concerned authorities can take time to enter the fire-prone areas.
## Mechanical Aspect
The Mechanical Design is explicitly made for significant weight carrying capacity. It is sturdy and reliable and can easily transverse through domestic terrain.
The navigation of this can be both manual and automated. In the automatic mode, it is regulated via a PID Wall Following System.

![Bot Design](Images_videos/Images/Bot_view_3.PNG)
![Bot Design](Images_videos/Images/Bot_view_2.PNG)
![Bot Design](https://github.com/Ch0ubey/Fire-Extinguisher-Bot/blob/675ec79065b406595411fb3a4fc21760a32cbd39/Images_videos/Images/Nozzle%20Mechanism.PNG)
## Electrical Aspect
The image processing Software used is OpenCV. The data about the image is fed to OpenCV, where the image is converted to HSV and GreyScale format. Approximate Centre Coordinates of the fire are calculated. This Data is then stored in a text file for the simulation software or Audrino to use.

![Bot Design](https://github.com/Ch0ubey/Fire-Extinguisher-Bot/blob/675ec79065b406595411fb3a4fc21760a32cbd39/Images_videos/Images/Fire%20Detection%20with%20Coordinates.png)
![Bot Design](Images_videos/Images/Image_processing_openCV.jpg)
## Cost Structure
| Components   |Amount  |      Quantity      |  Cost |
|----------    |:------:|:-------------:     |------:|
| Ultrasonic sensors     |  75    |  7     | Rs 525 |
| Temperature sensors    |  75    |1            | Rs 75 |
| Flame sensors     |   59     |1      | Rs 59 |
| Camera| 300 | 1| Rs 300|
|Arduino UNO|500|1|Rs 500|
|Encoder|1500|1|Rs 1500|
|Dc motors|1500|1|Rs 1500|
|Lead screw|100|1|Rs 100|

## Motivation
The motivation behind this project essentially originated from our desire to learn new things. We can use this autonomous bot in case of laboratories or domestic fires, which can save lives or act as a quick remedy before the concerned authorities arrive. Although this technology is relatively unused in India, it can significantly impact the lives we lose to Fire incidents and our complete dependency on Emergency services.
## Limitations
- Takes time to detect fire
- Needs manual assistance while changing the fire extinguishers
- Usable for household fires only
## Future Improvement
* Install cameras in every room
* Link with smoke sensors in the area
* Use custom made cylinders to avoid manual assistance
## Team members
1. Akanksha vijayvergiya
2. Eeshan punde
3. Ganesh kalanidhi
4. Mritunjay kumar choubey
5. Poreddy sahith reddy
6. Srushti parbat
## Mentors
1. Naman agarwalla
2. Parul chaudhary
3. Shubham goyal
## Refrences link
- [Coppeliasim Tutorial](https://www.youtube.com/watch?v=PwGY8PxQOXY&list=PLjzuoBhdtaXOoqkJUqhYQletLLnJP8vjZ)
- [Solidworks Tutorial](https://youtube.com/playlist?list=PLkMYhICFMsGajeARsY7N1t1jhbtMb1poL)
- [2 axis gimbal](https://www.youtube.com/watch?v=i6UoxhNlr1U)
- [Image processing openCV](https://www.youtube.com/watch?v=Z78zbnLlPUA&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq)
- [Coppeliasim Documentation](https://www.coppeliarobotics.com/helpFiles/index.html)
