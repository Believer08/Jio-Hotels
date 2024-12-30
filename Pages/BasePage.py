import time

from selenium.common import TimeoutException, NoSuchElementException, StaleElementReferenceException, \
    ElementClickInterceptedException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    """ selenium wrapper """

    def find_element(self, locator, timeout=None):
        """Find an element on the page."""
        try:
            return WebDriverWait(self.driver, timeout or self.timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            log.logger.info(f"Element with locator {locator} not found within {timeout or self.timeout} seconds")
            raise Exception(f"Element with locator {locator} not found within {timeout or self.timeout} seconds")

    def find_elements(self, locator, timeout=None):
        """Find a list of elements on the page."""
        try:
            return WebDriverWait(self.driver, timeout or self.timeout).until(
                EC.visibility_of_all_elements_located(locator)
            )
        except TimeoutException:
            log.logger.info(f"Element with locator {locator} not found within {timeout or self.timeout} seconds")
            raise Exception(f"Elements with locator {locator} not found within {timeout or self.timeout} seconds")

    def click(self, locator):
        attempts = 0
        while attempts < 3:
            try:
                element = self.find_element(locator)
                element.click()
                log.logger.info(f"Clicking on element " + str(locator))
                return
            except StaleElementReferenceException:
                attempts += 1
            except ElementClickInterceptedException:
                attempts += 1
        log.logger.info(f"Element not found after retries.")
        raise Exception(f"Element not found after retries.")

    def double_click(self, locator):
        """Double-click on an element."""
        element = self.find_element(locator)
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        log.logger.info(f"Double clicking on element " + str(locator))

    def send_keys(self, locator, text):
        """Send keys to an input field."""
        element = self.find_element(locator)
        element.send_keys(text)
        log.logger.info(f"Typing into element: " + str(locator) + " text: " + str(text))

    def is_element_visible(self, locator):
        """Check if an element is visible on the page."""
        try:
            element = self.find_element(locator)
            return element.is_displayed()
        except NoSuchElementException:
            return False

    def is_element_present(self, locator):
        """Check if an element is present on the page."""
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def get_element_attribute(self, locator, attribute):
        """Get an attribute value of an element."""
        element = self.find_element(locator)
        log.logger.info(f"Attributes of the element " + str(locator) + " is " + str(element.get_attribute(attribute)))
        return element.get_attribute(attribute)

    def get_element_text(self, locator):
        """Get text of a specific element."""
        element = self.find_element(locator)
        log.logger.info(f"Text of the element " + str(locator) + " is " + str(element.text))
        return element.text

    def get_page_title(self):
        """Get the title of the current page."""
        log.logger.info(f"Title of the current page : " + str(self.driver.title))
        return self.driver.title

    def navigate_to(self, url):
        """Navigate to a specific URL."""
        log.logger.info(f"Navigating to URL : " + str(url))
        self.driver.get(url)

    def take_screenshot(self, file_path):
        """Take a screenshot of the current page."""
        log.logger.info(f"Saving screenshot at : " + str(file_path))
        self.driver.save_screenshot(file_path)

    def refresh_page(self):
        """Refresh the current page."""
        log.logger.info(f"Browser refreshed")
        self.driver.refresh()

    def press_enter(self, locator):
        """Press the 'Enter' key on a specific element."""
        element = self.find_element(locator)
        element.send_keys(Keys.ENTER)
        log.logger.info(f"Pressed Enter key on element : " + str(locator))

    def hover_over_element(self, locator):
        """Hover over an element."""
        element = self.find_element(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        log.logger.info(f"Hovering on element : " + str(locator))

    """ selenium waits """

    def wait_for_element_to_be_clickable(self, locator, timeout=None):
        """Wait for an element to be clickable."""
        try:
            return WebDriverWait(self.driver, timeout or self.timeout).until(
                EC.element_to_be_clickable(locator)
            )
        except TimeoutException:
            log.logger.info(f"Element with locator {locator} not clickable within {timeout or self.timeout} seconds")
            raise Exception(f"Element with locator {locator} not clickable within {timeout or self.timeout} seconds")

    def wait_for_element_to_be_invisible(self, locator, timeout=None):
        """Wait for an element to become invisible."""
        try:
            WebDriverWait(self.driver, timeout or self.timeout).until(
                EC.invisibility_of_element(locator)
            )
        except TimeoutException:
            log.logger.info(
                f"Element with locator {locator} did not disappear within {timeout or self.timeout} seconds")
            raise Exception(
                f"Element with locator {locator} did not disappear within {timeout or self.timeout} seconds")

    def wait_for_element_to_disappear(self, locator, timeout=None):
        """Wait for an element to disappear from the page."""
        try:
            WebDriverWait(self.driver, timeout or self.timeout).until(
                EC.invisibility_of_element_located(locator)
            )
        except TimeoutException:
            log.logger.info(
                f"Element with locator {locator} did not disappear within {timeout or self.timeout} seconds")
            raise Exception(
                f"Element with locator {locator} did not disappear within {timeout or self.timeout} seconds")

    def wait_for_url_to_contain(self, text, timeout=None):
        """Wait until the URL contains a specific text."""
        try:
            WebDriverWait(self.driver, timeout or self.timeout).until(
                EC.url_contains(text)
            )
        except TimeoutException:
            log.logger.info(f"URL did not contain {text} within {timeout or self.timeout} seconds")
            raise Exception(f"URL did not contain {text} within {timeout or self.timeout} seconds")

    def wait_for_page_load(self):
        """Wait for the page to completely load."""
        try:
            WebDriverWait(self.driver, self.timeout).until(
                lambda driver: self.driver.execute_script("return document.readyState") == "complete"
            )
        except TimeoutException:
            log.logger.info(f"Page did not load completely within the given time.")
            raise Exception("Page did not load completely within the given time.")

    def fluent_wait(self, locator, poll_frequency=0.5, timeout=30):
        """Fluent wait to wait for an element with custom polling frequency."""
        wait = WebDriverWait(self.driver, timeout, poll_frequency=poll_frequency,
                             ignored_exceptions=[NoSuchElementException])
        return wait.until(EC.visibility_of_element_located(locator))

    """ scrolls """

    def scroll_to_element(self, locator):
        """Scroll to a specific element on the page."""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        log.logger.info(f"scrolling to element: " + str(locator))

    def scroll_by(self, x, y):
        """Scroll by a specific x, y offset."""
        self.driver.execute_script(f"window.scrollBy({x}, {y})")
        log.logger.info(f"scrolling by offset X: " + str(x) + " and Y: " + str(y))

    def scroll_to_bottom(self):
        """Scroll to the bottom of the page."""
        time.sleep(1)
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
        time.sleep(1)
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        log.logger.info(f"Scrolling into tbe bottom of the page")

    """ Frame & alerts """

    def switch_to_frame(self, locator):
        """Switch to an iframe using its locator."""
        frame = self.find_element(locator)
        self.driver.switch_to.frame(frame)
        log.logger.info(f"Switching to frame")

    def switch_to_default_content(self):
        """Switch back to the default content (main page)."""
        self.driver.switch_to.default_content()
        log.logger.info(f"switch_to_default_content")

    def handle_alert(self, accept=True):
        """Handle browser alerts."""
        alert = WebDriverWait(self.driver, self.timeout).until(EC.alert_is_present())
        if accept:
            alert.accept()
        else:
            alert.dismiss()

    def switch_to_new_window(self):
        """Switch to the most recently opened window."""
        current_window = self.driver.current_window_handle
        windows = self.driver.window_handles
        for window in windows:
            if window != current_window:
                self.driver.switch_to.window(window)

    def close_current_window(self):
        """Close the current browser window."""
        self.driver.close()
        log.logger.info(f"closing the current window")

    def switch_to_window(self, window_name):
        """Switch to a specific window by name or handle."""
        self.driver.switch_to.window(window_name)
        log.logger.info(f"switching to new window " + str(window_name))

    def close_alert_and_get_its_text(self):
        """Close an alert box and return the alert text."""
        alert = WebDriverWait(self.driver, self.timeout).until(EC.alert_is_present())
        text = alert.text
        alert.accept()
        log.logger.info(f"close_alert_and_get_its_text : " + str(text))
        return text

    """ Dropdown selection """

    def select_dropdown_by_value(self, locator, value):
        """Select an option from a dropdown by value."""
        element = self.find_element(locator)
        select = Select(element)
        select.select_by_value(value)
        log.logger.info(f"selecting {locator} by value {value}")

    def select_dropdown_by_visible_text(self, locator, text):
        """Select an option from a dropdown by visible text."""
        element = self.find_element(locator)
        select = Select(element)
        select.select_by_visible_text(text)
        log.logger.info(f"selecting {locator} by text {text}")

    """ Drag & Drop """

    def drag_and_drop(self, source_locator, target_locator):
        """Drag an element and drop it to another element."""
        source_element = self.find_element(source_locator)
        target_element = self.find_element(target_locator)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_element, target_element).perform()
        log.logger.info(f"drag from {source_locator} drop to {target_locator}")

    def drag_element(self, source_locator, x_offset, y_offset):
        """Drag an element by an offset."""
        source_element = self.find_element(source_locator)
        actions = ActionChains(self.driver)
        actions.drag_and_drop_by_offset(source_element, x_offset, y_offset).perform()
        log.logger.info(f"drag element {source_locator} drop to {x_offset} {y_offset}")

    def resize_element(self, source_locator, x_offset, y_offset):
        """Resize an element by dragging from the corner."""
        element = self.find_element(source_locator)
        actions = ActionChains(self.driver)
        actions.click_and_hold(element).move_by_offset(x_offset, y_offset).release().perform()
        log.logger.info(f"resize_element {source_locator}  : {x_offset} and {y_offset}")

    """ Cookies """

    def add_cookie(self, cookie_dict):
        """Add a cookie to the browser."""
        self.driver.add_cookie(cookie_dict)
        log.logger.info(f"adding cookies")

    def get_cookies(self):
        """Get all browser cookies."""
        return self.driver.get_cookies()

    def delete_cookie(self, cookie_name):
        """Delete a specific cookie."""
        self.driver.delete_cookie(cookie_name)
        log.logger.info(f"deleting cookies")

    def delete_all_cookies(self):
        """Delete all cookies."""
        self.driver.delete_all_cookies()
        log.logger.info(f"deleting all cookies")

    def capture_network_logs(self):
        """Capture network logs using performance logging."""
        logs = self.driver.get_log('performance')
        return logs

    def download_file(self, url, save_path):
        """Download a file using JavaScript execution."""
        self.driver.execute_script(f"window.location.href='{url}';")
        time.sleep(5)  # Wait for download to complete (adjust as necessary)
        self.take_screenshot(save_path)  # Capture screenshot to verify download

    def upload_file(self, locator, file_path):
        """Upload a file by sending the file path to an input field."""
        element = self.find_element(locator)
        element.send_keys(file_path)

    def execute_script(self, locator):
        """Execute JavaScript."""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)
        log.logger.info("Clicking on element " + str(locator) + " using execute_script")

    def return_elements_count(self, locator, timeout=None):
        """return number of element present in DOM."""
        try:
            ele = WebDriverWait(self.driver, timeout or self.timeout).until(
                EC.visibility_of_all_elements_located(locator))
            log.logger.info(f"count of th element {locator} is : " + str(len(ele)))
            return len(ele)
        except TimeoutException:
            return 0
