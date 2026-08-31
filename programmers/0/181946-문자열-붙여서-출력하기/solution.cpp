#include <iostream>

// 문자열 길이를 구하는 함수 (strlen 구현)
int get_length(const char* str) {
    int len = 0;
    while (str[len] != '\0') {
        len++;
    }
    return len;
}

int main() {
    char str1[11];
    char str2[11];
    
    std::cin >> str1 >> str2;
    
    int len1 = get_length(str1);
    int len2 = get_length(str2);
    
    // 두 문자열을 이은 새로운 문자열 저장 공간 동적 할당. 두 길이 합 + 널 문자 공간 1바이트까지.
    char* result = new char[len1 + len2 + 1];
    
    int i = 0;
    for (int j = 0; j < len1; j++) {
        result[i++] = str1[j];
    }
    
    for (int j = 0; j < len2; j++) {
        result[i++] = str2[j];
    }
    
    result[i] = '\0';
    
    std::cout << result << std::endl;
    delete[] result;
    return 0;
}

// const char* 
// *포인터: 주소값을 저장하는 변수. 메모리의 어딘가를 가리키고 있다는 뜻.
// char: 포인터가 가리키는 주소에 가면 문자char 데이터가 있다는 뜻
// const: 포인터를 통해 가리키고 있는 문자 데이터를 변경할 수 없다는 뜻