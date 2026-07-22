import re
from playwright.sync_api import Page, expect

def test_ebay_search_pokemon_cards(page: Page):
    """
    Test Case: Verify that searching for 'Pokemon cards' on eBay 
    returns relevant search results and loads the results page.
    """
    # 1. Navigate to eBay homepage
    page.goto("https://www.ebay.com")
    
    # 2. Locate the search bar and enter the search term
    search_input = page.locator("input[type='text']#gh-ac")
    expect(search_input).to_be_visible()
    search_input.fill("Pokemon cards")
    
    # 3. Click the search button
    search_button = page.locator("input[type='submit']#gh-btn")
    search_button.click()
    
    # 4 Assertion: Verify that the page title contains "Pokemon cards"
    expect(page).to_have_title(re.compile("Pokemon cards", re.IGNORECASE))
    
    #5. Assertion: Verify that the search results container is present
    results_container = page.locator("#srp-river-results")
    expect(results_container).to_be_visible()
    
    #6. Take screenshot as proof of execution
    page.screenshot(path="automation/screenshots/search_results.png")
