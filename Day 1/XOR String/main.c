#include <stdio.h>
#include <string.h>

int main()  {
    int i, n, result;
    char text[25];
    printf("Enter a string: ");
    scanf("%s", &text);
    n = strlen(text);
    for(i=0; i<n; i++)  {
        result = text[i]^0;
        printf("%d \n", result);
    }
}