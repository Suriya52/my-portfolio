
// Structure

#include<stdio.h>
#include<string.h>
struct Book
{
    int No;
    char Author[50];
    float price;
};


int main(){
    int a;
    a=5;
    struct Book Ps1;
    struct Book Ps2;
    
    
        Ps1.No=1;
        Ps1.price=579.80;
        strcpy(Ps1.Author,"Kalki");

        Ps2.No=2;
        Ps2.price=590.78;
        strcpy(Ps2.Author,"Kalki");

        printf("%d \n",Ps1.No);

        printf("%f \n",Ps1.price);

        printf("%s \n",Ps1.Author);

        printf("%d \n",Ps2.No);

        printf("%f \n",Ps2.price);

        printf("%s",Ps2.Author);
    
}