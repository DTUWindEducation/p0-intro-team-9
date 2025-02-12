def greet(name):
    #name = input("How do you want to be called? ")
    print(f"Hello {name}!")

def goldilocks(size):
    if size <= 150 and size >= 140:
        print("Goldilocks very happy, the bed size is just right.")
    elif size >150:
        print("Goldilocks unhappy, the bed is too large.")
    else:
        print("Goldilocks unhappy, the bed is too small.")

def fibonacci_stop(max_value):
    fibonacci_value = 1
    fibonacci_list = [fibonacci_value]
    while fibonacci_value < max_value:
        fibonacci_list.append(fibonacci_value)
        fibonacci_value = fibonacci_list[-2] + fibonacci_list[-1]
    print(f"The Fibonacci lower than {max_value} is: {fibonacci_list}")

def clean_pitch(measurement,status):
    measurement_cleaned = measurement
    if len(measurement) != len(status):
        print("The two arrays are not the same length.")
    else: 
        for i in range(len(measurement)):
            if status[i] == 0:
                measurement_cleaned[i] = measurement[i]
            else:
                measurement_cleaned[i] = -999 
    print(f"The cleaned pitch is: {measurement_cleaned}")
    return measurement_cleaned
    
greet("Dude")
goldilocks(150)
fibonacci_stop(30)
x, status = [-1, 2, 6, 95, 30], [1, 0, 0, 0, 1]
clean_pitch(x, status)

