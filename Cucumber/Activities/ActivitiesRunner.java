package testRunner;

import io.cucumber.junit.Cucumber;
import io.cucumber.junit.CucumberOptions;
import org.junit.runner.RunWith;

@RunWith(Cucumber.class)
@CucumberOptions(
        features = "Features",
        glue = {"stepDefinitions"},
        tags = "@activity5",
        plugin = {"pretty"},
        /**plugin = {"html: test-reports"},
         plugin = {"json: test-reports/json-report.json"}**/
        monochrome = true
)
public class ActivitiesRunner {

}
