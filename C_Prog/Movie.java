import java.util.Scanner;

public class Movie {
    private String customerName;
    private String gender;
    private int phone;
    private String movieDetails;

    public Movie(String customerName, String gender, int phone, String movieDetails) {
        this.customerName = customerName;
        this.gender = gender;
        this.phone = phone;
        this.movieDetails = movieDetails;
    }
    
// getter function
    public String getCustomerName(){
        return customerName;
    }
    public String getgender(){
        return gender;
    
    }
    public int getPhone(){
        return phone;

    }
    public String getMovieDetails(){
        return movieDetails;
    }

// setter function
    public void setCustomerName(String customerName){
        this.customerName = customerName;
    }
    public void setGender(String gender){
        this.gender = gender;
    }
    public void setPhone(int phone){
        this.phone = phone;
    }
    public void setMobvieDetails(String movieDetails){
        this.movieDetails = movieDetails;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("enter the customer name");
        String customerName = scanner.nextLine();
        System.out.println("enter the gender");
        String gender = scanner.nextLine();
        System.out.println("enter the phone number");
        int phone = scanner.nextInt();
        System.out.println("enter the movie details");
        String movieDetails = scanner.nextLine();
        Movie Details = new Movie(customerName, gender, phone, movieDetails);
        int choice = 0;
        while(choice != 4);
        System.out.println("enter the choice: ");
        System.out.println("1.customer name");
        System.out.println("2.gender");
        System.out.println("3.phone number");
        System.out.println("4.movie details");
        System.out.println("5.exit");
        choice = scanner.nextInt();
        switch(choice){
            case 1:
                System.out.println("customer name: " + Details.getCustomerName());
                break;

            case 2:
            System.out.println("gender: " + Details.getgender());
            break;

            case 3:
            System.out.println("phone number: " + Details.getPhone());
            break;

            case 4:
            System.out.println("movie details: " + Details.getMovieDetails());
            break;

            case 5:
            System.out.println("exit");
            break;

            default:
            System.out.println("invalid choice");
            break;
        }
        scanner.close();

    System.out.println("movie details" + Details.getMovieDetails()+ "customer name " + Details.getCustomerName() + "gender" + Details.getgender() + "phone number" + Details.getPhone());
        
    }
    
}