// Calculator

/*#include<stdio.h>

void main()
{
    int num1,num2;
    char op;

    printf("Enter a Number 1:");
    scanf("%d",&num1);

    printf("Enter a Number 2:");
    scanf("%d",&num2);

    printf("Enter the opertor:");
    scanf("\n %c",&op);

    if ( op == '+')
    {
        printf("Add:%d",num1 + num2);
    }

    else if ( op == '-')
    {
        printf("Sub:%d",num1 - num2);
    }

     else if ( op == '*')
    {
        printf("Multi:%d",num1 * num2);
    }

     else if ( op == '/')
    {
        printf("Div:%d",num1 / num2);
    }

    else
    {
        printf("Invalid Operator");
    }
    
}*/


// Using Switch Case

#include<stdio.h>
void main()
{
    int num1,num2;
    char op;

    printf("Enter a Number 1:");
    scanf("%d",&num1);

    printf("Enter a Number 2:");
    scanf("%d",&num2);

    printf("Enter the opertor:");
    scanf("\n %c",&op);

    switch (op)
    {
    case ('+'):
        printf("Add: %d",num1 + num2);
        break;
    case ('-'):
        printf("Sub: %d",num1 - num2);
        break;
    case ('*'):
        printf("Mul: %d",num1 * num2);
        break;
    case ('/'):
        printf("Div: %d",num1 / num2);
        break;
    
    default:
        printf("Invalid Operator");
        break;
    }
}