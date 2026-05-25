# Proj 0

This is an analog to the Java Proj0 posted on the course site. It is far from perfect and is meant to be representative of a 'B' level submission.

This readme is written in [Markdown](https://dillinger.io/). Use the link to render if needed. Most IDEs render markdown, and it is currently a de facto standard in modern day software documentation.

This project also includes a guide on formatting cpp projects.

## Running Proj 0

> NOTE: Your IDE may not immediately understand this "makefile" project. 

1. Download and install a cpp compiler on your computer.
    * You may need to also install "make" as well depending on whether or not your compiler bundled it.
    * You may need to add both programs to your "Path"
2. Navigate to [this](.) directory (containing the README.md) using a terminal application
3. Build the program using make: `make`. 
    * This will create (if needed) a build folder and compile the executable into it.
4. Run the program using make: `make run`. 
    * This is a default runtime included in the Makefile. It will run the program with the default input/in.txt and 
    output/out.txt arguments.
4. Run the program with different inputs: `build/proj0 input/a_different_input.txt output/some_output_file`
    * Be sure that the input file you choose actually exists and that the output's parent folder exists.

Output will be written to the specified output file after processing the input file.

### Proj 0 Usage:

```commandline
usage: ./proj0 in_file out_file

positional arguments:
  in_file     Input File Pathname
  out_file    Output File Pathname
```

Usage statements are very formalized. Here is an explanation on what that output above was saying:

| Symbol        | Meaning                                                                                                            |
|---------------|--------------------------------------------------------------------------------------------------------------------|
| [var]         | variable var is optional.                                                                                          |
| var           | variable var is required. All positional arguments are required.                                                   |
| -v, --version | This refers to a flag. One dash + one letter OR two dashes and a whole word. Some flags take one or more arguments |
| +             | This argument consumes 1 or more values                                                                            |
| *             | This argument consumes 0 or more values                                                                            |

## Sample CPP Packaging

There are many ways to package C++ code. This example project isn't arguably the best, nor is it complete, but it does
provide some basic guidance on what to expect and how projects should generally be structured.

### Project Layout

You can copy this folder and its contents, and rename things to lab1, lab2, etc. Just be sure to update the file names,
contents, etc. You especially will want to update the Makefile, which is fairly generic, but is expecting a sensible 
value for `TARGET`. IE for lab1, change:

```makefile
SUB_DIR := src
BUILD_DIR := build
TARGET := proj0
EXEC := $(BUILD_DIR)/$(TARGET)
...
```

to

```makefile
SUB_DIR := src
BUILD_DIR := build
TARGET := lab1
EXEC := $(BUILD_DIR)/$(TARGET)
...
```

* [proj0/](.): The parent or "root" folder containing all of these files/
    * [README.md](README.md):
      The guide you're reading. All software should come with a readme!
    * [Makefile](Makefile):
      This file is used to make compiling and running code easier. It's worth learning how Makefiles work (when you have
      time)
    * [src](src): 
      This is where we keep our C++ source files to keep things 'tidy'
      * [main.cpp](src/main.cpp): 
        This file is the entrypoint to your program when ran as a program. It usually just handles command line
        arguments and 'drives' the rest of the program.
      * `*.h`:
        These are your C++ header files, used to define how objects can be used
      * `*.c` / `*.cpp`:
        These are your C++ source files, used to implement the features described in the header files


## What To Submit

Create a project like this for each lab. IE username_lab1. DO not put all of your source in one file. Splitting code up
into files that "do one thing" is a great way to make it reusable, easier to read, make reviewing code more manageable.

Inside that project, include your code, analysis, copies of input/output, compiled executable, and a readme.

Zip your package.

Avoid including:
* IDE setting files (ie .idea/ .vscode/ .eclipse/ etc)
* Build cache files (*.o)
* Any binary data
* Extraneous logs
* etc
