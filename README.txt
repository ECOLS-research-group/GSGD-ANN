# Enhanced-ANN-GSGD

Variation of Guided Stochastic Gradient Descent (GSGD)

Copyright (c) 2023, ECOLS - All rights reserved.

[version 1.0]
The orignial GSGD works for logistic regression only. The code was written in Matlab by the supervisor Anuraganand Sharma in the paper:
A. Sharma, “Guided Stochastic Gradient Descent Algorithm for inconsistent datasets,” 
Applied Soft Computing, vol. 73, pp. 1068–1080, Dec. 2018 

[version 2.0]
The student Zain Ali converted the original Matlab code to Python then another student Avishek Anishkar Ram enhanced the code for GSGD to work for ANN.

Paper: A Guided Neural Network Approach to Predict Early Readmission of Diabetic Patients
Programmer: Avishek Anishkar Ram, Zain Ali 
Supervisor: Dr. Anuraganand Sharma

The ANN-GSGD code has been written and tested with Python 3.10.6

Steps to setup and run  ANN-GSGD 
1.	Install Conda Package Manager
2.	Create a new conda environment using the file “environment.yml” available in the directory, the following command can be used for this “conda env create -f environment.yml” 
3.	The main program is written in main.py. Run this program.
4.	A popup opens where you have to select the data file, which is available in the repository directory inside the “data” folder.
5.	Now, the program will start running, It will train both the guided and canonical models and present the results on the performance of both the models based on the validation dataset.

The following repositories were referenced to aid the development of the ANN-GSGD algorithm:
https://github.com/anuraganands/GSGD
https://github.com/anuraganands/GSGD-CNN
