#include<stdio.h>

int main(){

    FILE *fp;



    fp=fopen("test.txt","w");     //  File Write "w"

    fputc('c',fp);
    fputs("Hello Suriya",fp);

    fclose(fp);

    
}
