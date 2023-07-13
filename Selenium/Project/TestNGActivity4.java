import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.testng.Assert;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

public class TestNGActivity4 {

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
        String heading = driver.findElement(By.tagName("h2")).getText();

        //Print the title of the page
        System.out.println("Page title is: " + heading);

        //Assertion for page title
        Assert.assertEquals("Quia quis non", heading);

    }

    @AfterMethod
    public void afterMethod() {
        //Close the browser
        driver.quit();
    }
}
