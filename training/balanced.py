open_list = ["[","{","("] 
close_list = ["]","}",")"] 
  
def check(myStr): 
    """ It check if a string is balanced considering the below characters:

    {},[],()

    """
    stack = [] 
    if myStr == "":
        return False
    for i in myStr: 
        if i in open_list: 
            stack.append(i) 
        elif i in close_list: 
            pos = close_list.index(i) 
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])): 
                stack.pop() 
            else: 
                return False
    if len(stack) == 0: 
        return True
  
# Running the function to check de string
string = "{[]{()}}"

print(string,"is: ", check(string)) 

