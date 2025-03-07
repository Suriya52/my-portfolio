#include<stdio.h>

int main(){

    FILE *fp;

    char c[100];

    fp=fopen("test.txt","r");          // Read file "r"

    fgets(c,20,fp);
    printf("%s",c);

    fclose(fp);

    
}
