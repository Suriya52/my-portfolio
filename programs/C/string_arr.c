#include<stdio.h>
#include<string.h>
void main()
{
    int n,i;
    char str1[50],str2[50];

    //printf("Enter the n :");
    //scanf("%d",&n);

    //n=strlen(str1);             // string Function

    printf("Enter the string 1:");
    scanf("%s",&str1);

    printf("Enter the string 2:");
    scanf("%s",&str2);



    //strcat(str1,str2);            // Adding two string function.

    //printf("%d",strcmp(str1,str2));             // comparing two string.  0= Equal, 1= Not Equal

    printf("%s",strrev(str1));                    // Reverse the String.
    
    
    //printf("%s \n",str1);     // We can use this or for loop to print the character.

    /*for ( i = 0; i <n; i++)
    {
        printf("%c",str[i]);
        
    }*/
    
}