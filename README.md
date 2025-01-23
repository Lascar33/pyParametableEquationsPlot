
# Lascar's parametable equation plot

Plot 10 equations using Python formula. The Python Math Library and all its functions are available. For more information, refer to the [Python Math Library documentation](https://docs.python.org/3/library/math.html). 


## Run Locally  

Clone the project  

~~~bash  
  git clone https://github.com/Lascar33/pyParametablePlotFunction.git
~~~

Go to the project directory  

~~~bash  
  cd pyParametablePlotFunction
~~~

Install dependencies  

~~~bash  
  pip install --upgrade pip
  pip install matplotlib Tkinter
~~~

Run

~~~bash  
  py LpyPP.py
~~~

## How to use

Enter your function equations in the 10 function field. You can add variable parameters using $ sign (eg: $a). Parameters can use only one char, $xx will be interpreted as $x.
Use the Enter key to update fields. All variables need to be referred in "parameters" field. No error log. Refer to the console to handle errors.  
There is an autosave feature which save all field between runs.  
Function can use other above function results eg:
~~~
y0=$a*x+$b
y1=$y0*12.34
~~~

It's ugly but it works fine ! It's a tool perfect to find equations solutions or application dev which need calculus.

![Screenshot](./screen.png)

## Contributing  

Contributions are always welcome!   

## License  

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)  
