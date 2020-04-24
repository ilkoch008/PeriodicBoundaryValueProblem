# Periodic Boundary Value Problem
In this repo considered the solution of following equation

![](https://github.com/ilkoch008/PeriodicBoundaryValueProblem/blob/master/images/Screenshot_1.png?raw=true)

Let's rewrite the boundary value problem in the difference form

![](https://github.com/ilkoch008/PeriodicBoundaryValueProblem/blob/master/images/Screenshot_2.png?raw=true)

The task will be solved with the following parameters:

![](https://github.com/ilkoch008/PeriodicBoundaryValueProblem/blob/master/images/Screenshot_3.png?raw=true)

Rewrite equations:

![](https://github.com/ilkoch008/PeriodicBoundaryValueProblem/blob/master/images/Screenshot_4.png?raw=true)

Introduce the notation:

![](https://github.com/ilkoch008/PeriodicBoundaryValueProblem/blob/master/images/Screenshot_5.png?raw=true)

Then the equations will be rewritten in the form:

![](https://github.com/ilkoch008/PeriodicBoundaryValueProblem/blob/master/images/Screenshot_6.png?raw=true)

Or in matrix form

![](https://github.com/ilkoch008/PeriodicBoundaryValueProblem/blob/master/images/Screenshot_7.png?raw=true)

## Solution of tridiagnal periodic system

This system might be solved by Gaussian elimination, but this algorithm will take a lot of time.
Solution of this system can be reduced to solution of two non-periodic tridiagonal systems.
Let's introduce the notation for the coefficients of the matrix indicated above:
![](https://github.com/ilkoch008/PeriodicBoundaryValueProblem/blob/master/images/Screenshot_9.png?raw=true)

Then two non-periodic tridiagonal systems will be written as:

![](https://github.com/ilkoch008/PeriodicBoundaryValueProblem/blob/master/images/Screenshot_8.png?raw=true)

![](https://github.com/ilkoch008/PeriodicBoundaryValueProblem/blob/master/images/Screenshot_10.png?raw=true)

Expression for the last point:

![](https://github.com/ilkoch008/PeriodicBoundaryValueProblem/blob/master/images/Screenshot_11.png?raw=true)

Then the solution for the original system will be written as:

![](https://github.com/ilkoch008/PeriodicBoundaryValueProblem/blob/master/images/Screenshot_12.png?raw=true)

## Results

![](https://github.com/ilkoch008/PeriodicBoundaryValueProblem/blob/master/images/Screenshot_13.png?raw=true)

![](https://github.com/ilkoch008/PeriodicBoundaryValueProblem/blob/master/images/Screenshot_14.png?raw=true)

![](https://github.com/ilkoch008/PeriodicBoundaryValueProblem/blob/master/images/Screenshot_17.png?raw=true)

![](https://github.com/ilkoch008/PeriodicBoundaryValueProblem/blob/master/images/Screenshot_15.png?raw=true)

![](https://github.com/ilkoch008/PeriodicBoundaryValueProblem/blob/master/images/Screenshot_16.png?raw=true)

![](https://github.com/ilkoch008/PeriodicBoundaryValueProblem/blob/master/images/Screenshot_18.png?raw=true)
