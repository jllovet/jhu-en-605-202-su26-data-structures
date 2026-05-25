/**
 *  Copyright 2025, The Johns Hopkins University Whiting School of Engineering All rights reserved.
 *  This material may be used, modified and reproduced by faculty, staff, and students of The Johns
 *  Hopkins University for instruction, evaluation, and grading purposes. For any other permission,
 *  please contact The Johns Hopkins University Whiting School of Engineering.
 */

 /**
 * Implementation of IntegerStack object.
 * Warning, this code is NOT complete and does not handle error scenarios
 */

#include "integer_stack.h"

IntegerStack::IntegerStack(int height){
    this->max_items = height;
    this->items = new int[max_items];
    this->top = 0;
}

IntegerStack::~IntegerStack(){
    // Always clean up heap allocated memory
    delete this->items;
}

bool IntegerStack::is_empty(){
    return this->top <= 0;
}

bool IntegerStack::is_full(){
    return this->top >= this->max_items;
}

int IntegerStack::pop(){
    int ret_value = this->items[this->top];
    --this->top;
    return ret_value;
}

void IntegerStack::push(int number){
    ++this->top;
    this->items[this->top] = number;
}
