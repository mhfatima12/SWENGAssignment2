# SWENGAssignment2  
Assignment Description  
In this assignment, you need to apply what you've learned in using Docker for containerizing web applications and performing the Continuous Delivery pipeline. You will be working in a group of 4 members (all the groups for this assignment are now listed in the group section). You are asked to develop a calculator web app. The web app will take a mathematical expression in string format from the text box and should be able to validate and evaluate the mathematical expression.  
The calculator should have the following features:  
1) It can handle both integers and floating-point numbers.  
2) It should be capable of performing addition, subtraction, multiplication, division, and power (^).  
3) It should be able to work with expressions containing brackets.  
4) It should be capable of performing the log (natural log) and exp functions.  
5) The results should be rounded off to 3 decimal places.  
6) The user interface should be designed properly.  
Examples of expressions and values are given below:  
a) "exp(4)" should return a string containing "54.598".  
b) "3+5*exp(4.2)/(5+7)" should return a string containing "30.786".  
c) "3+**8" should return an error message.  
You should develop the app in two releases. You should also create a suitable CI workflow to run the unit tests and this should be triggered when pushing or merging into the main branch. The Continuous Delivery workflow, on the other hand, should containerize the app and push the image into Docker Hub. This workflow should be triggered when creating a release tag. Make sure to use the tag to distinguish between the two versions of the app image (don't use "latest" as a tag). You also need to apply the branching concept to manage tasks and teamwork.
