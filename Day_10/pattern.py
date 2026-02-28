'''
0 1 2 3 4 
0 1 2 3 4 
0 1 2 3 4 
0 1 2 3 4 
0 1 2 3 4

n=int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        print(col,end=' ')
    print()
-----------------------------------------------------
0 0 0 
1 1 1 
2 2 2     

n=int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        print(row,end=' ')
    print()
---------------------------------------------------
Enter the size: 6
1 2 3 4 5 6 
7 8 9 10 11 12 
13 14 15 16 17 18 
19 20 21 22 23 24 
25 26 27 28 29 30 
31 32 33 34 35 36 

n=int(input("Enter the size: "))
num=1
for row in range(n):
    for col in range(n):
        print(num,end=' ')
        num+=1
    print()
-----------------------------------------------------------
Enter the size: 6
0 1 2 3 4 5 
1 2 3 4 5 6 
2 3 4 5 6 7 
3 4 5 6 7 8 
4 5 6 7 8 9 
5 6 7 8 9 10

n=int(input("Enter the size: "))
num=1
for row in range(n):
    for col in range(n):
        print(row+col,end=' ')
        num+=1
    print()
------------------------------------------------------------------
Enter the size: 9
0 X 0 X 0 X 0 X 0 
X 0 X 0 X 0 X 0 X 
0 X 0 X 0 X 0 X 0 
X 0 X 0 X 0 X 0 X 
0 X 0 X 0 X 0 X 0 
X 0 X 0 X 0 X 0 X 
0 X 0 X 0 X 0 X 0 
X 0 X 0 X 0 X 0 X 
0 X 0 X 0 X 0 X 0

n=int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        if (row+col)%2==0:
            print(0,end=' ')
        else:
            print('X',end=' ')
    print()
--------------------------------------------

Enter the size: 9
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * * * 
* * * * * * * * 
* * * * * * * * *
n=int(input("Enter the size: "))
for row in range(n):
    for col in range(row+1):
            print('*',end=' ')
    print()
-----------------------------------------------------------------
Enter the size: 9
* * * * * * * * * 
* * * * * * * * 
* * * * * * * 
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
*

n=int(input("Enter the size: "))
for row in range(n):
    for col in range(n-row):
            print('*',end=' ')
    print()
----------------------------------------------
Enter the size: 9
                * 
              * * 
            * * * 
          * * * * 
        * * * * * 
      * * * * * * 
    * * * * * * * 
  * * * * * * * * 
* * * * * * * * * 
n=int(input("Enter the size: "))
for row in range(n):
    for spc in range(n-row-1):
        print(' ',end=' ')
    for col in range(row+1):
            print('*',end=' ')
    print()
--------------------------------------------------
Enter the size: 9
        * 
       * * 
      * * * 
     * * * * 
    * * * * * 
   * * * * * * 
  * * * * * * * 
 * * * * * * * * 
* * * * * * * * * 
n=int(input("Enter the size: "))
for row in range(n):
    for spc in range(n-row-1):
        print(' ',end='')  {just space at end }
    for col in range(row+1):
            print('*',end=' ')
    print()
-----------------------------
Enter the size: 9
  * * * * * * * * * 
    * * * * * * * * 
      * * * * * * * 
        * * * * * * 
          * * * * * 
            * * * * 
              * * * 
                * * 
                  *
n=int(input("Enter the size: "))
for row in range(n):
    for spc in range(row+1):
        print(' ',end=' ')
    for col in range(n-row):
            print('*',end=' ')
    print()
------------------------------------------------------
Enter the size: 10
* * * * * * * * * * 
*                 * 
*                 * 
*                 * 
*                 * 
*                 * 
*                 * 
*                 * 
*                 * 
* * * * * * * * * *
n=int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row==n-1 or col==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
-------------------------------------------
Enter the size: 13
* * * * * * * * * * * * * 
*           *           * 
*           *           * 
*           *           * 
*           *           * 
*           *           * 
* * * * * * * * * * * * * 
*           *           * 
*           *           * 
*           *           * 
*           *           * 
*           *           * 
* * * * * * * * * * * * * 
n=int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row==n-1 or col==n-1 or row==n//2 or col==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
--------------------------------------------------------------
Enter the size: 12
* * * * * * * * * * * * 
                    *   
                  *     
                *       
              *         
            *           
          *             
        *               
      *                 
    *                   
  *                     
* * * * * * * * * * * *
n=int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or row+col==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
-------------------------------------------------------------------
Enter the size: 12
*                     * 
  *                 *   
    *             *     
      *         *       
        *     *         
          * *           
          * *           
        *     *         
      *         *       
    *             *     
  *                 *   
*                     * 

n=int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        if row==col or row+col==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
-----------------------------------------------------
'''

































    













