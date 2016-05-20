# Missing Values Prediction - Machine Learning Final Project

Extract the zip file that contains the Python scripts to a folder. Copy the *final-nmv-noclass.txt* and *train.mv.txt* files to that folder. 

I specifically used Linux for this project, so the below instructions are for Linux system. 

I used **scikit-learn** library, so the system needs to have **python**, **numpy** and **scipy** with latest versions installed. 

Open the terminal, change current directory to the folder, and run:
```bash 
python impute.py && python getClass.mv.py && python genClassifier-dt-boost.mv.py
```

The newly created prediction file is named *prediction.txt*


