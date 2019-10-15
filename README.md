# automated-attendance-system-using-face-recognition
Using the faces of the employees or student to mark their attendance on a particular day at a partiular time.

Here the faces of the students are detected and then when the students come in front of the camera, the faces are recognised and the attendance is added to a notepad file. From the previous review the additional functionalities that have been added to the project include the addition of timestamp during addition of ac face in the notepad file thus helping in determining and sorting when the particular faces were added to determine if the students were present or not and if present when did they came to the class. Also running the python files again and again can prove to be problematic for everyday use so here I am also converting the python files to the corresponding executables thus them it easy to run them.
Firstly all the files should be kept in same folder along with the har cascade face classifier.

The face authentication is done as:

1. Run the detection.py code to add the faces of the employees to the database (by default in E:/) to allow them for recognition. Here the haarcascade frontal face is being used to determine the important points of the faces. Also each of the new added face will be given a unique id.
2. Run the training.py file to train the model for the recognition of the faces. It will create a trainner.yml file containing the important features of the faces that have been added to the database. 
3. The recog.py file opens the camera to recognise the faces of the employees. If the face is recognised that is more than 85% feature match then the program will add the given id of the student into the notepad file.
4. Instead of running all the python files from the terminal we can also just directly click on the respective executable file to run the particular program. 


The python files can be converted to executables as :
> pip install pyinstaller

> pyinstaller --onefile filename.py
