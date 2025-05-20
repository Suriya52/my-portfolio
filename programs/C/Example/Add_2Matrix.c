
// Adding two matrix

#include<stdio.h>
void main()
{
    int arr1[2][2],arr2[2][2],i,j;

    for ( i = 0; i < 2; i++)            // Nested loop
    {
        for ( j = 0; j < 2; j++)
        {
            printf("Enter the Element:");           
            scanf("%d",&arr1[i][j]);           // Getting arr1
        }
        
    }

    printf("Next Array\n");
    for ( i = 0; i < 2; i++)
    {
        for ( j = 0; j < 2; j++)
        {
            printf("Enter the Element:");
            scanf("%d",&arr2[i][j]);           // Getting arr2
        }
        
    }
    
    for ( i = 0; i < 2; i++)
    {
        for ( j = 0; j < 2; j++)
        {
            printf("%d ",arr1[i][j] + arr2[i][j]);      // Adding arr1 and arr2
        }
        printf("\n");
    }
}