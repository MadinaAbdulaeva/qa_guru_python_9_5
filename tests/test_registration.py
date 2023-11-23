from selene import browser, by, have
import os.path

def test_registration(browser_management):
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Madina')
    browser.element('#lastName').type('ABDULAEVA')
    browser.element('#userEmail').type('i@mabdulaeva.ru')
    browser.element('#gender-radio-2').double_click()
    browser.element('#userNumber').type('9258880099')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element(by.text('October')).click()
    browser.element('.react-datepicker__year-select').click().element(by.text('1998')).click()
    browser.element('.react-datepicker__day--020').click()

    browser.element('#subjectsInput').type('AUTOtests')
    browser.element('#hobbies-checkbox-3').double_click()

    browser.element('#uploadPicture').send_keys(os.path.abspath('/Users/elearner/Documents/plumeria.jpg'))
    browser.element('#currentAddress').type('Jerome Hanks Str., h.149, apt.09')

    browser.element('#react-select-3-input').type('Uttar Pradesh').press_enter()
    browser.element('#react-select-4-input').type('Karnal').press_enter()
    browser.element('#submit').press_enter()

    browser.element('.modal-header').should(have.text('Thanks for submitting the form'))
    browser.element('.table-responsive').should(have.text(
    'Madina ABDULAEVA' and
    'i@mabdulaeva.ru' and
    'Female' and
    '9258880099' and
    '20 October,1998' and
    'AUTOtests' and
    'Music' and
    'plumeria.jpg' and
    'Jerome Hanks Str., h.149, apt.09' and
    'Uttar Pradesh Karnal' ))

    browser.element('#closeLargeModal').press_enter()











