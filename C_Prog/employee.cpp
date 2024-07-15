// //write a menu driven c++ program to store employee details 
// save employee 
// display employee
// employee details: empid employee name

#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

struct Employee {
    int empid;
    string name;
};

void addEmployee(vector<Employee>& employees) {
    Employee employee;
    cout << "Enter employee ID: ";
    cin >> employee.empid;
    cout << "Enter employee name: ";
    cin.ignore(); // Ignore the newline character from the previous input
    getline(cin, employee.name);
    employees.push_back(employee);
    cout << "Employee added successfully!" << endl;
}

void saveEmployees(const vector<Employee>& employees, const string& filename) {
    ofstream outfile(filename);
    if (outfile.is_open()) {
        for (const Employee& employee : employees) {
            outfile << employee.empid << "," << employee.name << endl;
        }
        outfile.close();
        cout << "Employees saved to " << filename << endl;
    } else {
        cout << "Error saving employees to file." << endl;
    }
}

void displayEmployees(const vector<Employee>& employees) {
    if (employees.empty()) {
        cout << "No employees found." << endl;
    } else {
        for (const Employee& employee : employees) {
            cout << "Employee ID: " << employee.empid << endl;
            cout << "Employee Name: " << employee.name << endl;
            cout << endl;
        }
    }
}

int main() {
    vector<Employee> employees;
    int choice;

    do {
        cout << "\nMenu:" << endl;
        cout << "1. Add employee" << endl;
        cout << "2. Save employees" << endl;
        cout << "3. Display employees" << endl;
        cout << "4. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                addEmployee(employees);
                break;
            case 2:
                saveEmployees(employees."employees.txt")
                break;
            case 3:
                displayEmployees(employees);
                break;
            case 4:
                cout << "Existing program." << endl;
                break;
            default:
            cout << "Invalid choice. Please try again." <<endl;
        }
    }while (choice !=4);
    if (choice == 4)
    {
        return 0;
    }
    return 0;
}

    