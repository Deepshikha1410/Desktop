Ques 3 two array Addition using GPU and CPU code

# %%writefile add_array.cu
# #include <stdio.h>
# #include <stdlib.h>
# #include <time.h>
# #include <cuda.h>
# 
# #define SIZE 1000000
# 
# // Function for addition two arrays on the CPU 
# void add_cpu(int *a, int *b, int *c, int size) {
#         for (int i = 0; i < size; i++) {
#         c[i] = a[i] + b[i];
#     }
# }
# 
# // Function for addition two arrays on the GPU
# __global__ void add_gpu(int *a, int *b, int *c, int size) {
#     int i = blockIdx.x * blockDim.x + threadIdx.x;
#     if (i < size) {
#         c[i] = a[i] + b[i];
#     }
# }
# 
# int main() {
#     // memory allocated on the host 
#     int *a = (int *)malloc(SIZE * sizeof(int));
#     int *b = (int *)malloc(SIZE * sizeof(int));
#     int *c_cpu = (int *)malloc(SIZE * sizeof(int));
#     int *c_gpu = (int *)malloc(SIZE * sizeof(int));
# 
#     // Initialize the arrays
#     for (int i = 0; i < SIZE; i++) {
#         a[i] = i;
#         b[i] = i;
#     }
# 
#     // CPU execution
#     clock_t start_cpu = clock();
#     add_cpu(a, b, c_cpu, SIZE);
#     clock_t end_cpu = clock();
#     double cpu_time = (double)(end_cpu - start_cpu) / CLOCKS_PER_SEC;
# 
#     // GPU execution
#     int *d_a, *d_b, *d_c;
#     cudaMalloc((void **)&d_a, SIZE * sizeof(int));
#     cudaMalloc((void **)&d_b, SIZE * sizeof(int));
#     cudaMalloc((void **)&d_c, SIZE * sizeof(int));
# 
#     cudaMemcpy(d_a, a, SIZE * sizeof(int), cudaMemcpyHostToDevice);
#     cudaMemcpy(d_b, b, SIZE * sizeof(int), cudaMemcpyHostToDevice);
# 
#     clock_t start_gpu = clock();
#     add_gpu<<<1, 1>>>(d_a, d_b, d_c, SIZE);
#     cudaDeviceSynchronize();
#     clock_t end_gpu = clock();
#     double gpu_time = (double)(end_gpu - start_gpu) / CLOCKS_PER_SEC;
# 
#     cudaMemcpy(c_gpu, d_c, SIZE * sizeof(int), cudaMemcpyDeviceToHost);
# 
#     cudaFree(d_a);
#     cudaFree(d_b);
#     cudaFree(d_c);
# 
#     // Print the results
#     printf("CPU time: %f seconds\n", cpu_time);
#     printf("GPU time: %f seconds\n", gpu_time);
# 
#     // Free the memory
#     free(a);
#     free(b);
#     free(c_cpu);
#     free(c_gpu);
# 
#     return 0;
# }

//Compilation Command
!nvcc -o add_array add_array.cu
Runcommand
!./add_array
