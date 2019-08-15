package com.ll.test;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.ie.InternetExplorerDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.remote.DesiredCapabilities;

public class TestSelenium {
    public static void main(String[] args) throws InterruptedException {
//       WebDriver driver=new ChromeDriver();
//        WebDriver driver=new InternetExplorerDriver();
//        System.getProperties().setProperty("webdriver.ie.driver","D:\\dev\\workspace\\ocweb\\libs\\IEDriverServer.exe");
        //System.setProperty("webdriver.ie.bin", "C:\\Program Files\\Internet Explorer\\iexplore.exe");
        //WebDriver webDriver = new InternetExplorerDriver();
//        DesiredCapabilities caps = DesiredCapabilities.internetExplorer();
//        caps.setCapability(InternetExplorerDriver.INTRODUCE_FLAKINESS_BY_IGNORING_SECURITY_DOMAINS,true);
        WebDriver driver=new FirefoxDriver();
        String url="http://dl.hbbank.cn/";
        url="https://www.baidu.com/";
        driver.get(url);
        String title=driver.getTitle();
        System.out.println(title);
        new Thread().sleep(5000);
        //等等
        driver.close();
    }


}
