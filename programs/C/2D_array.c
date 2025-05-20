#include<stdio.h>
void main()
{
    int arr[2][2],i,j;              // 2D Array Declaraction

    for ( i = 0; i < 2; i++)
    {
        for ( j = 0; j < 2; j++)
        {
            printf("Enter the Element:");
            scanf("%d",&arr[i][j]);
        }
        
    }

    for ( i = 0; i < 2; i++)
    {
        for ( j = 0; j < 2; j++)
        {
            printf("%d",arr[i][j]);
            
        }
        printf("\n");
    }
     
}