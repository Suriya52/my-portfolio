// Conditional statement

// If

/*#include <stdio.h>

void main() {
    int a = 8;
    int b = 4;
    
    if (a != b) 
    {  
        printf("True");
    } 
    else 
    {
        printf("False");
    }
}
*/

// if else if

/*#include<stdio.h>
void main(){
    int a=8;
    int b=7;
    if (a==b)
    {
        printf("Both A and B are equal");
    }
    else if (a>b)
    {
        printf("A is greater than B");
    }
    else
    {
        printf("B is greater than A");
    }
}
*/


// Check the given number is Positive or Not

/*#include<stdio.h>
void main(){
    int num;
    printf("Enter a Number:");
    scanf("%d",&num);

    if(num>0)
    printf("The given Number is Positive");

    else if (num == 0)
    {
        printf("Zero Nether Positive nor Negative");
    }
    
    else
    {
        printf("The given Number is Negative");
    }
}
*/

// Nested if and Finding the give year is leap year or not


#include<stdio.h>
void main(){
    int year;
    printf("Enter a year:");
    scanf("%d",&year);

    if (year % 100 == 0)
    {
        if (year % 400 == 0)
        {
            printf("%d is Leap year",year);
        }
        else
        {
            printf("%d is not a Leap year",year);
        }
    }
    else{
        if (year % 4 == 0)
        {
            printf("%d is Leap year",year);
        }
        else
        {
            printf("%d is not a Leap year",year);
        }
    }
}