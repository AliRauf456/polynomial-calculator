# lines 2-5 imports math and sympy modules and all their functions
from math import *
import sympy
from sympy import *
import numpy as np
import matplotlib.pyplot as plt


#This function will recieve the Equation to plot a graph
def plot_function(fx_value):
    sfx_value = str(fx_value)

    #adding [i] after every x that comes in the equation so we draw a plot
    oldstring = sfx_value
    newstring = ""
    for letter in oldstring:
        if letter == "x":
            # print (letter)
            newstring = newstring + letter + "[i]"
        else:
            newstring = newstring + letter

    print("Drawing plot for the equation: ",newstring)

    x = np.linspace(-10, 10, num=100) #creating numeric sequences
    fx = []
    for i in range(len(x)):
        fx.append(eval(newstring))

    #plotting polynomials
    plt.plot(x, fx)
    plt.grid()
    plt.axvline()
    plt.axhline()
    plt.show()
    # plt.draw()
    # plt.pause(0.01)
    # input("Press [enter] to continue.")

#integral option 1. Indefinite 2. Definite
def Quadratic(Quad_option, Quad_a, Quad_b, Quad_c, integral_option = 0, Upper_bound = 0, Lower_bound = 0):
    # a cant = 0 so if user inputs 0 for a value, it makes a = 1
    if Quad_a == 0:
        Quad_a = 1

    # Quadratic Solve Option
    # if input for quadratic option is = 1 then it solves 
    if Quad_option == 1:
        # makes x an actual symbol
        x = Symbol("x")
        # makes a quadratic equation with guven a, b, and c values
        expr = Quad_a * x ** 2 + Quad_b * x + Quad_c
        #plot_function(expr)
        # solves the equation and outpits it
        return solve(expr)

    # Quadratic Differentiation Option
    # if Quadratic option = 2 then it differentiates 
    if Quad_option == 2:
        # makes x an actual symbol
        x = Symbol('x')
        # makes quadratic equation with given a, b, and c values
        function = Quad_a * x ** 2 + Quad_b * x + Quad_c
        #plot_function(function)
        # differentiates the equation
        deriv = function.diff(x)
        # outputs the differentiation answer
        return deriv.doit()

    # Quadratic Integral Option
    # if Quadratic option = 3 then it does the integral 
    if Quad_option == 3:
        # shows options of indefinite or definite integral then asks for input based on those options
        
        # Quadratic Indefinite Integrals
        # if user chooses indefinite integral
        if integral_option == 1:
            # makes x an actual symbol
            x = Symbol('x')
            # makes quadratic equation based on a, b, and c values
            Function_integral = Quad_a * x ** 2 + Quad_b * x + Quad_c
            #plot_function(Function_integral)
            # integrates the equation
            Indef_integral = sympy.integrate(Function_integral, x)
            # outputs the solution
            return Indef_integral

        # Quadratic Definite Integrals
        # if user chooses definite integral
        elif integral_option == 2:
            # makes x an actual symbol
            x = Symbol('x')
            # makes a quadratic equation based on a, b, and c values
            gfg = Quad_a * x ** 2 + Quad_b * x + Quad_c
            #plot_function(gfg)
            # integrates using upper and lower-biund numbers and quafratic equation
            Function_integral = sympy.integrate(gfg, (x, Lower_bound, Upper_bound))
            # outouts the answer
            return Function_integral

    if Quad_option == 4:
        # makes x an actual symbol
        x = Symbol("x")
        # makes a quadratic equation with guven a, b, and c values
        expr = Quad_a * x ** 2 + Quad_b * x + Quad_c
        plot_function(expr)
        
# makes function named Cubic
def Cubic(Cubic_option, Cubic_a, Cubic_b, Cubic_c, Cubic_d, integral_option = 0, Upper_bound = 0, Lower_bound = 0):
    # a can't = 0 so makes a = 1
    if Cubic_a == 0:
        Cubic_a == 1

    # Cubic Solve
    # If user chooses option 1 then it solves cubic equation using give a, b, c, and d-values
    if Cubic_option == 1:
        # makes x an avtual symbol
        x = Symbol('x')
        # makes a cubic equation using give values
        expr = Cubic_a * x ** 3 + Cubic_b * x ** 2 + Cubic_c * x + Cubic_d
        #plot_function(expr)
        # solves then outputs the solution(s) to the cubuc equation
        return solve(expr)

    # Cubic Differentiation
    # if user chooses option 2 then it dfferentiates using give a, b, c, and d-values
    if Cubic_option == 2:
        # makes x an actual symbol
        x = Symbol("x")
        # makes a cubic equation using give a, b, c, and d-values
        expr = Cubic_a * x ** 3 + Cubic_b * x ** 2 + Cubic_c * x + Cubic_d
        #plot_function(expr)
        # differentiates cubic equation
        deriv = expr.diff(x)
        # outputs differentiation
        return deriv.doit()

    # Cubic Integrals
    # if user cooses option 3 then it integrates using given a, b, c, and d-values
    if Cubic_option == 3:
        # Cubic Indefinite Integrals
        # if user chooses indefinite intgral then executes fillowing code
        if integral_option == 1:
            # makes x an actual symbol
            x = Symbol('x')
            # makes a cubicbequation using given a, b, c, and d-values
            Function_integral = Cubic_a * x ** 3 + Cubic_b * x ** 2 + Cubic_c * x + Cubic_d
            #plot_function(Function_integral)
            # integrates equation
            Indef_integral = sympy.integrate(Function_integral, x)
            # outputs integral answer
            return Indef_integral

        # Cubic Definite Integrals
        # if user chooses definite integral executes following code
        elif integral_option == 2:
            # makes x an actual symbol
            x = Symbol('x')
            # makes a cubic equatuon using give a, b, c, and d-values
            gfg = Cubic_a * x ** 3 + Cubic_b * x ** 2 + Cubic_c * x + Cubic_b
            #plot_function(gfg)
            # integrates cubic equation using upper and lower-bound numberz
            Function_integral = sympy.integrate(gfg, (x, Lower_bound, Upper_bound))
            # outputs integral answer
            return Function_integral

    if Cubic_option == 4:
        # makes x an avtual symbol
        x = Symbol('x')
        # makes a cubic equation using give values
        expr = Cubic_a * x ** 3 + Cubic_b * x ** 2 + Cubic_c * x + Cubic_d
        plot_function(expr)

# makes a function named Quartic
def Quartic(Quartic_option, Quartic_a, Quartic_b, Quartic_c, Quartic_d, Quartic_e, integral_option = 0, Upper_bound = 0, Lower_bound = 0):
    # a cant = 0 so if a = 0, makes a = 1
    if Quartic_a == 0:
        Quartic_a == 1

    # Quartic Solve
    # if user chooses option 1 then solves quartic equation using given values
    if Quartic_option == 1:
        # makes x an actual symbol
        x = Symbol('x')
        # makes a quartic equation using give values
        expr = Quartic_a * x ** 4 + Quartic_b * x ** 3 + Quartic_c * x ** 2 + Quartic_d * x + Quartic_e
        #plot_function(expr)
        # solves and outputs quartic equayion solution
        return solve(expr)

    # Quartic Differentiation
    # if user chooses option 2 then differentiates quartic equation
    if Quartic_option == 2:
        # maes x an actual symbol
        x = Symbol("x")
        # makes quartic equation using given values
        expr = Quartic_a * x ** 4 + Quartic_b * x ** 3 + Quartic_c * x ** 2 + Quartic_d * x + Quartic_e
        #plot_function(expr)
        # differentiates quartic equation
        deriv = expr.diff(x)
        # outputs differentiation answer
        return deriv.doit()

    # Quartic Integral
    # if user chooses option 3 then integrates quartic equation
    if Quartic_option == 3:
        # if user chooses option 1, does indefinite integration
        if integral_option == 1:
            # makes x an actual symbol
            x = Symbol('x')
            # makes quartic equation using given values
            Function_integral = Quartic_a * x ** 4 + Quartic_b * x ** 3 + Quartic_c * x ** 2 + Quartic_d * x + Quartic_e
            #plot_function(Function_integral)
            # does indefinite integration of quartic equation
            Indef_integral = sympy.integrate(Function_integral, x)
            # outputs integration answer
            return Indef_integral

        # Quartic Definite Integrals
        # if user chooses option 2, does definite integration
        elif integral_option == 2:
            # makes x an actual symbol
            x = Symbol('x')
            # makes quartic equation using given values
            gfg = Quartic_a * x ** 4 + Quartic_b * x ** 3 + Quartic_c * x ** 2 + Quartic_d * x + Quartic_e
            #plot_function(gfg)
            # solves definite integration using quartic equation and given upper and lower-bound values
            Function_integral = sympy.integrate(gfg, (x, Lower_bound, Upper_bound))
            # outputs definite integral answer
            return Function_integral
            # calls Quartic function (and ends it)

    if Quartic_option == 4:
        # makes x an actual symbol
        x = Symbol('x')
        # makes a quartic equation using give values
        expr = Quartic_a * x ** 4 + Quartic_b * x ** 3 + Quartic_c * x ** 2 + Quartic_d * x + Quartic_e
        plot_function(expr)
        