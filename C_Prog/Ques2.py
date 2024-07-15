
"""Find the Minimum and Maximum element of the array"""

# %%writefile find_min_max.cu
# #include <stdio.h>
# #include <stdlib.h>
# #include <time.h>
# #include <cuda.h>
# 
# #define SIZE 10000000
# 
# //find minimum maximum on the CPU
# void find_min_max(int *arr, int size, int *min, int *max) {
#     *min = arr[0];
#     *max = arr[0];
#     for (int i = 1; i < size; i++) {
#         if (arr[i] < *min) {
#             *min = arr[i];
#         }
#         if (arr[i] > *max) {
#             *max = arr[i];
#         }
#     }
# }
# 
# // on the gpu
# __global__ void find_min_max_gpu(int *arr, int size, int *min, int *max) {
#     int i = blockIdx.x * blockDim.x + threadIdx.x;
#     if (i < size) {
#         if (arr[i] < *min) {
#             *min = arr[i];
#         }
#         if (arr[i] > *max) {
#             *max = arr[i];
#         }
#     }
# }
# 
# int main() {
#     // Allocate memory on the host
#     int *arr = (int *)malloc(SIZE * sizeof(int));
# 
#     // Initialize the array with non-negative elements
#     srand(time(NULL));
#     for (int i = 0; i < SIZE; i++) {
#         arr[i] = rand() % 1000000;
#     }
# 
#     // CPU execution
#     int min_cpu, max_cpu;
#     clock_t start_cpu = clock();
#     find_min_max_cpu(arr, SIZE, &min_cpu, &max_cpu);
#     clock_t end_cpu = clock();
#     double cpu_time = (double)(end_cpu - start_cpu) / CLOCKS_PER_SEC;
# 
#     // GPU execution
#     int *d_arr, d_min, d_max;
#     cudaMalloc((void **)&d_arr, SIZE * sizeof(int));
#     cudaMemcpy(d_arr, arr, SIZE * sizeof(int), cudaMemcpyHostToDevice);
#     clock_t start_gpu = clock();
#     find_min_max_gpu<<<1, 1>>>(d_arr, SIZE, &d_min, &d_max);
#     clock_t end_gpu = clock();
#     double gpu_time = (double)(end_gpu - start_gpu) / CLOCKS_PER_SEC;
# 
#     // Print the results
#     printf("CPU execution time: %.6f seconds\n", cpu_time);
#     printf("GPU execution time: %.6f seconds\n", gpu_time);
# 
#     // Free up memory
#     free(arr);
#     cudaFree(d_arr);
# 
#     return 0;
# }

//File compilation command
!nvcc -o find_min_max find_min_max.cu

//Runc command for file
!./find_min_max
