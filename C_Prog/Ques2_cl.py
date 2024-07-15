# %%writefile max_min.cl
# #include <stdio.h>
# #include <stdlib.h>
# #include <time.h>
# #include <CL/cl.h>
# 
# #define SIZE 10000000
# 
# // Kernel function for minimum and maximum
# __kernel void min_max_kernel(__global int *data, __local int *local_min, __local int *local_max, __global int *global_min, __global int *global_max) {
#     int i = get_global_id(0);
#     int local_id = get_local_id(0);
# 
#     // Initialize local minimum and maximum
#     local_min[local_id] = data[i];
#     local_max[local_id] = data[i];
# 
#     // find the min and max
#     for (int j = 1; j < get_local_size(0); j++) {
#         if (data[i + j] < local_min[local_id]) {
#             local_min[local_id] = data[i + j];
#         }
#         if (data[i + j] > local_max[local_id]) {
#             local_max[local_id] = data[i + j];
#         }
#     }
# 
#     // Synchronizing
#     barrier(CLK_LOCAL_MEM_FENCE);
# 
#     // find
#     if (local_id == 0) {
#         // Initialize global minimum and maximum
#         global_min[0] = local_min[0];
#         global_max[0] = local_max[0];
# 
#         // find
#         for (int j = 1; j < get_local_size(0); j++) {
#             if (local_min[j] < global_min[0]) {
#                 global_min[0] = local_min[j];
#             }
#             if (local_max[j] > global_max[0]) {
#                 global_max[0] = local_max[j];
#             }
#         }
#     }
# }
# 
# int main() {
#     // Allocate memory on the host
#     int *data = (int *)malloc(SIZE * sizeof(int));
#     // Initialize the array with non-negative elements
#     for (int i = 0; i < SIZE; i++) {
#         data[i] = rand() % 1000;
#     }
# 
#     // OpenCL setup commands
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
#     // Create context
#     context = clCreateContext(NULL, 1, &device_id, NULL, NULL, NULL);
# 
#     // Create command queue
#     command_queue = clCreateCommandQueue(context, device_id, 0, NULL);
# 
#     // source code
#     char *source = "__kernel void min_max_kernel(__global int *data, __local int *local_min, __local int *local_max, __global int *global_min, __global int *global_max) {\n"
#                    "    int i = get_global_id(0);\n"
#                    "    int local_id = get_local_id(0);\n"
#                    "    local_min[local_id] = data[i];\n"
#                    "    local_max[local_id] = data[i];\n"
#                    "    for (int j = 1; j < get_local_size(0); j++) {\n"
#                    "        if (data[i + j] < local_min[local_id]) {\n"
#                    "            local_min[local_id] = data[i + j];\n"
#                    "        }\n"
#                    "        if (data[i + j] > local_max[local_id]) {\n"
#                    "            local_max[local_id] = data[i + j];\n"
#                    "        }\n"
#                    "    }\n"
#                    "    barrier(CLK_LOCAL_MEM_FENCE);\n"
# 
#                    "    if (local_id == 0) {\n"
#                    "        global_min[0] = local_min[0];\n"
#                    "        global_max[0] = local_max[0];\n"
#                    "        for (int j = 1; j < get_local_size(0); j++) {\n"
#                    "            if (local_min[j] < global_min[0]) {\n"
#                    "                global_min[0] = local_min[j];\n"
#                    "            }\n"
#                    "            if (local_max[j] > global_max[0]) {\n"
#                    "                global_max[0] = local_max[j];\n"
#                    "            }\n"
#                    "        }\n"
#                    "    }\n"
#                    "}\n";
# 
#     // Create program
#     program = clCreateWithSource(context, 1, &source, NULL, NULL);
# 
#     // Build program
#     clBuildProgram(program, 1, &device_id, NULL, NULL, NULL);
# 
#     // kernel
#     kernel = clCreateKernel(program, "min_max_kernel", NULL);
# 
#     // memory buffers on the device
#     cl_mem data_buffer = clCreateBuffer(context, CL_MEM_READ_ONLY, SIZE * sizeof(int), NULL, NULL);
#     cl_mem local_min_buffer = clCreateBuffer(context, CL_MEM_LOCAL, get_local_size(0) * sizeof(int), NULL, NULL);
#     cl_mem local_max_buffer = clCreateBuffer(context, CL_MEM_LOCAL, get_local_size(0) * sizeof(int), NULL, NULL);
#     cl_mem global_min_buffer = clCreateBuffer(context, CL_MEM_WRITE_ONLY, sizeof(int), NULL, NULL);
#     cl_mem global_max_buffer = clCreateBuffer(context, CL_MEM_WRITE_ONLY, sizeof(int), NULL, NULL);
# 
#     // Copy data from host to device
#     clEnqueueWriteBuffer(command_queue, data_buffer, CL_TRUE, 0, SIZE * sizeof(int), data, 0, NULL, NULL);
#     clEnqueueWriteBuffer(command_queue, data_buffer, CL_TRUE, 0, SIZE * sizeof(int), data, 0, NULL, NULL);
# 
#     // Execute kernel
#     size_t global_work_size = SIZE;
#     clEnqueueNDRangeKernel(command_queue, kernel, 1, NULL, &global_work_size, NULL, 0, NULL, NULL);
# 
#     // Copy data from device to host
#     int global_min;
#     clEnqueueReadBuffer(command_queue, global_min_buffer, CL_TRUE, 0, sizeof(int), &global_min, 0, NULL, NULL);
#     int global_max;
#     clEnqueueReadBuffer(command_queue, global_max_buffer, CL_TRUE, 0, sizeof(int), &global_max, 0, NULL, NULL);
# 
#     // Print the result
#     printf("Minimum element: %d\n", global_min);
#     printf("Maximum element: %d\n", global_max);
# 
#     // free up memory
#     clReleaseKernel(kernel);
#     clReleaseProgram(program);
#     clReleaseMemObject(data_buffer);
#     clReleaseMemObject(local_min_buffer);
#     clReleaseMemObject(local_max_buffer);
#     clReleaseMemObject(global_min_buffer);
#     clReleaseMemObject(global_max_buffer);
#     clReleaseCommandQueue(command_queue);
#     clReleaseContext(context);
# 
#     free(data);
# 
#     return 0;
# }
#
