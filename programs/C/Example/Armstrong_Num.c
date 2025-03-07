// Armstrong Number: A number that equals the sum of its digits,each raised to a power. Ex: 153 -> 1^3 + 5^3 + 3^3=153

#include<stdio.h>
#include<math.h>
void main()
{
    int n,copy,digit=0,sum=0;
    printf("Enter the value of n:");
    scanf("%d",&n);

    copy=n;

    while (copy>0)
    {
        copy = copy/10;
        digit++;
    }

    copy=n;

    while (copy>0)
    {
        sum = sum + pow((copy%10),digit);
        copy = copy/10;
    }

    if(sum==n){
        printf("The Number is Armstrong Number");
    }
    else
    {
        printf("The Number is Not a Armstrong Number");
    }
    
    
    
}
