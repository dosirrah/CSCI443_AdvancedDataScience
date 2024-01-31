#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>


double arr_add_constant(int n) {
    // Dynamically allocate memory for the array
    double* array = (double*)malloc(n * sizeof(double));
    if (array == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        return 1;
    }

    // Seed the random number generator
    srand(time(NULL));

    // Initialize the array with random floating-point values
    for (int i = 0; i < n; i++) {
        array[i] = (double)rand() / RAND_MAX * 100.0; // Random doubles between 0.0 and 100.0
    }

    // Define the constant to be added
    double constant = 10.0;

    // Declare variables for timing
    struct timeval start, end;

    // Start the timer
    gettimeofday(&start, NULL);

    // Add the constant to each element of the array
    for (int i = 0; i < n; i++) {
        array[i] += constant;
    }

    // Stop the timer
    gettimeofday(&end, NULL);

    // Calculate the time taken in seconds
    double time_taken = (end.tv_sec - start.tv_sec) * 1e6;
    time_taken = (time_taken + (end.tv_usec - start.tv_usec)) * 1e-6;

    // Print the time taken
    //printf("Time taken to increment array elements: %f seconds\n", time_taken);

    // Free the dynamically allocated memory
    free(array);

    return time_taken;

}


int main() {
    int n;
  
    // Open a file for writing the CSV data
    FILE *file = fopen("example_1_array_c_output.csv", "w");
    if (file == NULL) {
        fprintf(stderr, "Error opening file\n");
        return 1;
    }

    // Write the CSV header
    fprintf(file, "n,t\n");

    for (n = 1000; n < 10000; n += 100) {
        double result = arr_add_constant(n);
        fprintf(file, "%d,%f\n", n, result);
    }

    // Close the file
    fclose(file);

        // Open a file for writing the CSV data
    file = fopen("example_1_array_c_big_output.csv", "w");
    if (file == NULL) {
        fprintf(stderr, "Error opening file\n");
        return 1;
    }

      
    for (n = 1000; n < 100000; n+= 1000) {
        double result = arr_add_constant(n);
        fprintf(file, "%d,%f\n", n, result);
    }
    
    // Close the file
    fclose(file);


    return 0;
}
