
// Pointers * is declare to pointers.

#include<stdio.h>
int main(){
    int *a;
    float *b;
    char *c;

    int d=5;
    a=&d;

    printf("%d\n",a);    // address of an a value  6422296
    printf("%d",*a);    // Value of a   5
}