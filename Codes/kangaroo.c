//You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).
//The first kangaroo starts at location x1  and moves at a rate of v1 meters per jump.
//The second kangaroo starts at location x2 and moves  at a rate of v2 meters per jump.
//You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. If it is possible, return YES, otherwise return NO.

#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

void kangaroo(int x1, int v1, int x2, int v2) {
   // // Complete this function
   // char c[20];
    //
    if(x1==x2)
     printf("YES"); 
  else  if(x2>x1 && v2>=v1)
     printf("NO");
  else if (x2>x1&&v1>v2)
   { while(x2>x1)
     {x1=x1+v1;
      x2=x2+v2;
      if(x1==x2)
       {printf("YES");
      
        break;
       }//if
     }//while
       if(x2!=x1)
       {printf("NO");}
           
     } //if

   else  if(x1>x2&&v2>v1)
    printf("NO");
    
   else  if(x1>x2&&v2>v1)
     {  while(x1>x2)
         {x1=x1+v1;
          x2=x2+v2;
          if(x1==x2)
          {
             printf("YES");
              break;
          } 
         }
          if(x1!=x2)
          { printf("NO");}
         
         
         }
     }   
   
   
nt main() {
    int x1; 
    int v1; 
    int x2; 
    int v2; 
    scanf("%i %i %i %i", &x1, &v1, &x2, &v2);
    int result_size;
    kangaroo(x1, v1, x2, v2);
    //printf("%s\n", result);
    
    
    
    
    
    
    
    
    
    return 0;
}





