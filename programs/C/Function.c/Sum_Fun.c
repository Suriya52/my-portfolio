
// Syntax of Function

#include<stdio.h>

int add(){            // Function Name add()
    int a=5;
    int b=6;
    int c=a+b;
    return c;
    
}

void main(){
    //int ans=add();            calling Function like this or in below type.
    //printf("%d ",ans);
    
    printf("%d",add());         // same 11 will print in the output.

}