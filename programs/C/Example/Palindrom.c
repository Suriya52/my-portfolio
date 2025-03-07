// Reverseive of a Number

/*
#include<stdio.h>
void main()
{
    int n,copy,rev=0;

    printf("Enter the Number:");
    scanf("%d",&n);

    copy=n;

    while (copy>0)
    {
        rev=rev*10;       // changing 1s into 100s
        rev=rev + (copy%10);
        copy /= 10;       // copy = copy / 10;
    }
    printf("Reversed Number is:%d",rev);
    
}*/

//Palindrom of a Number

#include<stdio.h>
void main()
{
    int n,copy,rev=0;

    printf("Enter the Number:");
    scanf("%d",&n);

    copy=n;

    while (copy>0)
    {
        rev=rev*10;       // changing 1s into 100s
        rev=rev + (copy%10);
        copy /= 10;       // copy = copy / 10;
    }
    if(n==rev)
    {
        printf("It is a Palindrome");
    }
    else
    {
        printf("Not a Palindrome");
    }
    
}