package com.selenium_tests.testCases;

import java.util.concurrent.TimeUnit;

import com.selenium_tests.pageObjects.LoginPage;

import org.openqa.selenium.By;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.Assert;
import org.testng.annotations.Test;

public class TC_LoginTest_001 extends TCBaseClass {
    private String EXPECTED_TITLE = "Dashboard - PHPTRAVELS";

    @Test
    public void loginTest() {
        driver.get(baseURL);
        driver.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);

        LoginPage page = new LoginPage(driver);
        page.setUserName(username);
        page.setPassword(password);
        page.clickSubmit();
        
        WebDriverWait waitLogin = new WebDriverWait(driver, 30);
        waitLogin.until(ExpectedConditions.presenceOfElementLocated(By.xpath("//title")));
        Assert.assertEquals(driver.getTitle(), EXPECTED_TITLE);      
    }
}
