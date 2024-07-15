//write a menu driven java program to store customer details 
//save customer
//display all customer
// movie detailes :customer name,gender , phone


import java.util.Scanner;

public class Movie {
    private String customerName;
    private String gender;
    private String phone;

    public Movie(String customerName, String gender, String phone) {
        this.customerName = customerName;
        this.gender = gender;
        this.phone = phone;
    }

    public String getCustomerName() {
        return customerName;
    }

    public void setCustomerName(String customerName) {
        this.customerName = customerName;
    }

    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }

    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Movie[] movies = new Movie[100];
        int count = 0;
    }
        while (true) {
            System.out.println("Menu:");
            System.out.println("1. Save customer");
            System.out.println("2. Display all customer");
            System.out.println("3. Exit");
            System.out.print("Enter your choice: ");
        
            int choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline

            switch (choice) {
                case 1:
                    System.out.print("Enter customer name: ");
                    String customerName = scanner.nextLine();
                    System.out.print("Enter gender: ");
                    String gender = scanner.nextLine();
                    System.out.print("Enter phone: ");
                    String phone = scanner.nextLine();

                    movies[count] = new Movie(customerName, gender, phone);
                    count++;
                    System.out.println("Customer saved successfully.");
                    break;
                case 2:
                    if (count == 0) {
                        System.out.println("No customers saved yet.");
                    } else {
                        System.out.println("Customer details:");
                        for (int i = 0; i < count; i++) {
                            System.out.println("Customer " + (i + 1) + ":");
                            System.out.println("Name: " + movies[i].getCustomerName());
                            System.out.println("Gender: " + movies[i].getGender());
                            System.out.println("Phone: " + movies[i].getPhone());
                            System.out.println();
                        }
                    }
                    break;
                case 3:
                    System.out.println("Exiting...");
                    scanner.close();
                    System.exit(0);
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
    }
}
