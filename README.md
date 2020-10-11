# Car-evaluation
This model helps in evaluating the class of the given car on the basis of their buying cost, maintainace cost, number of doors, number of persons seated, lug_boot space and the safety features. 
when the above independent features are provided the machine learning model will use the KneigborClassifier model to predict the class of the given car.
the class in this senario are (unacc, acc, good, vgood). the more the features of the car the more better class it will be given.

# data downloading
Here first i have started with downloading the data from https://archive.ics.uci.edu/ml/datasets/Car+Evaluation it has the traing data for various independent and dependent features of various cars.

# coding_description
then open the data in python with panda library. as the data contain mant cateroral features it has to be preprossesd into interal form.
then i have made the test and trail data using the test split library. After that i have made the KneighborClassifier model and fit the trail data in the model.

# Pickel formation
hence we will be in the need of the created model in future so i have saved the model in a pickel format to be used in future.
this was done by dumping the model into a pickel file.

# flashing the result
once the pickel is been created i have made a code for flashing the result which shows the actual and predicted data. here i have got an accuracy of about 93%

TO SEE THE CODE PLEASE OPEN THE CODE FILE IN THE REPOSITORY.
