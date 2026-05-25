/**
 *  Copyright 2025, The Johns Hopkins University Whiting School of Engineering All rights reserved.
 *  This material may be used, modified and reproduced by faculty, staff, and students of The Johns
 *  Hopkins University for instruction, evaluation, and grading purposes. For any other permission,
 *  please contact The Johns Hopkins University Whiting School of Engineering.
 */

#pragma once

/**
 * Class (really a struct) used to store runtime metrics.
 * This class is so simple that its probably ok to not have a matching
 * cpp file, implementing the "code" in the header.
 */
class RuntimeMetric{
    private:
        long size;
        long runtime;

    public:
        RuntimeMetric(long n, long t){
            size = n;
            runtime = t;
        };

        long get_runtime(){
            return runtime;
        }

        long get_size(){
            return size;
        }
};
