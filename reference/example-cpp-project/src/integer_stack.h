/**
 *  Copyright 2025, The Johns Hopkins University Whiting School of Engineering All rights reserved.
 *  This material may be used, modified and reproduced by faculty, staff, and students of The Johns
 *  Hopkins University for instruction, evaluation, and grading purposes. For any other permission,
 *  please contact The Johns Hopkins University Whiting School of Engineering.
 */

/**
 * Definition of an IntegerStack class. Providing abstract interface
 */

#pragma once


class IntegerStack{

private:
    int* items = nullptr;
    int max_items;
    int top;

public:
    /**
     * Constructs an integer stack object with fixed size
     * 
     * @param height: Maximum number of items storable in stack
     */
    IntegerStack(int height);

    /**
     * Deconstructs integer stack object. Cleaning up memory
     */
    ~IntegerStack();

    /**
     * Returns true if no items are in the stack
     */
    bool is_empty();

    /**
     * Returns true if the stack is at capacity
     */
    bool is_full();

    /**
     * Removes and returns the item on top of the stack
     */
    int pop();

    /**
     * Adds a new number to the stack
     * @param number: Integer to add to the stack
     */
    void push(int number);
};
