# Decorator declarations

def kids(taskFunc):
    def newTask(*args, **kwargs):
        originalTask = taskFunc(*args, **kwargs)
        return f'{originalTask} by the kids'
    return newTask

def mom(taskFunc):
    def newTask(*args, **kwargs):
        originalTask = taskFunc(*args, **kwargs)
        return f'{originalTask} by Mom'
    return newTask

def dad(taskFunc):
    def newTask(*args, **kwargs):
        originalTask = taskFunc(*args, **kwargs)
        return f'{originalTask} by Dad'
    return newTask

# Task declarations

@mom
def laundry():
    return "The dirty laundry was cleaned"

@kids
def garbage():
    return "The garbage was taken out"

@mom
def dust():
    return "The house was dusted"

@dad
def groom():
    return "The dog was brushed"

print(laundry())
print(garbage())
print(dust())
print(groom())