# Getarg
A python module for easily getting command line arguments. 
# Instructions
To use the module in your own code simply:
```
import getarg
```
Then call:
```
getarg.get('parameter')
```
or 
```
getarg.getposition(POSITION_INT)
```
# Example
Create a file with the following code:
```
import getarg
fileName = getarg.get('filename')
print('The file name is ' + fileName)
```
then run the script from the command line:
```
python scripy.py filename="MyFile.txt"
```
you should get the following output:
```
The file name is MyFile.txt
```
