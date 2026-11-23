package mark;
import java.io.*;
import java.util.*;

public class W3E1sugay {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int sugaychoice;
		
		do {
			System.out.println("\n1. Input New Student Record");
			System.out.println("2. View Student Record");
			System.out.println("3. Exit");
			System.out.print("Enter choice: ");
			sugaychoice = sc.nextInt();
			sc.nextLine();	
			
			switch (sugaychoice){
			
			case 1:
				try {
					FileWriter fw = new FileWriter("Mark.txt", true);
					
					System.out.print("Student Number: ");
					String number = sc.nextLine();
					
					System.out.print("Last Name: ");
					String last = sc.nextLine();
					
					System.out.print("First Name: ");
					String first = sc.nextLine();
					
					fw.write(number + ", " + last + ", " + first + "\n");
					fw.close();
					
					System.out.println("Record saved!");
				} catch(IOException e) {
					System.out.println("File error.");	
				}
				break;
				
			case 2: 
				try {
					FileReader fr = new FileReader("Mark.txt");
					int ch;
					
					System.out.println("\n--- STUDENT RECORDS ---");
					
					while((ch = fr.read()) != -1) {
						System.out.print((char)ch);
					}
					
					fr.close();
					
				}catch(IOException e) {
					System.out.println("No Result Found.");
				}
				break;
				
			case 3:
				System.out.println("Program exited.");
				break;
				
				default:
					System.out.println("Invalid choice.");				
			}
			
		}while(sugaychoice !=3);
		
		sc.close();
			
			
	
	}

}

