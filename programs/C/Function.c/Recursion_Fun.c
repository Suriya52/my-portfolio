

// Recursion Function

# include<stdio.h>

int fact(int n){                  // Factorial of a Number
    
    if ( n <=1)        // *(Base case)*           // 0 or 1 Factorial is 1 so we declare this.                  
    
        return 1;

        return n*fact(n-1);     //*(Recasive Case)*    // 5 * 4! then it runs again 4 * 3! ......
    
    
}

void main(){

    int n=5;

    int c=fact(n);            // Function call

    printf("%d",c);


}

// Output : 5 ! is 120