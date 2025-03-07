#include<stdio.h>
void main()
{
    int arr1[3][3],arr2[3][3],i,j;

    for ( i = 0; i < 3; i++)
    {
        for ( j = 0; j < 3; j++)
        {
            printf("Enter the Element:");
            scanf("%d",&arr1[i][j]);
        }
        
    }

    printf("Next Array\n");
    for ( i = 0; i < 3; i++)
    {
        for ( j = 0; j < 3; j++)
        {
            arr2[i][j]=arr1[j][i];
        }
        
    }
    
    for ( i = 0; i < 3; i++)
    {
        for ( j = 0; j < 3; j++)
        {
            printf("%d ", arr2[i][j]);
        }
        printf("\n");
    }
}


// Output:     

/* 
    This the output we get:

    1 2 3
    4 5 6
    7 8 9

    Transpose Matrix is:
    
    1 4 7
    2 5 8
    3 6 9
*/