import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.Select;  

public class DemoTest {

	public static void main(String[] args) {
		// declaration and installtiation of objects/varibles
		System.setProperty("webdriver.chrome.driver",
				"C:\\Users\\QIZHAOR\\Desktop\\PROGRAM\\WebDevelop\\StudyRoom\\python\\chromedriver.exe");
		WebDriver driver=new ChromeDriver();  
	      
		 driver.navigate().to("https://www.testandquiz.com/selenium/testing.html");  
	      
	        // Fetch the text "This is sample text." and print it on console  
	        // Use the class name of the div to locate it and then fetch text using getText() method  
	     String sampleText = driver.findElement(By.className("col-md-12")).getText();  
	     System.out.println(sampleText);  
	          
	          // Use the linkText locator method to find the link and perform click using click() method  
	     driver.findElement(By.linkText("This is a link")).click();  
	       
	          // Click on the textbox and send value  
//	     driver.findElement(By.id("fname")).sendKeys("JavaTpoint");  
//	       
//	        // Clear the text written in the textbox  
//	     driver.findElement(By.id("fname")).clear();  
//	          
//	        // Click on the Submit button using click() command  
//	     driver.findElement(By.id("idOfButton")).click();  
//	   
//	        // Locate the radio button by id and check it using click() function  
//	     driver.findElement(By.id("male")).click();  
//	          
//	        // Locate the checkbox by cssSelector and check it using click() function  
//	     driver.findElement(By.cssSelector("input.Automation")).click();  
//	              
//	        // Use Select class for selecting value from dropdown  
//	    Select dropdown = new Select(driver.findElement(By.id("testingDropdown")));  
//	    dropdown.selectByVisibleText("Automation Testing");  
//	       
//	        // Close the Browser  
//	             driver.close();  
	      
	    }  
	  
	}  