package com.selenium_tests.testCases;

import com.selenium_tests.utilities.ReadConfig;

import org.apache.log4j.Logger;
import org.apache.log4j.PropertyConfigurator;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;

public class TCBaseClass {
    ReadConfig rc = new ReadConfig();
    public String baseURL = rc.getApplicationURL();
    public String username = rc.getUserName();
    public String password = rc.getPassword();
    public static WebDriver driver;
    public static Logger logger;

    @BeforeClass
    public void setup() {
        System.setProperty("webdriver.chrome.driver", System.getProperty("user.dir") + "\\Drivers\\chromedriver.exe");
        driver = new ChromeDriver();

        logger = Logger.getLogger(TCBaseClass.class);
        PropertyConfigurator.configure("log4j.properties");
    }

    @AfterClass
    public void tearDown() {
        driver.quit();
    }
}
