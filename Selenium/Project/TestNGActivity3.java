import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.testng.Assert;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;
public class TestNGActivity3 {
    WebDriver driver;

    @BeforeMethod
    public void beforeMethod() {
        // Set up the Firefox driver
        WebDriverManager.firefoxdriver();
        //Create a new instance of the Firefox driver
        driver = new FirefoxDriver();

        //Open browser
        driver.get("https://alchemy.hguy.co/jobs");
    }


    @Test
    public void exampleTestCase() {
        // Check the title of the page
        // Find the image element using a specific attribute, such as src
        WebElement imageElement = driver.findElement(By.tagName("img"));

        // Get the value of the src attribute, which contains the URL of the image
        String imageURL = imageElement.getAttribute("src");

        // Print the image URL

        System.out.println("Image URL: " + imageURL);

    }

    @AfterMethod
    public void afterMethod() {
        //Close the browser
        driver.quit();
    }


}
