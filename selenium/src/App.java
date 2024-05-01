import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;

public class App {
    public static void main(String[] args) {
        System.setProperty("webdriver.gecko.driver", "./geckodriver");
        WebDriver driver = new FirefoxDriver();
        driver.manage().window().maximize();
        driver.get("https://www.twitter.com");
        // driver.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);

        // 
        String signInXpath = "html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div";
        WebElement signButton =  driver.findElement(By.xpath(signInXpath));
        signButton.click();

        
        String email = "//*[@id=\"gsi_585536_810838-overlay\"]";
        WebElement emailInput = driver.findElement(By.xpath(email));
        // driver.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);
        emailInput.click();

        emailInput.sendKeys("");

                
    }
}