#include<stdio.h>

int main(){

    FILE *fp;



    fp=fopen("test.txt","a");     //  File Append "a".    "a+" means read and append. For binary add "b" in last

    fputc('c',fp);
    fputs("How are you...!",fp);

    fclose(fp);

    
}
