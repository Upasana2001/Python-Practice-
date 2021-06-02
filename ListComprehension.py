You are given three integers x,y,z representing the dimensions of a cuboid along with an integer n.
Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to n . 
Here,0<=i<=x; 0<=j<=y: 0<=k<=z . Please use list comprehensions rather than multiple loops, as a learning exercise.
  Sample Input 0:
1
1
1
2
Sample Output 0:
   [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
    
    
    if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    final_list=[]
    for i in range(1+x):
        for j in range(y+1):
            for k in range(1+z):
                if i+j+k!=n:
                    temp=[i,j,k]
                    final_list.append(temp)
                else:
                    continue
    print(final_list)
    
    
