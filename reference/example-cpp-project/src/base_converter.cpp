/**
 *  Copyright 2025, The Johns Hopkins University Whiting School of Engineering All rights reserved.
 *  This material may be used, modified and reproduced by faculty, staff, and students of The Johns
 *  Hopkins University for instruction, evaluation, and grading purposes. For any other permission,
 *  please contact The Johns Hopkins University Whiting School of Engineering.
 */

 #include <sstream>

#include "base_converter.h"
#include "integer_stack.h"

BaseConverter::BaseConverter(int num_digits):
    max_digits(num_digits){};


std::string BaseConverter::dec_to_bin(int decNum){
    long nextNum;
    int remainder;
    int totalBits;
    
    IntegerStack* stack = new IntegerStack(max_digits);
    
    nextNum = decNum;
    totalBits = 0;
    while (nextNum > 0) {
        remainder = (int)(nextNum % 2);
        stack->push(remainder);
        totalBits++;
        nextNum /= 2;
    }
    
    std::stringstream binary_buffer;
    for (int i = totalBits; i > 0; i--)
        binary_buffer << stack->pop();
    
    return binary_buffer.str();
};
