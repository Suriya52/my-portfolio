
// Syntax for "For Loop"

/*#include<stdio.h>
void main()
{
    int i;
    for (  i = 0; i <=10; i++)
    {
        printf("It is the syntax for 'For Loop'\n");
    }
    
}*/


// Sum of first n Natural Number

/*
#include<stdio.h>
void main()
{
    int i, n, sum=0;
    printf("Enter the value of n:");
    scanf("%d",&n);

    for ( i = 1; i <= n; i++)
    {
        sum = sum + i;
    }
    printf("Sum: %d",sum);
    
}*/

// Factorial of Given Number


#include<stdio.h>
void main()
{
    int i, n, fact=1;
    printf("Enter the value to factoral:");
    scanf("%d",&n);

    for ( i = 1; i <= n; i++)
    {
        fact= fact * i;
    }
    printf("Fatorial of %d: %d",n,fact);
    
}