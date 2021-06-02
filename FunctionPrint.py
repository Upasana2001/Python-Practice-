The included code stub will read an integer, , from STDIN.
Without using any string methods, try to print the following:1234...
Note that "" represents the consecutive values in between.
Example
n=5
Print the string 12345 .
Input Format:The first line contains an integer .
  
  
First Method(WHILE LOOP)                #input = 5, output = 12345
if __name__ == '__main__':
    n = int(input())
    i=1
    while i<=n:
        print(i,end='')
        i=i+1
        
        
 Second Method(FOR LOOP)
if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i,end='')
        
        
