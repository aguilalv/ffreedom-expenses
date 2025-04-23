from behave import given, when, then


@given("I am in the bank connection page")
def step_on_main_page(context):
    context.page.goto(f"{context.base_url}/bank/connect")


@when('I click on "Connect Bank"')
def step_click_connect_bank(context):
    context.page.click('text="Connect to your Bank"')


@then("I should see a list of available banks")
def step_see_bank_list(context):
    # Just verify that there's at least one bank visible
    context.page.wait_for_selector(".bank-list")
