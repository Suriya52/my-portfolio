#include<stdio.h>

int add(int a, int b)
{
    int c = a+b;
    int d = a-b;
    printf(" Sub:%d \n",d);

    return c;
}

void main()
    
{
    int a=21;
    int b=32;
    

    printf("%d \n",add(a,b));

    printf("%d",add(123,23));

    

}