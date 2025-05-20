
// Call  By Value

// call By Reference

#include<stdio.h>

void swap(int *x, int *y)        // Swap function it simply swap a given number
{
    int temp = *x;      /* We use pointer (Call By Reference)here because without pointers this not working(Call By Value)*/
      *x=*y;
      *y=temp;
}

int main(){

    int a=5;
    int b=6;

    printf("%d %d\n",a,b);

    swap(&a,&b);

    printf("%d %d\n",a,b);
}