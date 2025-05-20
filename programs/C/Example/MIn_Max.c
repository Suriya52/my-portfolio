#include<stdio.h>
void main()
{
    int n,arr[50],min,max,i;

    printf("Enter the n value:");
    scanf("%d",&n);

    for ( i = 0; i <n; i++)
    {
        printf("Enter a Element %d:",i);
        scanf("%d",&arr[i]);
    }
       

    min=arr[0];
    max=arr[0];
    for ( i = 0; i <n; i++)
    {
        if (arr[i]>max)
        {
            max=arr[i];
       }
       if (arr[i]<min)
       {
            min=arr[i];
       }
       
        
    }
    printf("The Max value is %d\n",max);
    printf("The Min value is %d",min);
    
}