#include <stdio.h>
#include <string.h>

int main() {
    char buffer[10];  // Declare a fixed-size buffer with size 10
    
    printf("Enter a string (up to 9 characters): ");
    
    // Unsafe function that doesn't limit input length
    gets(buffer);  // Warning: gets() is unsafe and should never be used in production code.
    
    // Print the entered string
    printf("You entered: %s\n", buffer);
    
    // Demonstrate buffer overflow: If you input more than 9 characters, it will overflow
    // and overwrite adjacent memory, potentially causing unexpected behavior.

    return 0;
}
