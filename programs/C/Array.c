#include<stdio.h>
void main()
{
    int height[50],i;      // Array

    height[0]=21;          // Index value of an array
    height[1]=43;
    height[2]=55;

    for ( i = 3; i <6; i++)
    {
        scanf("%d",&height[i]);
    }
    for ( i = 0; i <6; i++)
    {
        printf("%d\n",height[i]);
    }
    
    
}