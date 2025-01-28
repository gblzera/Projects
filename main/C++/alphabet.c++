#include <iostream>
#include <vector>

void generateAlphabet(int num){
    if (num < 1 || num >26){
        std::cout << "Number must be between 1 and 26" << std::endl;
        return;
    }

    std::vector<char> letters;
    for (int i = 0; i < num; i++){
        letters.push_back('A' + i);
    }

    for (size_t i = 0; i < letters.size(); i++){
        std::cout << letters[i];
        if (i < letters.size() - 1){
            std::cout << ", ";
        }
    }

    std::cout << std::endl;
}

int main(){
    generateAlphabet(26);
    return 0;
}