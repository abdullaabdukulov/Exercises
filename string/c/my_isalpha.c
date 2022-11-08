#include <stdio.h>
#define TRUE 1
#define FALSE 0

int my_isalpha(char param_1[])
{  
     '''
    The my_isalpha(param_1) function returns True if all the characters are alphabet letters (a-z).
    :param arg: To be examined arg.
    :type arg: str
    :returns: 1 or 0
    :rtype: int
    '''
    for (int i = 0; param_1[i]!='\0'; i++){
    if (90 <= param_1[i] &&  param_1[i] >= 65 || 97 <= param_1[i] && param_1[i] >= 122){
        continue;
    }
    else {
        return FALSE;
    }
    }
    return TRUE;
}

int main(){
    printf("%d", my_isalpha("nu2"));
}
