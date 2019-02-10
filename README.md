# Naive-Bayes-classifier-
Classification of the data into class based on posterior probability 

# Description
* The naive assumption is that input values are independent given the class. This is a very bold assumption, but it allows us to compute the probability distribution much more easily.
* the Bayes Classifier will predict the class for which the posterior probability (or a function proportional to the posterior probability) is the greatest.


## Data set format

* CSV (Comma Separated Values) format.
* Attributes can be integer or real values.
* List attributes first, and add response as the last parameter in each row.
    * E.g. 170 , 55 , 35, "M" where the first 3 numbers are values of attributes height, weight, age and "M" is one of the response classes.

* Responses can be integer, real or categorical.
* Training data set is directly in the program code, To check the program with different training data please edit it directly in the code mainting the format.
* Data set used in this code is :- 
   * D = [(170, 57, 32, 'W'), (192, 95, 28, 'M'), (150, 45, 30, 'W'), (170, 65, 29, 'M'), (175, 78, 35, 'M'), (185, 90, 32, 'M'), (170, 65, 28, 'W'), (155, 48, 31, 'W'), (160, 55, 30, 'W'), (182, 80, 30, 'M'), (175, 69, 28, 'W'), (180, 80, 27, 'M'), (160, 50, 31, 'W'), (175, 72, 30, 'M')]
    
* Format of the data set (height, weight, Age, "class')

## How to Run the code 

1. run the file by using command "python naiveBayes.py"
2. Input the whether the prediction to be made by with or without Age by inputing appropiate values.
    User also has the option to exit the program by inputing -1 
3. Enter the data point to be predicted(eg "170 70 32"), 
    User also has the option to go back and select with or without Age by inputing -1
4. The Intermediate Parameters will be calculated and displayed on the screen 
    Also, the class prediction will be made based on the posterior probabilities and displayed on the screen
5. The user will be prompted if he wants to do prediction for different data point or exit the program.
