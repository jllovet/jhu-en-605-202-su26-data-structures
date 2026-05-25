/**
 *  Copyright 2025, The Johns Hopkins University Whiting School of Engineering All rights reserved.
 *  This material may be used, modified and reproduced by faculty, staff, and students of The Johns
 *  Hopkins University for instruction, evaluation, and grading purposes. For any other permission,
 *  please contact The Johns Hopkins University Whiting School of Engineering.
 */

#pragma once

#include <string>

/**
 * Converts numbers from one base (decimal) to another (binary)
 */
class BaseConverter{
    private:
        // Max number of bits to display
        int max_digits;

    public:
        /**
         * Create a converter that supports a maximum number of digits in the conversion result.
         * @param num_digits: max number of digits in conversion result
         */
        BaseConverter(int num_digits);

        /**
         * Uses this converter to convert a number into a binary string
         * @param dec_num: number to convert
         */
        std::string dec_to_bin(int dec_num);

};
