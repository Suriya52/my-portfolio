// Exit control loop

#include<stdio.h>
void main()
{
    int i=1, n, fact=1;
    printf("Enter the value to factoral:");
    scanf("%d",&n);

    do
    {
        fact = fact * i;
        i++;
    } while (i<=n);
    
    printf("Fatorial of %d: %d",n,fact);
    
}