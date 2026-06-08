#tryexcept
#example1
try:
    print(x)
except:
    print("variable not found")

#example2
try:                              #try block lets you test a block of code for errors
    print("hello")
except:
    print("something went wrong!")    #except block lets you handle the error
else:
    print("nothing went wrong!")       #else block lets you execute the code when there is no error

#example3
try:
    print(x)
except NameError:
    print("no variable found")
else:
    print("something went wrong!")

#example4
try:
    print(x)
except:
    print("something went wrong!")
finally:                                       #finally executes the code,regardless of results of try except block
    print("the 'try except' is finished")  

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")  


#raise an expection
x=-1
if x<0:
   raise Exception("no numbers below 0")


x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")
