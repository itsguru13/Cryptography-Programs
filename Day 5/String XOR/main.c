#include <stdio.h>
#include <string.h>

int main()  {
    char text[25];
    int i, len, result;
    printf("Enter a text: ");
    scanf("%s", &text);
    len = strlen(text);
    
    for(i=0; i<len; i++)   {
        result = text[i] & 127;
        printf("%c AND 127: %d\n", text[i], result); 
    }

    printf("\n");
    
    for(i=0; i<len; i++)   {
        result = text[i] ^ 127;
        printf("%c XOR 127: %d\n", text[i], result); 
    }
}