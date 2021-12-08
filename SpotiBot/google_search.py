from botcity.web import WebBot, Browser
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *


class Bot(WebBot):
    def action(self, execution=None):
        # Configure whether or not to run on headless mode
        self.headless = False

        
        # Uncomment to change the default Browser to Firefox
        # self.browser = Browser.CHROME
        
        # Uncomment to set the WebDriver path
        self.driver_path = "C:/Users/Victor/Documents/GitHub/My Projects/Spotify Automation/My Bot/SpotiBot/drivers installation/drivers/chromedriver.exe"

        # Fetch the Activity ID from the task:
        # task = self.maestro.get_task(execution.task_id)
        # activity_id = task.activity_id

        # Opens the BotCity website.
        self.browse("https://www.google.com")
        
        self.feeling_lucky_click()

        # Uncomment to mark this task as finished on BotMaestro
        # self.maestro.finish_task(
        #     task_id=execution.task_id,
        #     status=AutomationTaskFinishStatus.SUCCESS,
        #     message="Task Finished OK."
        # )

        # Wait for 10 seconds before closing
        self.wait(10000)

        # Stop the browser and clean up
        self.stop_browser()

    def not_found(self, label):
        print(f"Element not found: {label}")
    
        #Search on feeling lucky
    def feeling_lucky_click(self):
        self.paste("Shall never Surrender")
        
        if not self.find( "button", matching=0.97, waiting_time=10000):
            self.not_found("button")
        self.click()
        
        
        


if __name__ == '__main__':
    Bot.main()








