#!/bin/bash

# Enter the Module Name as per given below
read -p "Enter VTune module name: " vtune_module
module load $vtune_module

# Enter the project directory path
read -p "Enter project directory path: " folder_path
if [ ! -d "$folder_path" ]; then
  echo "Project directory does not exist"
  exit 1
fi

read -p "Enter executable file path: " exe_file
if [ ! -f "$exe_file" ]; then
  echo "Executable file does not exist"
  exit 1
fi

# Report should be store in this directory
report_dir="$folder_path/report"

# Check condition for the report directory 
if [ -d "$report_dir" ]; then
  read -p "Report directory already exists. Do you want to overwrite? (y/n): " response
  if [ "$response" != "y" ]; then
    echo "Exiting..."
    exit 1
  fi
  rm -r "$report_dir" 
fi

# Run command for the vtune
vtune_cmd="vtune --collect=hotspot --result-dir=$report_dir -- $exe_file"
$vtune_cmd

# Report should be generate in this
vtune-gui $report_dir
