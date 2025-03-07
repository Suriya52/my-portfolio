#include<stdio.h>
void main()
{

    int i,j,n;

    printf("Enter a n Number:");
    scanf("%d",&n);

    for ( i = 1; i <=n ; i++)
    {
        for ( j = 1; j <=i; j++)
        {
            printf("%d ",j);
        }
        printf("\n");
    }
    

}

// Output: 4
/*
1
1 2
1 2 3
1 2 3 4
*/