SUB_DIR := src
BUILD_DIR := build
TARGET := proj0
EXEC := $(BUILD_DIR)/$(TARGET)

# Detect all cpp files in the src directory
SRC := $(wildcard $(SUB_DIR)/*.cpp)

# Use pattern substitution to create a list of object files (.o) from the source files (.cpp), store them in the build directory
OBJ := $(SRC:$(SUB_DIR)/%.cpp=$(BUILD_DIR)/%.o)

# Define any compiler flags you want to use (e.g., for optimization, debugging, or warnings)
CXXFLAGS := -Wall -O2 -std=c++17

# Default rule:  Build the executable
all: $(EXEC)

# Lazy rule to run with default parameters
run: $(EXEC)
	$(EXEC) io/input.txt io/output.txt

# Create the build directory if it doesn't exist
# Might not work in command prompt, requiring powershell
$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

# Rule to link the object files to create the executable
$(EXEC): $(BUILD_DIR) $(OBJ)
	$(CXX) $(CXXFLAGS) -o $(EXEC) $(OBJ)

# Rule to compile each .cpp file into its corresponding .o file
$(BUILD_DIR)/%.o: $(SUB_DIR)/%.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Clean rule:  Remove the object/executable files
clean:
	rm -f $(OBJ) $(TARGET)

# make the all/clean commands usable repeatedly
.PHONY: all clean run
