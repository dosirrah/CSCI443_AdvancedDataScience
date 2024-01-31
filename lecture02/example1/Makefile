# Makefile for example_1_array_add

# Compiler to use
CC = gcc

# Compiler flags
CFLAGS = -Wall -Wextra -std=c99

# Name of the output executable
TARGET = example_1_array_add

# Default target
all: $(TARGET)

# Compile the program
$(TARGET): example_1_array_add.c
	$(CC) $(CFLAGS) example_1_array_add.c -o $(TARGET) -lm

# Clean up
clean:
	rm -f $(TARGET)
