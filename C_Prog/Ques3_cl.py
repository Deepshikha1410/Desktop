"""Addition of two array using opencl"""
# %%writefile addition_array.cl
# #include <stdio.h>
# #include <stdlib.h>
# #include <CL/cl.h>
# 
# #define SIZE 1000000
# 
# // Kernel function for addition of two arrays
# __kernel void array_add_kernel(__global int *A, __global int *B, __global int *C) {
#     int i = get_global_id(0);
#     C[i] = A[i] + B[i];
# }
# 
# int main() {
#     // Allocate memory on the host
#     int *A = (int *)malloc(SIZE * sizeof(int));
#     int *B = (int *)malloc(SIZE * sizeof(int));
#     int *C = (int *)malloc(SIZE * sizeof(int));
# 
#     // Initialize the arrays
#     for (int i = 0; i < SIZE; i++) {
#         A[i] = i;
#         B[i] = i;
#     }
# 
#     // OpenCL setup
#     cl_platform_id platform_id;
#     cl_device_id device_id;
#     cl_context context;
#     cl_command_queue command_queue;
#     cl_program program;
#     cl_kernel kernel;
# 
#     // Get platform and device
#     clGetPlatformIDs(1, &platform_id, NULL);
#     clGetDeviceIDs(platform_id, CL_DEVICE_TYPE_GPU, 1, &device_id, NULL);
#
#      //CreateContext
#     context = clCreateContext(NULL, 1, &device_id, NULL, NULL, NULL);
# 
#     // Create command queue
#     command_queue = clCreateCommandQueue(context, device_id, 0, NULL);
# 
#     // create source
#     char *source = "__kernel void array_add_kernel(__global int *A, __global int *B, __global int *C) {\n"
#                    "    int i = get_global_id(0);\n"
#                    "    C[i] = A[i] + B[i];\n"
#                    "}\n";
# 
#     // Create program
#     program = clCreateProgramWithSource(context, 1, &source, NULL, NULL);
# 
#     // Build program
#     clBuildProgram(program, 1, &device_id, NULL, NULL, NULL);
# 
#     // Create kernel
#     kernel = clCreateKernel(program, "array_add_kernel", NULL);
# 
#     //kernel arguments
#     clSetKernelArg(kernel, 0, sizeof(cl_mem), &A);
#     clSetKernelArg(kernel, 1, sizeof(cl_mem), &B);
#     clSetKernelArg(kernel, 2, sizeof(cl_mem), &C);
# 
#     //kernel arguments
#     clSetKernelArg(kernel, 0, sizeof(cl_mem), (void *)&A);
#     clSetKernelArg(kernel, 1, sizeof(cl_mem), (void *)&B);
#     clSetKernelArg(kernel, 2, sizeof(cl_mem), (void *)&C);
# 
#     // memory buffers 
#     cl_mem A_buffer = clCreateBuffer(context, CL_MEM_READ_ONLY, SIZE * sizeof(int), NULL, NULL);
#     cl_mem B_buffer = clCreateBuffer(context, CL_MEM_READ_ONLY, SIZE * sizeof(int), NULL, NULL);
#     cl_mem C_buffer = clCreateBuffer(context, CL_MEM_WRITE_ONLY, SIZE * sizeof(int), NULL, NULL);
# 
#     // Copy data from host to device
#     clEnqueueWriteBuffer(command_queue, A_buffer, CL_TRUE, 0, SIZE * sizeof(int), A, 0, NULL, NULL);
#     clEnqueueWriteBuffer(command_queue, B_buffer, CL_TRUE, 0, SIZE * sizeof(int), B, 0, NULL, NULL);
# 
#     // Execute
#     size_t global_work_size = SIZE;
#     clEnqueueNDRangeKernel(command_queue, kernel, 1, NULL, &global_work_size, NULL, 0, NULL, NULL);
# 
#     // Copy data from device to host
#     clEnqueueReadBuffer(command_queue, C_buffer, CL_TRUE, 0, SIZE * sizeof(int), C, 0, NULL, NULL);
# 
#     // Print the result
#     for (int i = 0; i < SIZE; i++) {
#         printf("%d + %d = %d\n", A[i], B[i], C[i]);
#     }
# 
#     // Free up
#     clReleaseKernel(kernel);
#     clReleaseProgram(program);
#     clReleaseMemObject(A_buffer);
#     clReleaseMemObject(B_buffer);
#     clReleaseMemObject(C_buffer);
#     clReleaseCommandQueue(command_queue);
#     clReleaseContext(context);
# 
#     free(A);
#     free(B);
#     free(C);
# 
#     return 0;
# }
