/**
 *  Copyright 2025, The Johns Hopkins University Whiting School of Engineering All rights reserved.
 *  This material may be used, modified and reproduced by faculty, staff, and students of The Johns
 *  Hopkins University for instruction, evaluation, and grading purposes. For any other permission,
 *  please contact The Johns Hopkins University Whiting School of Engineering.
 */

/**
 * This file is the entry point into this program when the module is executed as a standalone program. IE './proj0'.
 * Generally, main should return an int, and may take some arguments. It's a good idea to use this file for handling
 * and/or opening input and output files, and not much else. This code should "drive" the code you want to run, hence
 * it is often referred to as a 'main driver'
 */

// This library provides input/output functions such as reading and writing to files
#include <iostream>
#include <fstream>
#include <filesystem>
#include "runtime_metric.h"
#include "base_converter.h"
#include <cmath>

void printUsage(int argc, char** argv){
    // argv[0] should always be the name of the program as run
    std::cout << argv[0] << " is expecting two command line arguments: input_file output_file" << std::endl;
    std::cout << argc << " argument(s) provided." << std::endl;
    exit(1);
}

/**
 * Helper function to get the absolute file path to a file. Very useful when relative paths are incorrect.
 * @param pathString: String representation of file path
 */
std::string getAbsolutePath(char* pathString) {
    try {
        std::filesystem::path absolutePath = std::filesystem::absolute(pathString);
        return absolutePath.string();
    }
    catch (const std::filesystem::filesystem_error& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return "";
    }
}

void write_message(std::ofstream &output_file, const char* err_message, bool is_error = false){
    if (is_error){
        std::cerr << err_message << std::endl;
    }else{
        std::cout << err_message << std::endl;
    }
    output_file << err_message << std::endl;
}

/**
 * The main entrypoint into this program. This code runs first.
 * Expecting command line arguments: <input_file> <output_file>
 * 
 * @param argc: Number of arguments (char* strings) passed to the program
 * @param argv: Array of 'string' values representing each argument.
 */
int main(int argc, char **argv){
    if (argc != 3){
        printUsage(argc, argv);
    }

    // Open up the first argument for reading (Input)
    char* input_file_name = argv[1];
    std::string input_file_path = getAbsolutePath(input_file_name);
    std::ifstream input_file(input_file_path);
    if (input_file.bad()){
        std::cerr << "Input file " << input_file_name << " failed to open" << std::endl;
        return 1;
    }
    std::cout << "Reading input from " << input_file_path << std::endl;

    // Open up the second argument for writing (Output)
    char* output_file_name = argv[2];
    std::string output_file_path = getAbsolutePath(output_file_name);
    std::ofstream output_file(output_file_path);
    if (output_file.bad()){
        std::cerr << "Output file " << output_file_path << " failed to open" << std::endl;
        return 1;
    }
    std::cout << "Writing output to " << output_file_path << std::endl;

    // the () at the end initializes all values to nullptr
    RuntimeMetric** metrics = new RuntimeMetric*[100]();
    int conversions = 0;
    long next_value;
    while (input_file >> next_value){
        if (next_value < 0){
            write_message(output_file, "Invalid value, cannot be negative", true);
            continue;
        }
        if (next_value > std::pow(2,32)){
            write_message(output_file, "Value too large, must be <= 32 bits", true);
            continue;
        }
        
        // Convert the next value to its bit representation and time how long that takes
        BaseConverter bc(32);
        auto start_time = std::chrono::high_resolution_clock::now();
        std::string bits = bc.dec_to_bin(next_value);
        auto end_time = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::nanoseconds>(end_time - start_time);
        metrics[conversions] = new RuntimeMetric(next_value, duration.count());

        // The next two for loops print the output padded and separated by the hexadecimal digit (every 4 bits)
        std::stringstream pretty_output;
        int curr_bit = 0;
        // print the padding for 32 bit alignment
        for (unsigned int padding = 0; padding < 32 - bits.length(); padding++){
            pretty_output << "0";
            curr_bit++;
            // add a space to separate each 4 bits
            if (curr_bit % 4 == 0){
                pretty_output << " ";
            }
        }
        // now print out the data from the converter
        for (unsigned int i = 0; i < bits.length(); i++){
            pretty_output << bits[i];
            curr_bit++;
            // add a space to separate each 4 bits
            if (curr_bit % 4 == 0){
                pretty_output << " ";
            }
        }
        output_file << pretty_output.str() << std::endl;
        conversions++;
    }

    // separate conversions from results
    output_file << std::endl;

    // now print out metrics
    for (int i = 0; i < conversions; i++){
        RuntimeMetric* metric = metrics[i];
        output_file << metric->get_size() << " = " << metric->get_runtime() << std::endl;
        // we're done with the metrics now, best practice is to delete all 'new-ed' memory
        delete metric;
    }
    // no longer need the metrics array
    delete[] metrics;

    if (input_file.fail() && ! input_file.eof()){
        write_message(output_file, "Error reading values from file. Possible invalid integer encountered");
        return 1;
    }
    input_file.close();
    output_file.close();

    return 0;
}
